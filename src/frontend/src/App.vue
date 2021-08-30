<template>
  <div class="page-loader" v-if="!isLoaded">
    <div style="background-color: #8cc271" class="cube first"></div>
    <div style="background-color: #69beeb" class="cube"></div>
    <div style="background-color: #f5aa39" class="cube"></div>
    <div style="background-color: #e9643b" class="cube last"></div>
  </div>
  <div id="head">
      <p style="cursor: pointer;">Nhận diện Covid-19 qua tiếng ho <a target="_blank" style="color: #004fcf;" href="https://github.com/dee-ex/aicovidvn115m">[Github]</a></p>
      <img id="logohcmut" src="./assets/hcmut.png">
      <img id="logouit" src="./assets/uit.png">
  </div>

  <div id="up">
      <button id="button" onclick="document.getElementById('inputfile').click()">CHỌN FILE</button>
      <input type='file' id="inputfile" style="display:none" @change="onFileChange">
      <button id="process" @click="onProcess">DỰ ĐOÁN</button>
  </div>

  <div id="down">
      <div id="left">
        <audio controls v-if="url" :key="url">
          <source :src="url" alt="file đầu vào" type="audio/wav">
        </audio>
      </div>
      <div id="right">
        <h2 style="color: white">
          Xác suất dương tính là:
          <span v-if="res" v-bind:class="{low: low, mid: mid, high: high}">{{ res }}</span>
        </h2>
      </div>
  </div>
  <footer><p>© Nguyễn Thành Trung (trung.nguyendx@hcmut.edu.vn)</p></footer>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      isLoaded: false,
      file: null,
      url: null,
      res: null,
      fd: null,
      low: null,
      mid: null,
      high: null,
    }
  },
  mounted() {
    document.onreadystatechange = () => {
      if (document.readyState == "complete") {
        this.isLoaded = true;
      }
    }
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0];
      console.log(this.file);
      this.url = URL.createObjectURL(this.file);
    },
    onProcess() {
      this.isLoaded = false;

      this.fd = new FormData();

      this.fd.append("audio", this.file);

      fetch("http://localhost:8000/api/predict/", {method: "POST", body: this.fd})
      .then(response => response.json())
      .then(data => {
        this.res = data["prob"]
        if (.2 - this.res >= 1e-9) {
          this.low = true;
          this.mid = false;
          this.high = false
        } else if (.7 - this.res >= 1e-9) {
          this.low = false;
          this.mid = true;
          this.high = false;
        } else {
          this.low = false;
          this.mid = false;
          this.high = true;
        }
        this.isLoaded = true;
      });
    },
  },
}
</script>

<style>

@keyframes left {
  40% {
    transform: translateX(-60px);
  }

  50% {
    transform: translateX(0);
  }
}

@keyframes right {
  40% {
    transform: translateX(60px);
  }

  50% {
    transform: translateX(0);
  }
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding-left: 10%;
  padding-right: 10%;
}

div {
  border-radius: 12px;
}

.page-loader {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(3, 3, 3, .3);
  z-index: 999;
}

.cube {
  width: 40px;
  height: 40px;
  margin-right: 10px;
}

.first {
  animation: left 1s infinite;
}

.last {
  animation: right 1s infinite .5s;
}

#head {
    padding: 10px;
    text-align: center;
    background-color: #eea35e;
    font-size: 30px;
    font-weight: bold;
    color: white;
    margin: 1%;
}

#up {
    padding: 10px 10px;
    margin: 1%;
    padding-left: 39%;
}

#logohcmut {
    width: 10%;
    height: 10%;
    cursor: pointer;
}

.logouit {
    width: 3%;
    height: 3%;
    cursor: pointer;
}

#button {
    display: block;
    background-color: white;
    border: 2px solid #074B80;
    color: black;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 12px;
    margin-right: 10px;
}

#process {
    display: block;
    background-color: white;
    border: 2px solid #4CAF50;
    color: black;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 12px;
}

#button:hover {
    background-color: #074B80;
    color: white;
    cursor: pointer;
}

#process:hover {
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
}

#left {
    float: left;
    background: gray;
    width: 48%;
    height: 200px;
    margin: 1%;
    display: flex;
    align-items: center;
    justify-content: center;
}

#right {
    float: right;
    background: gray;
    width: 48%;
    height: 200px;
    margin: 1%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.low {
    color: #00ff37;
    display: block;
    margin: 10px 10px;
}

.mid {
    color: #fffb00;
    display: block;
    margin: 10px 10px;
}

.high {
    color: #ff0000;
    display: block;
    margin: 10px 10px;
}

footer {
    margin: 1%;
    text-align: center;
    color: #074B80;
    font-size: 20px;
    margin-top: 18%;
}
</style>
