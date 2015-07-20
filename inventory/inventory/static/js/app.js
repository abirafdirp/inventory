var app = angular.module('inventory', ['ngRoute']);

app.controller('MainController', [
  '$scope', '$http', function($scope, $http) {
    $scope.baseitems = [];
    return $http.get('/apiv1/baseitems/?format=json').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.baseitems.push(item);
      });
    });
  }
]);
