(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["67507db0"],{"051b":function(e,t,n){"use strict";n.r(t);var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("q-page",{attrs:{padding:""}},[n("div",{staticStyle:{width:"500px","max-width":"90vw"}},[n("q-list",e._l(e.allUsers.edges,function(t){return n("q-item",{key:t.id,attrs:{to:"/users/"+t.node.id}},[n("q-item-section",{attrs:{avatar:""}},[n("q-icon",{attrs:{name:"mdi-account",inverted:"",color:"grey-6"}})],1),n("q-item-section",[e._v("\n          "+e._s(t.node.firstName)+" "+e._s(t.node.lastName)+"\n        ")])],1)}),1)],1)])},i=[],s=n("5640"),a=n.n(s),o=n("1b62"),c=n("9530"),u=n.n(c);function l(){var e=a()(["\nquery userQuery {\n  allUsers {\n    edges {\n      node {\n        id\n        firstName\n        lastName\n        username\n      }\n    }\n  }\n}\n"]);return l=function(){return e},e}var f=u()(l()),d={name:"Users",mixins:[o["c"],o["b"]],data:function(){return{title:"Users"}},apollo:{allUsers:{query:f,prefetch:!1}}},b=d,m=n("2877"),p=Object(m["a"])(b,r,i,!1,null,null,null);t["default"]=p.exports},"1b62":function(e,t,n){"use strict";var r=n("534b"),i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("q-toolbar",[n("q-btn",{attrs:{flat:"",dense:"",round:"","aria-label":"Menu"},on:{click:e.toggleLeftDrawer}},[n("q-icon",{attrs:{name:"menu"}})],1),n("q-toolbar-title",[e._v("\n    "+e._s(e.pageTitle)+"\n  ")])],1)},s=[],a=n("3156"),o=n.n(a),c=n("2f62"),u={name:"DefaultToolbar",mixins:[r["a"]],props:[],methods:o()({},Object(c["b"])(["toggleLeftDrawer"]))},l=u,f=n("2877"),d=Object(f["a"])(l,i,s,!1,null,null,null),b=d.exports,m={mounted:function(){this.setPageTitle(this.title),this.onSwitch()},beforeRouteUpdate:function(e,t,n){this.onSwitch(),n()},methods:{onSwitch:function(){this.setToolbar(b)}}},p=n("1f8c"),h=n.n(p);n.d(t,"c",function(){return r["a"]}),n.d(t,"b",function(){return m}),n.d(t,"a",function(){return h.a})},"1f8c":function(e,t){},"534b":function(e,t,n){"use strict";var r=n("3156"),i=n.n(r),s=n("2f62");t["a"]={computed:i()({leftDrawerOpen:{get:function(){return this.$store.getters["leftDrawerOpen"]},set:function(e){this.$store.commit("setLeftDrawerOpen",e)}}},Object(s["c"])(["page","pageTitle","toolbar","editor","edited"])),methods:i()({},Object(s["b"])(["setPage","setPageTitle","setLeftDrawerOpen","setToolbar","setEditor","setEdited"]))}},5640:function(e,t){function n(e,t){return t||(t=e.slice(0)),Object.freeze(Object.defineProperties(e,{raw:{value:Object.freeze(t)}}))}e.exports=n}}]);