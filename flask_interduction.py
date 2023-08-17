from flask import Flask,render_template
# in this python file we need to create an Application instance
# application instance is nothing but the object of Flask class of flask package

# create a Application Instance
FAI=Flask(__name__)

@FAI.route('/fun1')
def fun1():
    return 'hai this our first flask view function'

@FAI.route('/wish/<name>')
def wish(name):
    return 'hai hello MR/MS {}'.format(name)

@FAI.route('/template')
def template():
    return render_template('first.html',name='Flask',age=23)




# application instance is having the run method inorder to run the server
if __name__=='__main__':
    FAI.run(debug=True)