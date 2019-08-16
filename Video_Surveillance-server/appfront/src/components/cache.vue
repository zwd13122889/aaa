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
          <el-form type='text' style="width:600px;" :model="indexForm"  label-width="100px" class="demo-ruleForm">
          <el-form-item label="暂存目录" prop="index">
              <el-input   v-model="indexForm.index" autocomplete="off"></el-input>
              
          </el-form-item>

          <el-form-item label="缓存容量" prop="volume">
            <div>
              <el-input  type='number' style="width:100px;" v-model="indexForm.volume" autocomplete="off"></el-input>
              G,超过该门限历史数据将会被覆盖</div>
          </el-form-item>
          <br>
          <el-form-item>
            <el-button  @click="xiugaimulu">修改目录</el-button>
            <el-button @click="xiugairongliang">修改容量</el-button>
          </el-form-item>
          </el-form>
          


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
    name: "cache",
    data() {
      return {
        indexForm: {
          index: '',
          volume: '',
        },
      }
    },
    methods: {
      liulanwenjianjia(){

      },
      xiugaimulu(){
        let that = this;
        that.$http.get(this.$site + 'api/change_cache?index=' + that.indexForm.index + "&&volume=" + that.indexForm.volume )
          .then((response) => {
                console.log(response);
                if (response.body['res'] === 'ok') {
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
              });
      }
    },
    xiugairongliang(){
        let that = this;
        that.$http.get(this.$site + 'api/change_cache?index=' + that.indexForm.index + "&&volume=" + that.indexForm.volume )
          .then((response) => {
                console.log(response);
                if (response.body['res'] === 'ok') {
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
              });
      },
      fanhui(){
        let that = this;
        that.$router.push({
                name: "restaurant_list"
        }) 
      }
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
</style>
