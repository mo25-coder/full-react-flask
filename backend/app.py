from flask import Flask, request, session, jsonify, render_template
from werkzeug.security import check_password_hash
from flask_wtf.csrf import CSRFProtect
from forms import SignUpForm
from flask_cors import CORS
from models import db, WatchLater, Show
from functions import execute_query
app = Flask(__name__)
app.config.from_object("config.Config")
from flask_session import Session

# CORS(app)  # Enable CORS for frontend requests
CORS(app, supports_credentials=True)
csrf = CSRFProtect(app)  # Protect against CSRF attacks
app.secret_key = "secret_key"
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config.update(
    SESSION_COOKIE_SAMESITE='None',
    SESSION_COOKIE_SECURE=True
)
# app.config['DEBUG'] = True
Session(app)

database = "prime_video.db"

@app.route("/", methods=["GET"])
def main():
    return jsonify({"message": "Welcome to Prime Video API"}), 200


@csrf.exempt
@app.route("/signin", methods=["POST", "GET"])
@app.route("/SignIn", methods=["GET", "POST"])
def signin():
    # test
    # query = "SELECT * FROM user"
    # rows = execute_query(database, query, fetch=True)
    # print(rows)
    if request.method == "POST":

        # Execute query to fetch user by username
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
        if request.form:
            username = request.form.get("username")
            password = request.form.get("password")
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        # print("Headers:", dict(request.headers))
        # print("Body:", request.get_data())
        # print("JSON:", request.get_json())
        # print("Headers:", dict(request.headers))
        # print("JSON body:", request.get_json())
        if not username or not password:
            return jsonify({"error": "Missing username or password"}), 400

        # query = "SELECT * FROM user WHERE username = ?"
        # rows = execute_query(database, query, request.form.get("username"), fetch=True)
        query = "SELECT * FROM user WHERE email = ?"
        rows = execute_query(database, query, username, fetch=True)

        print(rows)
        # Check if the user exists and verify the password (password is hashed in the database)
        # if len(rows) != 1 or not check_password_hash(rows[0][3], request.form.get("password")):
        if len(rows) != 1 or rows[0][3] != password:
            return jsonify({"error": "Invalid username or password"}), 400

        session["user_id"] = rows[0][0]
        print("User ID:", session["user_id"])

        return jsonify({"logged_in": True, "message": "Login successful"}), 200

    elif request.method == "GET":
        print("Cookies:", request.cookies)
        print("Session:", dict(session))
        print("Session content:", dict(session))
        return jsonify({"logged_in": "user_id" in session}), 200
        # return jsonify({"logged_in": session['user_id']}), 200
        
        # return render_template("login.html", {"csrf_token": csrf.generate_csrf()})
    
# SignUp Route
@app.route("/signup", methods=["POST","GET"])
def signup():
    # test
    # query = "INSERT INTO user (name, email, password) VALUES (?, ?, ?)"
    # data = ("name", "email_or_phone", "password")
    # execute_query(database, query, data)
    # print("done")
    form = SignUpForm()
    if form.validate_on_submit():
        # Capture form data
        name = form.name.data
        email_or_phone = form.email_or_phone.data
        password = form.password.data
        # insert into database
        query = "INSERT INTO user (name, email_or_phone, password) VALUES (?, ?, ?)"
        data = (name, email_or_phone, password)
        execute_query(database, query, data)
        # conn = sqlite3.connect('prime_video.db')

        
        # Dummy response (In real app, you should store in a database)
        return jsonify({
            "success": True,
            "message": "Account created successfully!",
            "data": {
                "name": name,
                "email_or_phone": email_or_phone
            }
        }), 201

    return jsonify({"success": False, "errors": form.errors}), 400

@app.route("/watch-later/<int:user_id>", methods=["GET"])
def get_watch_later(user_id):
    """Fetch watch later list for a specific user."""
    watch_later_entries = WatchLater.query.filter_by(user_id=user_id).all()

    if not watch_later_entries:
        return jsonify({"message": "No shows in watch later list"}), 404

    watch_later_list = [
        {
            "show_id": entry.show.id,
            "title": entry.show.title,
            "description": entry.show.description,
            "image_url": entry.show.image_url
        }
        for entry in watch_later_entries
    ]

    return jsonify(watch_later_list), 200


