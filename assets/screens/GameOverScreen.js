import React from "react";
import { View, StyleSheet, Text, Button } from "react-native";

const GameOverScreen = ({round, answer, onRestart}) => {
  return (
    <View style={styles.screen}>
      <Text>The Game is Over!</Text>
      <Text>Number of rounds: { round }</Text>
      <Text>Correct Number was: { answer }</Text>
      <Button onPress={onRestart} title="Restart"></Button>
    </View>
  );
};

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});

export default GameOverScreen;
