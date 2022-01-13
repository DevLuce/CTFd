<template>
  <div class="border-bottom">
    <div>
      <button
        type="button"
        class="close float-right"
        aria-label="Close"
        @click="deleteField()"
      >
        <span aria-hidden="true">&times;</span>
      </button>
    </div>

    <div class="row">
      <div class="col-md-3">
        <div class="form-group">
          <!-- <label>Field Type</label> -->
          <label>필드 타입</label>
          <select
            class="form-control custom-select"
            v-model.lazy="field.field_type"
          >
            <!-- <option value="text">Text Field</option> -->
            <option value="text">텍스트</option>
            <!-- <option value="boolean">Checkbox</option> -->
            <option value="boolean">체크박스</option>
          </select>
          <!-- <small class="form-text text-muted"
            >Type of field shown to the user</small
          > -->
          <small class="form-text text-muted"
            >유저가 입력하는 필드 타입</small
          >
        </div>
      </div>
      <div class="col-md-9">
        <div class="form-group">
          <!-- <label>Field Name</label> -->
          <label>필드 이름</label>
          <input type="text" class="form-control" v-model.lazy="field.name" />
          <!-- <small class="form-text text-muted">Field name</small> -->
          <small class="form-text text-muted">필드 이름</small>
        </div>
      </div>

      <div class="col-md-12">
        <div class="form-group">
          <!-- <label>Field Description</label> -->
          <label>필드 설명</label>
          <input
            type="text"
            class="form-control"
            v-model.lazy="field.description"
          />
          <!-- <small id="emailHelp" class="form-text text-muted"
            >Field Description</small
          > -->
          <small id="emailHelp" class="form-text text-muted"
            >필드 설명</small
          >
        </div>
      </div>

      <div class="col-md-12">
        <div class="form-check">
          <label class="form-check-label">
            <input
              class="form-check-input"
              type="checkbox"
              v-model.lazy="field.editable"
            />
            <!-- Editable by user in profile -->
            유저 프로필에서 수정 가능하도록 설정
          </label>
        </div>
        <div class="form-check">
          <label class="form-check-label">
            <input
              class="form-check-input"
              type="checkbox"
              v-model.lazy="field.required"
            />
            <!-- Required on registration -->
            회원가입시에 반드시 기입 요청 설정
          </label>
        </div>
        <div class="form-check">
          <label class="form-check-label">
            <input
              class="form-check-input"
              type="checkbox"
              v-model.lazy="field.public"
            />
            <!-- Shown on public profile -->
            공개 프로필에서 보여지도록 설정
          </label>
        </div>
      </div>
    </div>

    <div class="row pb-3">
      <div class="col-md-12">
        <div class="d-block">
          <button
            class="btn btn-sm btn-success btn-outlined float-right"
            type="button"
            @click="saveField()"
          >
            <!-- Save -->
            저장
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CTFd from "core/CTFd";
import { ezToast } from "core/ezq";

export default {
  props: {
    index: Number,
    initialField: Object
  },
  data: function() {
    return {
      field: this.initialField
    };
  },
  methods: {
    persistedField: function() {
      // We're using Math.random() for unique IDs so new items have IDs < 1
      // Real items will have an ID > 1
      return this.field.id >= 1;
    },
    saveField: function() {
      let body = this.field;
      if (this.persistedField()) {
        CTFd.fetch(`/api/v1/configs/fields/${this.field.id}`, {
          method: "PATCH",
          credentials: "same-origin",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
          },
          body: JSON.stringify(body)
        })
          .then(response => {
            return response.json();
          })
          .then(response => {
            if (response.success === true) {
              this.field = response.data;
              ezToast({
                title: "Success",
                // body: "Field has been updated!",
                body: "필드가 업데이트 되었습니다!",
                delay: 1000
              });
            }
          });
      } else {
        CTFd.fetch(`/api/v1/configs/fields`, {
          method: "POST",
          credentials: "same-origin",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
          },
          body: JSON.stringify(body)
        })
          .then(response => {
            return response.json();
          })
          .then(response => {
            if (response.success === true) {
              this.field = response.data;
              ezToast({
                title: "Success",
                // body: "Field has been created!",
                body: "필드가 생성되었습니다!",
                delay: 1000
              });
            }
          });
      }
    },
    deleteField: function() {
      // if (confirm("Are you sure you'd like to delete this field?")) {
      if (confirm("이 필드를 정말 삭제하시겠습니까?")) {
        if (this.persistedField()) {
          CTFd.fetch(`/api/v1/configs/fields/${this.field.id}`, {
            method: "DELETE",
            credentials: "same-origin",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json"
            }
          })
            .then(response => {
              return response.json();
            })
            .then(response => {
              if (response.success === true) {
                this.$emit("remove-field", this.index);
              }
            });
        } else {
          this.$emit("remove-field", this.index);
        }
      }
    }
  }
};
</script>

<style scoped></style>
