'''
写一个后端模板语言渲染引擎
'''


a = '''{
  "isMain": false,
  "list": []
}'''


b = '''
<div class="head">
<button y-if="{{isMain}}">首页</button>
</div>
<ul class="content">
<!-- 卡片区域 -->
<li class="card isMain" y-for="lesson, index in list">
  <div class="card-title">
    	<i y-if="{{lesson.label}}">{{lesson.label.type}}</i>
    	{{lesson.title}}
 		</div>
    班课<span class="bold">-</span>老师：{{lesson.teacher}}
    <div class="lesson-time">{{lesson.time}}<i class="tt"></i></div>
  </li>
</ul>
end
'''