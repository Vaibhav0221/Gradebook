from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from werkzeug.exceptions import HTTPException
from flask import make_response
import json

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Users/vaibhav/Desktop/iit madras/week_5/database.sqlite3"
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'database.sqlite3')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_database.sqlite3'
app.app_context().push()
api=Api(app)

db = SQLAlchemy()
db.init_app(app)

class NotFoundError(HTTPException):
    def __init__(self,status_code):
        self.response=make_response('', status_code)

class Error(HTTPException):
    def __init__(self,status_code,error_code,error_message):
        message={
            "error_code":error_code,
            "error_message":error_message
        }
        self.response=make_response(json.dumps(message), status_code)

Course_output_fields={
    "course_id": fields.Integer,
    "course_name": fields.String,
    "course_code": fields.String,
    "course_description": fields.String
}
Student_output_fields={
    "student_id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "roll_number": fields.String
}
enrollment_fields = {
    'enrollment_id': fields.Integer,
    'student_id': fields.Integer,
    'course_id': fields.Integer
}

create_Cource_parser=reqparse.RequestParser()
create_Cource_parser.add_argument('course_name')
create_Cource_parser.add_argument('course_code')
create_Cource_parser.add_argument("course_description")

Update_Cource_parser=reqparse.RequestParser()
Update_Cource_parser.add_argument('course_name')
Update_Cource_parser.add_argument('course_code')
Update_Cource_parser.add_argument("course_description")

create_Student_parser=reqparse.RequestParser()
create_Student_parser.add_argument('first_name')
create_Student_parser.add_argument('last_name')
create_Student_parser.add_argument("roll_number")

Update_Student_parser=reqparse.RequestParser()
Update_Student_parser.add_argument('first_name')
Update_Student_parser.add_argument('last_name')
Update_Student_parser.add_argument("roll_number")

create_enroll_parser=reqparse.RequestParser()
create_enroll_parser.add_argument('course_id')

class CourseAPI(Resource):
    @marshal_with(Course_output_fields)
    def get(self,course_id):
        c=db.session.query(course).filter(course.course_id==course_id).first()
        if c:
            return c
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(Course_output_fields)
    def put(self,course_id):
        args=Update_Cource_parser.parse_args()
        course_ids = db.session.query(course.course_id).all()
        course_ids = [id[0] for id in course_ids]
        if course_id not in course_ids:
            raise NotFoundError(status_code=404)
        course_name=args.get("course_name",None)
        course_code=args.get("course_code",None)
        course_description=args.get("course_description",None)
        if course_name is None:
            raise Error(status_code=400,error_code="COURSE001",error_message="Course Name is required")
        if course_code is None:
            raise Error(status_code=400,error_code="COURSE002",error_message="Course Code is required")
        course_tobe_update= db.session.query(course).filter(course.course_id==course_id).first()
        course_tobe_update.course_name=course_name
        course_tobe_update.course_code=course_code
        course_tobe_update.course_description=course_description
        db.session.add(course_tobe_update)
        db.session.commit()
        return course_tobe_update


    @marshal_with(Course_output_fields)
    def delete(self,course_id):
        course_ids = db.session.query(course.course_id).all()
        course_ids = [id[0] for id in course_ids]
        if course_id not in course_ids:
            raise NotFoundError(status_code=404)
        course_tobe_delete= db.session.query(course).filter(course.course_id==course_id).first()
        db.session.delete(course_tobe_delete)
        db.session.commit()
        raise NotFoundError(status_code=200)


    @marshal_with(Course_output_fields)
    def post(self):
        args=create_Cource_parser.parse_args()
        course_codes = db.session.query(course.course_code).all()
        course_codes = [code[0] for code in course_codes]
        course_name=args.get("course_name",None)
        course_code=args.get("course_code",None)
        course_description=args.get("course_description",None)
        if course_name is None:
            raise Error(status_code=400,error_code="COURSE001",error_message="Course Name is required")
        if course_code is None:
            raise Error(status_code=400,error_code="COURSE002",error_message="Course Code is required")
        if course_code in course_codes:
            raise NotFoundError(status_code=409)
        new_cource=course(course_name=course_name,course_code=course_code,course_description=course_description)
        db.session.add(new_cource)
        db.session.commit()
        return new_cource,201

