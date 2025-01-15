// @Author: PT
// @CreateTime: 2024-06-05
// @Description:登录注册
// @Version:1.0

// 登录注册表单左右切换
const loginsec = document.querySelector('.login-section')
const loginlink = document.querySelector('.login-link')
const registerlink = document.querySelector('.register-link')
registerlink.addEventListener('click', () => {
  loginsec.classList.add('active')
})
loginlink.addEventListener('click', () => {
  loginsec.classList.remove('active')
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

$("#btn_login").click(function () {
  toastr.success('登录成功！');
})

$("#btn_register").click(function () {
  toastr.success('注册成功！');
})

// 弹出忘记密码模态框
function popupToggle() {
  // 打开对应模态框
  popup = document.getElementById('popup');
  popup.classList.toggle('active');
}

// 重置密码
function resetClick() {
  // 获取输入框内容
  var user_input = document.getElementById('user_input').value
  var email_input = document.getElementById('email_input').value
  var new_pwd_input = document.getElementById('new_pwd_input').value
  var confirm_pwd_input = document.getElementById('confirm_pwd_input').value

  // 传给后端的数据
  var data = {
    "user_input": user_input,
    "email_input": email_input,
    "new_pwd_input": new_pwd_input,
    "confirm_pwd_input": confirm_pwd_input,
  }

  $.ajax({
    url: "getresetdata",
    type: "GET",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      flag_reset = response.flag_reset
      if (flag_reset == 0) {
        toastr.warning('该用户不存在！')
      }
      else if (flag_reset == 1) {
        toastr.success('重置密码成功，请登录！')
      }
      else if (flag_reset == 2) {
        toastr.warning('新密码与旧密码相同，请直接登录！')
      }
      else if (flag_reset == 3) {
        toastr.warning('新密码与确认密码不同，请重新输入！')
      }
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
