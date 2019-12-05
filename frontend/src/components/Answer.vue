<template>
    <div class="container">
        <div class="answer-bord">
            <p class="text-muted">
            <strong>Answered by: {{ answer.author }}</strong>
            </p>
            <p>{{ answer.body }} </p>
            <p><small>{{ answer.created_at }} </small></p>
            <div v-if="isAnswerAuthor">
                    <router-link
                    :to="{ name: 'answer-editor', params: { id: answer.id } }"
                    class="btn btn-sm btn-outline-secondary mr-1"
                    >Edit
                  </router-link>
                <button @click="triggerDeleteAnswer" class="btn btn-sm btn-danger">Delete</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true
        },
        requestUser: {
            type: String,
            required: true
        }
    },
    computed: {
        isAnswerAuthor() {
            return this.answer.author === this.requestUser;
        }
    },
    methods: {
        triggerDeleteAnswer() {
            this.$emit("delete-answer", this.answer)
        }
    },
}
</script>

<style>
    .answer-bord {
        border: 1px solid rgba(0,0,0,0.1);
        padding: 10px;
        margin-bottom: 10px;
    }
</style>