class StudentAPI(Resource):
    @marshal_with(Student_output_fields)
    def get(self,student_id):
        Student_detail=db.session.query(Student).filter(Student.student_id==student_id).first()
        if Student_detail:
            return Student_detail
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(Student_output_fields)
    def put(self,student_id):
        args=Update_Student_parser.parse_args()
        student_ids = db.session.query(Student.student_id).all()
        student_ids = [id[0] for id in student_ids]
        if student_id not in student_ids:
            raise NotFoundError(status_code=404)
        first_name=args.get("first_name",None)
        last_name=args.get("last_name",None)
        roll_number=args.get("roll_number",None)
        if roll_number is None:
            raise Error(status_code=400,error_code="STUDENT001",error_message="Roll Number required")
        if first_name is None:
            raise Error(status_code=400,error_code="STUDENT002",error_message="First Name is required")
        Student_tobe_update= db.session.query(Student).filter(Student.student_id==student_id).first()
        Student_tobe_update.first_name=first_name
        Student_tobe_update.last_name=last_name
        Student_tobe_update.roll_number=roll_number
        db.session.add(Student_tobe_update)
        db.session.commit()
        return Student_tobe_update


    @marshal_with(Student_output_fields)
    def delete(self,student_id):
        student_ids = db.session.query(Student.student_id).all()
        student_ids = [id[0] for id in student_ids]
        if student_id not in student_ids:
            raise NotFoundError(status_code=404)
        student_tobe_delete= db.session.query(Student).filter(Student.student_id==student_id).first()
        db.session.delete(student_tobe_delete)
        db.session.commit()
        raise NotFoundError(status_code=200)


    @marshal_with(Student_output_fields)
    def post(self):
        args=create_Student_parser.parse_args()
        Roll_nos = db.session.query(Student.roll_number).all()
        Roll_nos = [role[0] for role in Roll_nos]
        first_name=args.get("first_name",None)
        last_name=args.get("last_name",None)
        roll_number=args.get("roll_number",None)
        if roll_number is None:
            raise Error(status_code=400,error_code="STUDENT001",error_message="Roll Number required")
        if first_name is None:
            raise Error(status_code=400,error_code="STUDENT002",error_message="First Name is required")
        if roll_number in Roll_nos:
            raise NotFoundError(status_code=409)
        new_Student=Student(first_name=first_name,last_name=last_name,roll_number=roll_number)
        db.session.add(new_Student)
        db.session.commit()
        return new_Student,201

class EnrollAPI(Resource):

    @marshal_with(enrollment_fields)
    def get(self,student_id):
        student_ids = db.session.query(Student.student_id).all()
        valid_student_ids = [id[0] for id in student_ids]
        if student_id not in valid_student_ids:
            raise Error(status_code=400,error_code="ENROLLMENT002",error_message="Student does not exist.")
        all_enrollments = db.session.query(Enrollments).filter_by(student_id=student_id).all()
        if all_enrollments:
            return all_enrollments
        else:
            raise NotFoundError(status_code=404)

    @marshal_with(enrollment_fields)
    def post(self,student_id):
        student_ids = db.session.query(Student.student_id).all()
        valid_student_ids = [id[0] for id in student_ids]
        if student_id not in valid_student_ids:
            raise Error(status_code=404,error_code="ENROLLMENT002",error_message="Student does not exist.")
        args=create_enroll_parser.parse_args()
        course_id=args.get("course_id",None)
        if course_id is None:
            raise Error(status_code=400,error_code="ENROLLMENT001",error_message="Cource does not exist.")
        course_ids = db.session.query(course.course_id).all()
        course_ids = [id[0] for id in course_ids]
        if int(course_id) not in course_ids:
            raise Error(status_code=400,error_code="ENROLLMENT001",error_message="Cource does not exist.")
        new_enroll=Enrollments(student_id=student_id, course_id=course_id)
        db.session.add(new_enroll)
        db.session.commit()
        all_enrollments = db.session.query(Enrollments).filter_by(student_id=student_id).all()
        return all_enrollments,201
    
    def delete(self,student_id,course_id):
        student_ids = db.session.query(Student.student_id).all()
        valid_student_ids = [id[0] for id in student_ids]
        course_ids = db.session.query(course.course_id).all()
        course_ids = [id[0] for id in course_ids]
        if student_id not in valid_student_ids:
            raise Error(status_code=400,error_code="ENROLLMENT002",error_message="Student does not exist.")
        if int(course_id) not in course_ids:
            raise Error(status_code=400,error_code="ENROLLMENT001",error_message="Cource does not exist.")
        all_enrollments = db.session.query(Enrollments.student_id, Enrollments.course_id).all()
        student_course_tuples = [(enrollment[0], enrollment[1]) for enrollment in all_enrollments]
        if (student_id, course_id) not in student_course_tuples:
            raise NotFoundError(status_code=404)
        enroll_tobe_delete= db.session.query(Enrollments).filter((Enrollments.student_id==student_id )&(Enrollments.course_id==course_id)).first()
        db.session.delete(enroll_tobe_delete)
        db.session.commit()
        raise NotFoundError(status_code=200)






