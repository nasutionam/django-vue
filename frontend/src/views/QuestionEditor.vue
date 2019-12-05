<template>
    <div class="container">
        <div class="mt-5"></div>
        <h2>Ask a Question</h2>
        <form @submit.prevent="onSubmit">
            <textarea v-model="question_body" class="form-control" placeholder="What you want to ask?" rows="3"></textarea>
            <button type="submit" class="btn btn-success mt-2">Publish</button>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
    name: "QuestionEditor",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            question_body: null,
            error: null
        }
    },
    methods: {
        onSubmit() {
            if(!this.question_body) {
                this.error = "You cannot send an empty question!";
            } else if (this.question_body.length > 240) {
                this.error = "Ensure this field no more than 240 chareacters";
            } else if (this.question_body.trim().length === 0) {
                this.error = "Oops just a space?";
                this.question_body = "";
            } else {
                let endpoint = "/api/questions/";
                let method = "POST";

                if (this.slug !== undefined){
                    endpoint += `${this.slug}/`;
                    method = "PUT"
                }
                apiService(endpoint, method, { content: this.question_body })
                    .then(question_data => {
                        this.$router.push({ name: 'question', params: {slug: question_data.slug } })
                    })
            }
        }
    },
    async beforeRouteEnter (to, from, next) {
        if(to.params.slug !== undefined){
            let endpoint = `/api/questions/${to.params.slug}/`;
            let data = await apiService(endpoint);
            return next(vm => (vm.question_body = data.content))
        } else {
            return next();
        }
    },
    created() {
        document.title = "Editor - Discussion";
    }
}
</script>


<style>
    
</style>