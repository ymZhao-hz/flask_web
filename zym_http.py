from flask import Flask, send_from_directory, render_template, request
import os
 
app = Flask(__name__)
@app.route('/')
@app.route('/news') #主页地址,“装饰器”
def news():
    the_news = {
            '计算机学科各课程之间的关系图':'1',
            '计算机课程资料上传下载':'2',

    }
    context = {
        'title':'计算机专业的认识',
        'the_news': the_news,
    }
    return render_template('index.html',context=context) #把index.html文件读进来，再交给浏览器
@app.route('/file') #主页地址,“装饰器”
def index():
    entries = os.listdir('/opt/work/zym/class_home_work/templates/upload')
    return render_template('fileMgr.html', entries=entries)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    path = os.path.join('/opt/work/zym/class_home_work/templates/upload', f.filename)
    f.save(path)
    return render_template('upload.html')


@app.route('/files/<filename>')
def files(filename):
    return send_from_directory('/opt/work/zym/class_home_work/templates/upload', filename, as_attachment=True)


@app.route('/graph') #主页地址,“装饰器”
def graph():
     return render_template('graph.html') #把index.html文件读进来，再交给浏览器

if __name__ == '__main__':
    #app.run(host='0.0.0.0',debug=True,port=8005) #127.0.0.1 回路 自己返回自己
    app.run(host='0.0.0.0', port=8005,threaded=True)