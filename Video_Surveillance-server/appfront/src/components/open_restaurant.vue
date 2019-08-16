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
          <div class="div_allinline">
            <div class="subdiv_allinline">      
              <P @click="loadopenList">在线ID列表</P>
                <template>
                  <el-table
                    
                    :data="openData.filter(data => !search1 || data.id.toLowerCase().includes(search1.toLowerCase()))"
                    style="width: 100%"
                    height="500px">
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
                          v-model="search1"
                          size="mini"
                          placeholder="输入饭店ID"/>
                      </template>
                    </el-table-column>
                  </el-table>
                </template>
            </div>
            <div class="subdiv_allinline">      
              <P @click="minus">断线ID列表</P>
                <template>
                  <el-table
                    
                    :data="closeData.filter(data => !search2 || data.id.toLowerCase().includes(search2.toLowerCase()))"
                    style="width: 100%"
                    height="500px">
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
                          v-model="search2"
                          size="mini"
                          placeholder="输入饭店ID"/>
                      </template>
                    </el-table-column>
                  </el-table>
                </template>
            </div>
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
        openData: [],
        openflag:0,
        minusflag:0,
        closeData:[],
        openData1:[],
        allData:[],
        search1: '',
        search2: '',
        restaurantname:''
      }
    },
    methods: {
      addRow () {
        console.log("进入add")
      },safe_quit() {
        sessionStorage.clear();
        console.log("lalallallal")
        this.$router.push('/')
      },

      loadList() {  //读取饭店列表，还没写好，结果放到allData中
          let that = this;
          this.$http.get(this.$site + 'api/search_restaurant/')
            .then((response) => {
              var res = JSON.parse(response.bodyText)
              if (res === 'wrong') {
                that.$message({
                  message: '校验失败，请检查后重试',
                  type: 'error'
                });
              } else {
                for(var i=0 ; i< res.length ; i++){
                  this.name = res[i].name.toString()
                  this.id = res[i].id.toString()
                  var list = {
                    id: this.id,
                    name: this.name,
                }
                this.allData.unshift(list)
                }
              }
            }) 
          this.$http.get(this.$site + 'api/search_open_restaurant/')
            .then((response) => {
              var res = JSON.parse(response.bodyText).rows
                for(var i=0 ; i< res.length ; i++){
                  this.id = res[i].id.toString()
                  var list = {
                    id: this.id.toString(),
                  }
                  this.openData1.unshift(list)
                }
              }
            )
      },
      loadopenList() {  //读取开着的饭店列表，还没写好，结果放到openData中,但是由于只有id，需要和allData比较再把饭店名称写入opendata中
          if(this.openflag==0){
          console.log("进在线检测了")
          let that = this;
          for(var i = 0 ;i<this.openData1.length;i++){
            var list = {
              id: this.openData1[i].id.toString(),
            }
            this.openData.unshift(list)
            console.log("open"+this.openData[i].id)
          }
                 for(var i = 0 ;i < this.openData.length ; i++){
                  for(var j=0 ; j<this.allData.length; j++){
                    
                    console.log(this.openData[i].id+"和"+this.allData[j].id)
                    if(this.openData[i].id==this.allData[j].id){
                      console.log("进来的是"+this.openData[i].id)
                      this.openData[i].name=this.allData[j].name;
                      break;
                    }
                  }
                }         
          this.openflag=1 
        }
      },
      minus() { //用来求allData-openData的差集，放到closeData里
        if(this.minusflag==0){
          let that = this;
          var flag = 0
          var open = this.openData1.length;
          var all = this.allData.length;
          for(var i = 0 ;i < all ; i++){
            for(var j = 0 ;j < open ; j++){
              if(this.openData1[j].id==this.allData[i].id){
                flag = 1;
                break;
              }
            }
            if(flag==0){
              console.log(this.allData[i])
              this.closeData.unshift(this.allData[i]);
            }
            flag = 0;
          }
        this.minusflag=1;
        }
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

  .div_allinline{
    text-align:center;
    margin:0 auto;
    padding:0;
    clear:both
  }
 
  .subdiv_allinline{
    margin:0;
    padding:0;
    display:inline-block;
    zoom:1;
    width:500px;  height: 400px; margin-top: 50px;
    margin-right: 50px;
    margin-left: 50px
  }


</style>
