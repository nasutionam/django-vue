<template>
  <div class="home">

    <div class="container">
      <div class="mt-5"></div>
      <div v-for="question in questions" :key="question.pk" class="bord">
        <p class="mb-0">Posted by:
          <span class="author-name">{{ question.author }}</span>
        </p>
       <p class="cont">{{ question.content }}</p>
        <p>Answers: {{ question.answers_count }} 
          <span class="float-right">
             <router-link :to="{ name: 'question', params: {slug: question.slug } }" class="btn btn-success btn-sm">Detail</router-link>
          </span>
        </p>
      </div>

      <div class="my-4 text-center">
        <p v-show="loadingQuestions">Loading...</p>
        <button v-show="next" @click="getQuestions" class="btn btn-primary">Load More</button>
      </div>  
      
    </div>

  </div>
</template>

<script>
import { apiService } from "../common/api.service";

export default {
  name: "home",
  data() {
    return {
      questions: [],
      next: null,
      loadingQuestions: false
    }
  },
  methods: {
    getQuestions() {
      let endpoint = "/api/questions/";  
      if(this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint)
        .then(data => {
          this.questions.push(...data.results);
          this.loadingQuestions = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }

        })
    }
  },
  created() {
      this.getQuestions();
      document.title = "Discussion";
    }

};
</script>

<style>
  .author-name {
    font-weight: bold;
    color: #28a745;
  }
  .bord {
    border: 1px solid #DDD;
    margin: 10px;
    padding: 10px;
    border-radius: 5px;
  }
  .cont {
    margin-top: 20px;
    color: gray;
  }
</style>