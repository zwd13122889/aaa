<template>
  <div>
    <el-container style="height: 100vh; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1','2']" router>
          <el-menu-item index="/restaurant_list">
            <i class="el-icon-setting"></i>
            <span slot="title">ID列表刷新</span>
          </el-menu-item>
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>Client功能</template>
              <el-menu-item index="/open_restaurant">Client在线检测</el-menu-item>
              <el-menu-item index="/client_config">Client算法配置</el-menu-item> 
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-menu"></i>其他设置</template>
            <el-menu-item index="/close_restaurant">关店设置</el-menu-item>
            <el-menu-item index="/cache">缓存设置</el-menu-item>
          </el-submenu>
          <el-menu-item index="/home">算法配置</el-menu-item>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click.native="safe_quit">安全退出</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>{{person_name}}</span>
        </el-header>

        <el-main>
          <div style=" margin-right: auto;  margin-left: auto;width:500px;  height: 400px; margin-top: 50px;">      
              <template>
                <el-table
                  
                  :data="tableData.filter(data => !search || data.id.toLowerCase().includes(search.toLowerCase()))"
                  style="width: 100%"
                  height="600px">
                  <el-table-column
                    label="饭店ID"
                    prop="id"
                    width="150"
                    sortable >
                  </el-table-column>
                  <el-table-column
                    label="饭店名称"
                    prop="name"
                    width="200"
                    sortable >
                  </el-table-column>
                  <el-table-column
                    align="right">
                    <template slot="header" slot-scope="scope">
                      <el-input
                        v-model="search"
                        size="mini"
                        placeholder="输入饭店ID"/>
                    </template>
                  </el-table-column>
                </el-table>
              </template>
          </div>
        </el-main>
    
        <el-footer style="text-align: center; font-size: 10px">
          版权所有 © 上海大学
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name:'',
        id:'',
        person_name: '',
        tableData: [],
        search: ''
      }
    },
    methods: {
      addRow () {
        console.log("进入add")
        var list = {
          id: '测试',
          name: '测试饭店',}
        this.tableData.unshift(list)
      },safe_quit() {
        sessionStorage.clear();
        console.log("lalallallal")
        this.$router.push('/')
      },
      loadList() {  //读取饭店列表
          let that = this;
          this.$http.get(this.$site + 'api/search_restaurant/')
            .then((response) => {
              var res = JSON.parse(response.bodyText)
              console.log("the length of the res is: ", res.length)
              if (res === 'wrong') {
                that.$message({
                  message: '校验失败，请检查后重试',
                  type: 'error'
                });
              } else {
                that.$message({
                  message: '加载成功',
                  type: 'success'
                }); 
                for(var i=0 ; i< res.length ; i++){
                  this.name = res[i].name.toString()
                  this.id = res[i].id.toString()
                  var list = {
                    id: this.id,
                    name: this.name,
                }
                this.tableData.unshift(list)
                }
              }
            }) 
      }
    },
    mounted() {
        
        this.loadList()
        let that = this;
        var person_name = sessionStorage.getItem('person_name');
        console.log("页面刚加载就运行的person_name:", person_name)
        if (person_name === null) {
          this.$router.push('/')
        } else {
          this.person_name = person_name
        }
    },
  }
</script>

<style scoped>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }

  .card {
    text-align: center;
    width: 1500px;
    margin-left: 250px;
    margin-bottom: 30px;
    margin-top: 30px;
  }
  ::-webkit-scrollbar {
  width: 8px;
  height: 8px;
  }

::-webkit-scrollbar-thumb {
background-color: #a1a3a9;
border-radius: 4px;
}

</style>
