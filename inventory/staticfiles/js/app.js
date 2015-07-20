var app = angular.module('inventory', ['ngRoute', 'ui.bootstrap']);

app.controller('MainController', [
  '$scope', '$http', function($scope, $http) {
    $scope.baseitem = [];
    return $http.get('/apiv1/baseitems/?format=json').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.baseitem.push(item);
      });
    });
  }
]);

var my_app = angular.module('inventory').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});