// @Author: PT
// @CreateTime: 2024-06-05
// @Description:图谱管理
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
  timeOut: "3000",
  extendedTimeOut: "1000",
  showEasing: "swing",
  hideEasing: "linear",
  showMethod: "fadeIn",
  hideMethod: "fadeOut"
};

// 弹出修改模态框
function popupModifyToggle() {
  // 获取下拉框的内容
  var select = getComputedStyle(document.querySelector("#selected"), ":before").getPropertyValue('content')
  // 去除两端双引号
  select = select.slice(1, -1)
  // 获取输入框内容
  var search_input = document.getElementById('search_input').value

  // 传给后端的数据
  var data = {
    "select": select,
    "search_input": search_input,
  }

  $.ajax({
    url: "getmodifydata",
    type: "GET",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值 获取预填写的数据
    success: function (response) {
      flag_modify = response.flag_modify
      if (flag_modify == 1) {
        // 根据节点预填信息到小窗口中
        if (select == "证") {
          // 获取相应属性值
          zheng_Id = response.zheng_Id
          zheng_bzm = response.zheng_bzm
          zheng_zl = response.zheng_zl
          zheng_zf = response.zheng_zf
          zheng_byzs = response.zheng_byzs
          zheng_hyzs = response.zheng_hyzs
          // 给对应输入框赋值
          document.getElementById('zheng_Id_input').value = zheng_Id
          document.getElementById('zheng_bzm_input').value = zheng_bzm
          document.getElementById('zheng_zl_input').value = zheng_zl
          document.getElementById('zheng_zf_input').value = zheng_zf
          document.getElementById('zheng_byzs_input').value = zheng_byzs
          document.getElementById('zheng_hyzs_input').value = zheng_hyzs
          // 打开对应模态框
          popup = document.getElementById('popup_modify_zheng');
        }
        else if (select == "证素") {
          // 获取相应属性值
          zs_Id = response.zs_Id
          zs_bzm = response.zs_bzm
          zs_py = response.zs_py
          zs_bw = response.zs_bw
          // 给对应输入框赋值
          document.getElementById('zs_Id_input').value = zs_Id
          document.getElementById('zs_bzm_input').value = zs_bzm
          document.getElementById('zs_py_input').value = zs_py
          document.getElementById('zs_bw_input').value = zs_bw
          // 打开对应模态框
          popup = document.getElementById('popup_modify_zs')
        }
        else if (select == "症状") {
          // 获取相应属性值
          zz_Id = response.zz_Id
          console.log(zz_Id)
          zz_bzm = response.zz_bzm
          console.log(zz_bzm)
          zz_py = response.zz_py
          console.log(zz_py)
          zz_zl = response.zz_zl
          console.log(zz_zl)
          zz_image = response.zz_image
          console.log(zz_image)
          // 给对应输入框赋值
          document.getElementById('zz_Id_input').value = zz_Id
          document.getElementById('zz_bzm_input').value = zz_bzm
          document.getElementById('zz_py_input').value = zz_py
          document.getElementById('zz_zl_input').value = zz_zl
          document.getElementById('zz_image_input').value = zz_image
          // 打开对应模态框
          popup = document.getElementById('popup_modify_zz')
        }
        else if (select == "中药") {
          // 获取相应属性值
          cm_Id = response.cm_Id
          cm_zym = response.cm_zym
          cm_xw = response.cm_xw
          cm_gj = response.cm_gj
          cm_image = response.cm_image
          // 给对应输入框赋值
          document.getElementById('cm_Id_input').value = cm_Id
          document.getElementById('cm_zym_input').value = cm_zym
          document.getElementById('cm_xw_input').value = cm_xw
          document.getElementById('cm_gj_input').value = cm_gj
          document.getElementById('cm_image_input').value = cm_image
          // 打开对应模态框
          popup = document.getElementById('popup_modify_cm')
        }
        else {
          toastr.warning('请重新选择节点种类！')
          return
        }
        popup.classList.toggle('active');
      }
      else return
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

// 弹出增加模态框
function popupAddToggle() {
  // 获取下拉框的内容
  var select = getComputedStyle(document.querySelector("#selected"), ":before").getPropertyValue('content')
  // 去除两端双引号
  select = select.slice(1, -1)

  if (select == "证") {
    popup = document.getElementById('popup_add_zheng');
  }
  else if (select == "证素") {
    popup = document.getElementById('popup_add_zs');
  }
  else if (select == "症状") {
    popup = document.getElementById('popup_add_zz');
  }
  else if (select == "中药") {
    popup = document.getElementById('popup_add_cm');
  }
  else if (select == "代表方") {
    popup = document.getElementById('popup_add_dbf');
  }
  popup.classList.toggle('active');
}

// 节点搜索按钮点击事件
function searchClick() {
  // 获取下拉框的内容
  var select = getComputedStyle(document.querySelector("#selected"), ":before").getPropertyValue('content')
  // 获取输入框内容
  var search = document.getElementById("search_input").value

  // 传给后端的数据
  var data = {
    "flag": 1,
    "select": select,
    "input_content": search,
    "str": ''
  }

  $.ajax({
    url: "getmanage",
    type: "GET",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      manage_result = response.manage_result
      if (manage_result)
        toastr.info('该节点存在！', '系统提醒')
      else
        toastr.info('该节点不存在！', '系统提醒')
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

// 节点修改按钮点击事件
function modifyClick() {
  // 获取下拉框的内容
  var select = getComputedStyle(document.querySelector("#selected"), ":before").getPropertyValue('content')
  select_temp = select.slice(1, -1)
  // 获取输入框内容
  var modify = document.getElementById("search_input").value
  var modify_data = {}
  if (select_temp == "证") {
    var zheng_Id_input = document.getElementById('zheng_Id_input').value
    var zheng_bzm_input = document.getElementById('zheng_bzm_input').value
    var zheng_zl_input = document.getElementById('zheng_zl_input').value
    var zheng_zf_input = document.getElementById('zheng_zf_input').value
    var zheng_byzs_input = document.getElementById('zheng_byzs_input').value
    var zheng_hyzs_input = document.getElementById('zheng_hyzs_input').value
    modify_data = {
      'zheng_Id_input': zheng_Id_input,
      'zheng_bzm_input': zheng_bzm_input,
      'zheng_zl_input': zheng_zl_input,
      'zheng_zf_input': zheng_zf_input,
      'zheng_byzs_input': zheng_byzs_input,
      'zheng_hyzs_input': zheng_hyzs_input
    }
  }
  else if (select_temp == "证素") {
    var zs_Id_input = document.getElementById("zs_Id_input").value
    var zs_bzm_input = document.getElementById("zs_bzm_input").value
    var zs_py_input = document.getElementById("zs_py_input").value
    var zs_bw_input = document.getElementById("zs_bw_input").value
    modify_data = {
      'zs_Id_input': zs_Id_input,
      'zs_bzm_input': zs_bzm_input,
      'zs_py_input': zs_py_input,
      'zs_bw_input': zs_bw_input
    }
  }
  else if (select_temp == "症状") {
    var zz_Id_input = document.getElementById('zz_Id_input').value
    var zz_bzm_input = document.getElementById('zz_bzm_input').value
    var zz_py_input = document.getElementById('zz_py_input').value
    var zz_zl_input = document.getElementById('zz_zl_input').value
    var zz_image_input = document.getElementById('zz_image_input').value
    modify_data = {
      'zz_Id_input': zz_Id_input,
      'zz_bzm_input': zz_bzm_input,
      'zz_py_input': zz_py_input,
      'zz_zl_input': zz_zl_input,
      'zz_image_input': zz_image_input
    }
  }
  else if (select_temp == "中药") {
    var cm_Id_input = document.getElementById('cm_Id_input').value
    var cm_zym_input = document.getElementById('cm_zym_input').value
    var cm_xw_input = document.getElementById('cm_xw_input').value
    var cm_gj_input = document.getElementById('cm_gj_input').value
    var cm_image_input = document.getElementById('cm_image_input').value
    modify_data = {
      'cm_Id_input': cm_Id_input,
      'cm_zym_input': cm_zym_input,
      'cm_xw_input': cm_xw_input,
      'cm_gj_input': cm_gj_input,
      'cm_image_input': cm_image_input
    }
  }

  // 由于传参数过去的时候，字典获取不了，转为字符串就可以了
  // 顺便request获取含%的也会解析有误，这样也避免了这个问题
  var modify_str = JSON.stringify(modify_data)

  // 传给后端的数据
  var data = {
    "flag": 2,
    "select": select,
    "input_content": modify,
    "str": modify_str
  }

  $.ajax({
    url: "getmanage",
    type: "GET",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      manage_result = response.manage_result
      if (manage_result)
        toastr.info('该节点修改成功！', '系统提醒')
      else
        toastr.info('该节点修改失败！', '系统提醒')
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

// 节点删除按钮点击事件
function delClick() {
  // 获取下拉框的内容
  var select = getComputedStyle(document.querySelector("#selected"), ":before").getPropertyValue('content')
  // 获取输入框内容
  var del = document.getElementById("search_input").value

  // 传给后端的数据
  var data = {
    "flag": 3,
    "select": select,
    "input_content": del,
    "str": ''
  }

  $.ajax({
    url: "getmanage",
    type: "GET",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      manage_result = response.manage_result
      if (manage_result)
        toastr.info('该节点删除成功！', '系统提醒')
      else
        toastr.info('该节点删除失败！', '系统提醒')
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

// 增加单个节点按钮点击事件
function addClick() {
  // 获取下拉框的内容
  var select = getComputedStyle(document.querySelector("#selected"), ":before").getPropertyValue('content')
  // 去除两端双引号
  select_temp = select.slice(1, -1)
  var add_data = {}
  // 获取输入框内容
  if (select_temp == "证") {
    var zheng_bzm_add_input = document.getElementById('zheng_bzm_add_input').value
    var zheng_zl_add_input = document.getElementById('zheng_zl_add_input').value
    var zheng_zf_add_input = document.getElementById('zheng_zf_add_input').value
    var zheng_byzs_add_input = document.getElementById('zheng_byzs_add_input').value
    var zheng_hyzs_add_input = document.getElementById('zheng_hyzs_add_input').value
    add_data = {
      'zheng_bzm_add_input': zheng_bzm_add_input,
      'zheng_zl_add_input': zheng_zl_add_input,
      'zheng_zf_add_input': zheng_zf_add_input,
      'zheng_byzs_add_input': zheng_byzs_add_input,
      'zheng_hyzs_add_input': zheng_hyzs_add_input
    }
  }
  else if (select_temp == "证素") {
    var zs_bzm_add_input = document.getElementById("zs_bzm_add_input").value
    var zs_py_add_input = document.getElementById("zs_py_add_input").value
    var zs_bw_add_input = document.getElementById("zs_bw_add_input").value
    add_data = {
      'zs_bzm_add_input': zs_bzm_add_input,
      'zs_py_add_input': zs_py_add_input,
      'zs_bw_add_input': zs_bw_add_input
    }
  }
  else if (select_temp == "症状") {
    var zz_bzm_add_input = document.getElementById('zz_bzm_add_input').value
    var zz_py_add_input = document.getElementById('zz_py_add_input').value
    var zz_zl_add_input = document.getElementById('zz_zl_add_input').value
    var zz_image_add_input = document.getElementById('zz_image_add_input').value
    add_data = {
      'zz_bzm_add_input': zz_bzm_add_input,
      'zz_py_add_input': zz_py_add_input,
      'zz_zl_add_input': zz_zl_add_input,
      'zz_image_add_input': zz_image_add_input
    }
  }
  else if (select_temp == "中药") {
    var cm_zym_add_input = document.getElementById('cm_zym_add_input').value
    var cm_xw_add_input = document.getElementById('cm_xw_add_input').value
    var cm_gj_add_input = document.getElementById('cm_gj_add_input').value
    var cm_image_add_input = document.getElementById('cm_image_add_input').value
    add_data = {
      'cm_zym_add_input': cm_zym_add_input,
      'cm_xw_add_input': cm_xw_add_input,
      'cm_gj_add_input': cm_gj_add_input,
      'cm_image_add_input': cm_image_add_input
    }
  }
  else if (select_temp == "代表方") {
    var dbf_dbf_add_input = document.getElementById('dbf_dbf_add_input').value
    add_data = {
      'dbf_dbf_add_input': dbf_dbf_add_input
    }
  }
  // 转为字符串传给后端
  var add_str = JSON.stringify(add_data)

  // 传给后端的数据
  var data = {
    "flag": 4,
    "select": select,
    "input_content": '',
    "str": add_str,
  }

  $.ajax({
    url: "getmanage",
    type: "GET",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      manage_result = response.manage_result
      if (manage_result)
        toastr.info('该节点添加成功！', '系统提醒')
      else
        toastr.info('该节点已存在，添加失败！', '系统提醒')
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

// 中药表批量添加点击事件
function cmClick() {
  // 传给后端的数据
  var data = {
    "upload_flag": 'cm'
  }

  $.ajax({
    url: "getbtn",
    type: "get",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      upload_result = response.upload_result
      if (upload_result)
        toastr.info('中药表批量添加成功！', '系统提醒')
      else
        toastr.info('批量添加失败！', '系统提醒')
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

// 代表方-中药表批量添加点击事件
function pcmClick() {
  // 传给后端的数据
  var data = {
    "upload_flag": 'pcm'
  }

  $.ajax({
    url: "getbtn",
    type: "get",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      upload_result = response.upload_result
      if (upload_result)
        toastr.info('代表方-中药表批量添加成功！', '系统提醒')
      else
        toastr.info('批量添加失败！', '系统提醒')
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

// 证表批量增加点击事件
function szClick() {
  // 传给后端的数据
  var data = {
    "upload_flag": 'sz'
  }

  $.ajax({
    url: "getbtn",
    type: "get",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      upload_result = response.upload_result
      if (upload_result)
        toastr.info('证表批量添加成功！', '系统提醒')
      else
        toastr.info('批量添加失败！', '系统提醒')
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

// 证-证素表批量增加点击事件
function sz_zsClick() {
  // 传给后端的数据
  var data = {
    "upload_flag": 'sz_zs'
  }

  $.ajax({
    url: "getbtn",
    type: "get",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      upload_result = response.upload_result
      if (upload_result)
        toastr.info('证-证素表批量添加成功！', '系统提醒')
      else
        toastr.info('批量添加失败！', '系统提醒')
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

// 症状表批量添加点击事件
function symptomClick() {
  // 传给后端的数据
  var data = {
    "upload_flag": 'symptom'
  }

  $.ajax({
    url: "getbtn",
    type: "get",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      upload_result = response.upload_result
      if (upload_result)
        toastr.info('症状表批量添加成功！', '系统提醒')
      else
        toastr.info('批量添加失败！', '系统提醒')
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

// 症状别名表批量添加点击事件
function snnClick() {
  // 传给后端的数据
  var data = {
    "upload_flag": 'snn'
  }

  $.ajax({
    url: "getbtn",
    type: "get",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      upload_result = response.upload_result
      if (upload_result)
        toastr.info('症状别名表批量添加成功！', '系统提醒')
      else
        toastr.info('批量添加失败！', '系统提醒')
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

// 证素-症状表批量添加点击事件
function zs_sClick() {
  // 传给后端的数据
  var data = {
    "upload_flag": 'zs_s'
  }

  $.ajax({
    url: "getbtn",
    type: "get",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      upload_result = response.upload_result
      if (upload_result)
        toastr.info('证素-症状表批量添加成功！', '系统提醒')
      else
        toastr.info('批量添加失败！', '系统提醒')
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
