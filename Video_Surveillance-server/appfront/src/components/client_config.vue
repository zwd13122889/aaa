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
            <el-menu-item-group>
              <template slot="title"></template>
              <el-menu-item index="/open_restaurant">Client在线检测</el-menu-item>
              <el-menu-item index="/client_config">Client算法配置</el-menu-item>
            </el-menu-item-group>
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
          
          <el-steps :active="active" finish-status="success" class="step_bar">
            <el-step title="步骤 1" description="选择客户端"></el-step>
            <el-step title="步骤 2" description="显示并修改客户端"></el-step>
          </el-steps>
          <div class="id_test" v-if="active === 0">
            
            <div class="div_allinline">
              <div class="subdiv_allinline">      
                <P>在线ID列表</P>
                  <template>
                    <el-table
                      :data="openData.filter(data => !search || data.id.toLowerCase().includes(search.toLowerCase()))"
                      style="width: 100%"
                      highlight-current-row
                      @current-change="handleCurrentChange"
                      height="500px">
                      <el-table-column
                        label="饭店ID"
                        prop="id"
                        sortable >
                      </el-table-column>
                      <el-table-column
                        label="饭店名称"
                        prop="name"
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
                  <div style=" margin-right: auto;  margin-left: auto;margin-top: 50px;">
                    <P><el-button type="primary"  @click="jiemianxianshi">进入远程界面</el-button></P> 
                  </div>
                  </div>
              </div>
          </div>

          
          <div class="algorithm" v-if="active === 1">
            
            <el-form :inline="true" :model="formInline" v-for="form in formInline" :key="form" class="demo-form-inline">
              <img src='../assets/img/bg.jpg' height="200" width="200" alt='获取失败'>
              <br>  
              <el-form-item :label="form.cam_id">         
              </el-form-item>
              <el-form-item label="帽子">
                <el-checkbox v-model="form.maozi"></el-checkbox>
              </el-form-item>
              <el-form-item label="口罩">
                <el-checkbox v-model="form.kouzhao"></el-checkbox>
              </el-form-item>
              <el-form-item label="老鼠">
                <el-checkbox v-model="form.mouse"></el-checkbox>
              </el-form-item>
              <el-form-item label="抓图">
                <el-checkbox v-model="form.picture"></el-checkbox>
              </el-form-item>
              
            </el-form>
            
            <el-button @click="yuanchengpeizhi">远程配置</el-button>
            <el-button @click="previous" >返回</el-button>
        </div>

          <!--<div style="text-align: center; margin-top: 40px">-->
          <!--<el-button style="margin-top: 12px; align-items: center" @click="next" :disabled="next_flag">下一步</el-button>-->
          <!--</div>-->
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
    name: "client_config",
    data() {
      return {
        person_name: '',
        active: 0,
        res_id: '',  //饭店的id
        res_name: '',  //饭店的名称
        name:'',
        id:'',
        openData: [{
          id: '1001',
          name: '两咖啡、夏宫、1515牛排馆'
        },{
          id: '1005',
          name: 'city super'
        }, {
          id: '1006',
          name: '素凯泰酒店'
        }, {
          id: '1008',
          name: '晶'
        }],
        search: '',
        form1:'1001',
        formInline: [
          {cam_id: '301',  maozi: true,  kouzhao: true, mouse: false,  picture: false},
          {cam_id: '201',  maozi: false,  kouzhao: true, mouse: false,  picture: true},
        ],
        test:'测试'
      }
    },
    methods: {
      next() {  //点击下一步
        if (this.active++ > 2) this.active = 0;
        this.next_flag = !this.next_flag
      },
      safe_quit() {
        sessionStorage.clear();
        console.log("lalallallal")
        this.$router.push('/')
      },
      previous() {
        if (this.active-- < 0) this.active = 0;
    
      },

      yuanchengpeizhi() {
        let that = this;
        config='';
        for(i=0,len=formInline.length;i<len;i++){
          var xconfig='C00000000000000000000000000000000000000000000';
          xconfig='C'+formInline[i].cam_id+xconfig.substring(4,);
          if(formInline[i].maozi ==true){
            xconfig=xconfig.substring(0,4)+'11'+xconfig.substring(7,)
          }
          if(formInline[i].kouzhao ==true){
            xconfig=xconfig.substring(0,14)+'21'+xconfig.substring(17,)
          }
          if(formInline[i].mouse ==true){
            xconfig=xconfig.substring(0,24)+'31'+xconfig.substring(27,)
          }
          if(formInline[i].picture ==true){
            xconfig=xconfig.substring(0,34)+'41'+xconfig.substring(37,)
          }
          config+=xconfig;
        }
        that.$http.get(this.$site + 'api/change_idconfig?res_id=' + that.res_id + '&&config=' + that.config)
            .then((response) => {
              console.log(response);
              if (response['res'] === 'ok') {
                  that.$message({
                  message: '修改成功',
                  type: 'success'
                  })
              }
              else{
                  that.$message({
                  message: '修改失败',
                  type: 'error'
                  })
              }
            })
      },
        
      jiemianxianshi() {
        var that = this;
        console.log(that.formInline)
        //that.formInline = [];
      /*  that.$http.get(this.$site + 'api/search_idconfig_by_restaurant?res_id=' + that.res_id)
            .then((response) => {
              console.log(response);
              formInline = response;
            }); */
        if (this.active++ > 2){
          this.active = 0;
        } 
      },

      mounted() {
        let that = this;
        var person_name = sessionStorage.getItem('person_name');
        console.log("person_name:", person_name)
        if (person_name === null) {
          this.$router.push('/')
        } else {
          this.person_name = person_name
        }
      }
    }
  }
</script>

<style scoped>
  .step_bar {
    margin-left: 100px;
    margin-right: 100px;
    margin-top: 30px;
  }

  .id_test, .setting, .algorithm {
    margin-top: 50px;
    text-align: center;
  }

  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }


</style>