# send all shows categorized (drama,comedy,..) tables show and category form database to frontend
@app.route("/shows", methods=["GET"])
def get_shows():
    """Fetch all shows from the database."""
    query = """
                SELECT 
                    s.id, 
                    s.name, 
                    s.description, 
                    s.image, 
                    c.name AS category_name
                FROM 
                    Show AS s
                JOIN 
                    Category AS c ON s.Category_id = c.id;


    """
    rows = execute_query(database, query, fetch=True)
    if not rows:
        return jsonify({"error": "No shows found"}), 404
    else:
        shows = [{"id": row[0], "title": row[1], "description":
                row[2], "image_url": row[3], "category_name": row[4]} for row in rows]
        return jsonify(shows), 200
    
# @app.route("/shows", methods=["GET"])
# def get_shows():
#     """Fetch all shows from the database."""
#     query = "SELECT * FROM Show"
#     rows = execute_query(database, query, fetch=True)
#     if not rows:
#         return jsonify({"error": "No shows found"}), 404
#     else:
#         shows = [{"id": row[0], "title": row[1], "description":
#                 row[2], "image_url": row[3]} for row in rows]
#         return jsonify(shows), 200
# @app.route("/shows", methods=["GET"])
# def shows():
#     query = "SELECT * FROM shows"
#     rows = execute_query(database, query, fetch=True)
#     if not rows:
#         return jsonify({"error": "No shows found"}), 404
#     else:
#         shows = [{"id": row[0], "title": row[1], "description":
#                 row[2], "image_url": row[3]} for row in rows]
#         return jsonify(shows), 200



@app.route("/user-data", methods=["GET"])
def userdata():
    """Fetch data for a specific user."""
    # rows = execute_query(database, """
    #                                 SELECT 
    #                                     u.id AS user_id, 
    #                                     u.name AS user_name, 
    #                                     u.email AS user_email, 
    #                                     s.id AS show_id, 
    #                                     s.name AS show_name, 
    #                                     s.description AS show_description, 
    #                                     s.rating AS show_rating, 
    #                                     s.time AS show_time, 
    #                                     s.age_limit AS show_age_limit, 
    #                                     s.Category AS show_category, 
    #                                     c.id AS category_id, 
    #                                     c.name AS category_name,
    #                                     CASE WHEN l.show_id IS NOT NULL THEN 1 ELSE 0 END AS is_liked, 
    #                                     CASE WHEN d.show_id IS NOT NULL THEN 1 ELSE 0 END AS is_disliked,
    #                                     CASE WHEN w.show_id IS NOT NULL THEN 1 ELSE 0 END AS is_watch_later
    #                                 FROM 
    #                                     user u
    #                                 JOIN 
    #                                     Category c ON 1=1
    #                                 JOIN 
    #                                     Show s ON s.Category_id = c.id
    #                                 LEFT JOIN 
    #                                     like l ON l.user_id = u.id AND l.show_id = s.id
    #                                 LEFT JOIN 
    #                                     dislike d ON d.user_id = u.id AND d.show_id = s.id
    #                                 LEFT JOIN 
    #                                     watch_later w ON w.user_id = u.id AND w.show_id = s.id
    #                                 WHERE 
    #                                     u.id = ?;
    #                      """, session["user_id"] ,fetch=True)
    # test
    rows = execute_query(database, """
                                    SELECT 
                                        u.id AS user_id, 
                                        u.name AS user_name, 
                                        u.email AS user_email, 
                                        s.id AS show_id, 
                                        s.name AS show_name, 
                                        s.description AS show_description, 
                                        s.rating AS show_rating, 
                                        s.time AS show_time, 
                                        s.age_limit AS show_age_limit, 
                                        s.Category AS show_category, 
                                        c.id AS category_id, 
                                        c.name AS category_name,
                                        CASE WHEN l.show_id IS NOT NULL THEN 1 ELSE 0 END AS is_liked, 
                                        CASE WHEN d.show_id IS NOT NULL THEN 1 ELSE 0 END AS is_disliked,
                                        CASE WHEN w.show_id IS NOT NULL THEN 1 ELSE 0 END AS is_watch_later
                                    FROM 
                                        user u
                                    JOIN 
                                        Category c ON 1=1
                                    JOIN 
                                        Show s ON s.Category_id = c.id
                                    LEFT JOIN 
                                        like l ON l.user_id = u.id AND l.show_id = s.id
                                    LEFT JOIN 
                                        dislike d ON d.user_id = u.id AND d.show_id = s.id
                                    LEFT JOIN 
                                        watch_later w ON w.user_id = u.id AND w.show_id = s.id
                                    WHERE 
                                        u.id = 2;
                        """,fetch=True)
    print("Session:", dict(session))
    
    if not rows:
        return jsonify({"error": "User not found"}), 404
    else:
        user_data = {
            "id": rows[0][0],
            "name": rows[0][1],
            "email_or_phone": rows[0][2],
            "shows": [],
            "islogged_in": True
        }

        # Iterate through the rows and organize the show and category data
        for row in rows:
            show_data = {
                "show_id": row[3],
                "show_name": row[4],
                "show_description": row[5],
                "show_rating": row[6],
                "show_time": row[7],
                "show_age_limit": row[8],
                "show_category": row[9],
                "category_id": row[10],
                "category_name": row[11],
                "is_liked": bool(row[12]),         # 1 means liked, 0 means not liked
                "is_disliked": bool(row[13]),      # 1 means disliked, 0 means not disliked
                "is_watch_later": bool(row[14])    # 1 means in watchlist, 0 means not
            }

            # Add the show data to the user's shows list
            user_data['shows'].append(show_data)

        return jsonify(user_data), 200
    
    