api.add_resource(CourseAPI, "/api/course/<int:course_id>", "/api/course")
api.add_resource(StudentAPI, "/api/student/<int:student_id>", "/api/student")
api.add_resource(EnrollAPI,"/api/student/<int:student_id>/course", "/api/student/<int:student_id>/course/<int:course_id>")



class Student(db.Model):
    __tablename__='student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)

class course(db.Model):
    __tablename__='course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)

class Enrollments(db.Model):
    __tablename__='enrollment'
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    student_id = db.Column(db.Integer, db.ForeignKey(Student.student_id), nullable=True)  
    course_id = db.Column(db.Integer, db.ForeignKey(course.course_id), nullable=True)  

d = {"course_1":"MAD I","course_2":"DBMS","course_3":"PDSA","course_4":"BDM"}

@app.route("/")
def executer():
    students = Student().query.all()
    return render_template("index.html", students=students)

@app.route("/student/create", methods=["GET","POST"])
def creator():
    if request.method=="POST":
        roll = request.form["roll"]
        f_name = request.form["f_name"]
        l_name = request.form["l_name"]
        cour = [d[i] for i in request.form.getlist("courses")]
        
        studata = Student.query.all()
        for i in studata:
            if i.roll_number==roll:
                return render_template("create_exist.html")

        stu = Student(roll_number=roll,first_name=f_name,last_name=l_name)
        db.session.add(stu)

        sid = Student.query.filter_by(roll_number=roll).first().student_id
        for i in cour:
            cid = course.query.filter_by(course_name=i).first().course_id
            en = Enrollments(student_id=sid,course_id=cid)
            db.session.add(en)    
            
        db.session.commit()
        return redirect("/")
        
    return render_template("create.html")

@app.route("/student/<int:student_id>/update", methods=["GET","POST"])
def updater(student_id):
    if request.method == "POST":
        f_name = request.form["f_name"]
        l_name = request.form["l_name"]
        cour = [d[i] for i in request.form.getlist("courses")]

        stu = Student.query.filter_by(student_id=student_id).first()
        stu.first_name = f_name
        stu.last_name = l_name
        db.session.add(stu)

        en = Enrollments.query.filter_by(student_id=student_id)
        for i in en:
            db.session.delete(i)
        for i in cour:
            cid = course.query.filter_by(course_name=i).first().course_id
            enr = Enrollments(student_id=student_id,course_id=cid)
            db.session.add(enr)  
        db.session.commit()
        return redirect("/")
    
    stu = Student.query.filter_by(student_id=student_id).first()
    return render_template("update.html",student=stu)

@app.route("/student/<int:student_id>/delete", methods=["GET","POST"])
def destroyer(student_id):
    stu = Student.query.filter_by(student_id=student_id).first()
    db.session.delete(stu)
    db.session.commit()
    return redirect("/")

@app.route("/student/<int:student_id>", methods=["GET"])
def viewer(student_id):
    stu = Student.query.filter_by(student_id=student_id).first()
    en = Enrollments.query.filter_by(student_id=student_id)
    enroll = []
    for i in en:
        cour = course.query.filter_by(course_id=i.course_id).first()
        enroll.append({"code":cour.course_code,"name":cour.course_name,"desc":cour.course_description})
    return render_template("view.html",student=stu,enroll=enroll)
