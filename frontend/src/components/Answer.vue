<template>
    <div class="container">
        <div class="answer-bord">
            <p class="text-muted">
            <strong>Answered by: {{ answer.author }}</strong>
            </p>
            <p>{{ answer.body }} </p>
            <p><small>{{ answer.created_at }} </small></p>
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
        }
    }
}
</script>

<style>
    .answer-bord {
        border: 1px solid rgba(0,0,0,0.1);
        padding: 10px;
        margin-bottom: 10px;
    }
</style>