# get liked shows input from user and insert into database
@app.route("/like", methods=["POST"])
def like_show():
    data = request.json
    user_id = session["user_id"]
    show_id = data.get("show_id")
    # Check if the user has already liked the show
    existing_like = execute_query(database, "SELECT * FROM like WHERE user_id = ? AND show_id = ?", (user_id, show_id), fetch=True)
    if existing_like:
        return jsonify({"message": "Show already liked"}), 400
    else:
        # Insert the like into the database
        execute_query(database, "INSERT INTO like (user_id, show_id) VALUES (?, ?)", (user_id, show_id))
        return jsonify({"message": "Show liked successfully"}), 200
    
# get liked shows input from user and insert into database
@app.route("/dislike", methods=["POST"])
def dislike_show():
    data = request.json
    user_id = session["user_id"]
    show_id = data.get("show_id")
    # Check if the user has already disliked the show
    existing_dislike = execute_query(database, "SELECT * FROM dislike WHERE user_id = ? AND show_id = ?", (user_id, show_id), fetch=True)
    if existing_dislike:
        return jsonify({"message": "Show already disliked"}), 400
    else:
        # Insert the dislike into the database
        execute_query(database, "INSERT INTO dislike (user_id, show_id) VALUES (?, ?)", (user_id, show_id))
        return jsonify({"message": "Show disliked successfully"}), 200
    
# add to watch later
@app.route("/watch-later", methods=["POST"])
def add_to_watch_later():
    data = request.json
    user_id = session["user_id"]
    show_id = data.get("show_id")
    
    # Check if the show is already in the watch later list
    existing_entry = execute_query(database, "SELECT * FROM watch_later WHERE user_id = ? AND show_id = ?", (user_id, show_id), fetch=True)
    
    if existing_entry:
        return jsonify({"message": "Show already in watch later list"}), 400
    else:
        # Insert the show into the watch later list
        execute_query(database, "INSERT INTO watch_later (user_id, show_id) VALUES (?, ?)", (user_id, show_id))
        return jsonify({"message": "Show added to watch later list"}), 200
