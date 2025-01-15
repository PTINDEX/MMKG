// @Author: PT
// @CreateTime: 2024-06-05
// @Description:用户管理
// @Version:1.0

const body = document.querySelector('body'),
  shell = body.querySelector('nav'),
  toggle = body.querySelector('.toggle');

// 点击toggle元素时触发事件
toggle.addEventListener("click", () => {
  // 切换shell元素的close类
  shell.classList.toggle("close");
})

// 提示框
var toastr;
toastr.options = {
  closeButton: true,
  debug: false,
  progressBar: true,
  positionClass: "toast-top-center",
  onclick: null,
  showDuration: "300",
  hideDuration: "1000",
  timeOut: "1500",
  extendedTimeOut: "1000",
  showEasing: "swing",
  hideEasing: "linear",
  showMethod: "fadeIn",
  hideMethod: "fadeOut"
};

// 修改按钮点击事件
function buttonClick() {
  // 获取输入框内容
  var old_pwd = document.getElementById('old_pwd').value
  var new_pwd = document.getElementById('new_pwd').value
  var data = {
    "flag": 1,
    "old_pwd": old_pwd,
    "new_pwd": new_pwd
  }

  $.ajax({
    url: "getpwd",
    type: "GET",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      flag_to_html = response
      // 弹出相应提示框
      if (flag_to_html == '1')
        toastr.info('修改成功！', '系统提醒');
      else if (flag_to_html == '2')
        toastr.info('新密码等于旧密码，请重输！', '系统提醒')
      else if (flag_to_html == '3')
        toastr.info('旧密码有误，请重输！', '系统提醒')
      else
        toastr.error('网页未响应！')
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
      debugger
      // 状态码
      console.log(XMLHttpRequest.status);
      // 状态
      console.log(XMLHttpRequest.readyState);
      // 错误信息
      console.log(textStatus);
      toastr.error('网页无响应！')
    }
  })
}
