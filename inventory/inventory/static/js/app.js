var api = angular.module('inventory.api', ['ngResource']);

api.factory('BaseItem', [
  '$resource', function($resource) {
    return $resource('/apiv1/baseitems/:id', {
      id: '@id'
    });
  }
]);

api.factory('Post', [
  '$resource', function($resource) {
    return $resource('/api/posts/:id', {
      id: '@id'
    });
  }
]);

api.factory('Photo', [
  '$resource', function($resource) {
    return $resource('/api/photos/:id', {
      id: '@id'
    });
  }
]);


var app = angular.module('inventory', ['ngRoute', 'ui.bootstrap', 'inventory.api']);

app.controller('MainController', [
  '$scope', 'BaseItem', function($scope, BaseItem) {
    return $scope.baseitems= BaseItem.get();
  }
]);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});