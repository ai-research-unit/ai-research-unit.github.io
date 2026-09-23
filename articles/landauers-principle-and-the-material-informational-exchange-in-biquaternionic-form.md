# __Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form__

## Introduction

Landauer's principle is the exchange rate between information and thermodynamics: the erasure of one bit of information requires the dissipation of at least

$$
Q_{\min} = k_B T \log 2
$$

of heat into an environment at temperature $T$. It is the bridge between the informational and the material descriptions of a physical process. It is also the reason the two descriptions cannot be kept apart: a memory is a physical system, its logical states are physical states, and the reset of those states has a thermodynamic price.

This article writes the exchange in the biquaternion framework. The two sides of the exchange are the framework's two sectors. The **material sector** $\mathbb{M}_-$ is the anti-Hermitian subspace; it carries energy and momentum, and its four-vector is the natural carrier of heat. The **informational sector** $\mathbb{M}_+$ is the Hermitian subspace; its states are $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$, and it carries the entropy functional of the companion article *Coarse-Graining and the Biquaternion Entropy Functional*,

$$
\mathcal{S}(\tilde{\rho}) = -2\,\mathrm{Sc}\!\left(\tilde{\rho}\log\tilde{\rho}\right) = h(|\mathbf{r}|),
$$

which is a function of the sector's norm form. Erasure is the reset of a state to a fixed pointer value; it is a completely positive trace-preserving map of **rank two** in the algebra, and it lowers $\mathcal{S}$ by exactly $\log 2$ for a full bit. The second law, applied to the memory together with its environment, then forces the environment's entropy upward by the same amount, and the heat that carries that entropy is the material cost. The exchange rate is the temperature $T$, and the price is $k_B T \log 2$ per bit.

The biquaternion content of the article is structural. The two ledgers of the exchange are the norm forms of the two sectors, and the two norm forms are exchanged by the central factor $i$: for every element, $N(i\tilde{Q}) = -N(\tilde{Q})$, so multiplication by $i$ maps the material sector to the informational sector and reverses the sign of the quadratic form. The material ledger and the informational ledger are thus mirror images under the algebra's imaginary unit, and the temperature is the thermodynamic rate at which one is converted into the other. What the framework does **not** supply is the numerical rate itself: $k_B T \log 2$ is a theorem of thermodynamics and statistical mechanics, transcribed here as standard, and the framework's role is to exhibit the two sectors, their entropies, and the exchange of their quadratic forms.

The treatment is classical. The memory is a classical bit: a state diagonal in a pointer basis, with no coherences, and its entropy is the Shannon entropy of its pointer distribution. The erasure map is the classical reset. Nothing quantum is used, and the standard results of quantum thermodynamics — the entropy of a thermal state, the free-energy balance of a quantum channel — are not developed; where they are cited, they are cited as the standard context.

The conventions are those of the companion articles. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$; $i$ is the central scalar imaginary; the sectors are $\mathbb{M}_+$ (Hermitian states) and $\mathbb{M}_-$ (anti-Hermitian energy-momentum); the trace is $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ with $\mathrm{Tr}(e_0) = 2$; the norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$; and the entropy is measured in nats, the thermodynamic entropy being $k_B$ times it.

## Landauer's Principle

### The Statement

Let a memory have two distinguishable logical states, and let it be in thermal contact with an environment at temperature $T$. If the memory is **erased** — reset to a single standard logical state, whatever its prior logical state — then the heat delivered to the environment satisfies

$$
Q \ge k_B T \log 2 .
$$

The bound is tight: it is approached by a quasistatic erasure, and the deficit $Q - k_BT\log2$ is the entropy produced by the irreversibility of the protocol. The statement is the modern form of the observation of Landauer, made quantitative by Bennett, and placed on an axiomatic footing more recently; the references are standard.

### The Standard Derivation

The derivation uses only the second law. Before erasure the memory is maximally ignorant of its bit, so its entropy is $\log 2$ in nats; after erasure the bit is known, so the entropy is zero. The information lost by the memory is

$$
\Delta S_{\rm info} = -\log 2 .
$$

The memory and the environment together form a closed system, whose entropy cannot decrease:

$$
\Delta S_{\rm info} + \Delta S_{\rm env} \ge 0 \qquad\Longrightarrow\qquad \Delta S_{\rm env} \ge \log 2 .
$$

If the environment is a heat bath at temperature $T$ and the process is reversible for the bath itself, then the heat delivered to it is $Q = T\,\Delta S_{\rm th,env}$ with $\Delta S_{\rm th,env} = k_B\,\Delta S_{\rm env}$ in thermodynamic units, so

$$
Q \ge k_B T \log 2 .
$$

The argument isolates the three elements that any model must supply: the initial entropy of the memory, the entropy of the erased state, and a thermal environment whose entropy is tied to the heat it receives. The framework supplies the first two from the algebra; the environment is standard thermodynamics.

### Tightness and the Role of Correlation

Two refinements are worth recording because they structure the later articles. First, the bound is **tight**, and a protocol that erases quasistatically while keeping the memory in equilibrium with the bath attains it; the excess is the entropy produced by a finite-rate protocol. Second, the bound is a statement about the **marginal** memory: if the memory is correlated with another system, the bound is modified by the correlation, and the corrected statement is the subject of the companion article *Maxwell's Demon and the Informational Sector in Biquaternionic Form*. The marginal form above is the case of vanishing correlation.

## The Two Ledgers

### The Informational Ledger

A classical bit in the informational sector is a state diagonal in a pointer basis $\{\tilde{P}_+(\hat{\mathbf{n}}),\tilde{P}_-(\hat{\mathbf{n}})\}$:

$$
\tilde{\rho} = p_+\,\tilde{P}_+(\hat{\mathbf{n}}) + p_-\,\tilde{P}_-(\hat{\mathbf{n}}), \qquad p_\pm \ge 0, \quad p_+ + p_- = 1 .
$$

Its Bloch vector is $\mathbf{r} = (p_+ - p_-)\hat{\mathbf{n}}$, of length $|\mathbf{r}| = |p_+ - p_-| \le 1$, and its entropy functional is

$$
\mathcal{S}(\tilde{\rho}) = -2\,\mathrm{Sc}\!\left(\tilde{\rho}\log\tilde{\rho}\right) = -p_+\log p_+ - p_-\log p_- = h(|p_+ - p_-|).
$$

The state is genuinely **classical**: it is a mixture of two orthogonal idempotents with no coherence between them, so its information content is the Shannon entropy of its pointer distribution and nothing else. The maximally ignorant bit has $p_\pm = \tfrac{1}{2}$, $\mathbf{r} = 0$, and $\mathcal{S} = \log 2$; a definite bit has $|p_+ - p_-| = 1$, $\mathbf{r}$ on the sphere, and $\mathcal{S} = 0$.

### The Material Ledger

The material sector carries energy and momentum. Its four-vector is

$$
\tilde{P} = i\,\frac{E}{c}\,e_0 + \mathbf{p}, \qquad \mathbf{p} = p_1e_1 + p_2e_2 + p_3e_3 ,
$$

an element of $\mathbb{M}_-$: an imaginary scalar component $iE/c$ and a real vector component. The energy is the timelike component, $E = -i\,c\,\mathrm{Sc}(\tilde{P})$, and heat is a change of it. The material ledger of a thermodynamic process is the energy account

$$
\Delta E_{\rm env} = Q ,
$$

with the entropy of a bath at temperature $T$ related to the heat it receives by the Clausius relation

$$
\Delta S_{\rm th,env} = \frac{Q}{T} .
$$

The temperature is the conversion factor between the two ledgers: it converts energy in $\mathbb{M}_-$ into entropy in the informational currency.

### The Sector Exchange

The two sectors' quadratic forms are exchanged by the imaginary unit. Since $i$ is central and the quaternion conjugation fixes it, $\overline{i\tilde{Q}} = i\bar{\tilde{Q}}$, and therefore

$$
N(i\tilde{Q}) = (i\tilde{Q})\,\overline{(i\tilde{Q})}
= (i\tilde{Q})(i\bar{\tilde{Q}})
= i^2\,\tilde{Q}\bar{\tilde{Q}}
= -N(\tilde{Q}) .
$$

That is, multiplication by $i$ maps $\mathbb{M}_-$ to $\mathbb{M}_+$ and reverses the sign of the norm form. The energy-momentum vector of a material body, whose norm form is non-positive, is carried by $i$ to an element of the informational sector whose norm form is non-negative — the same sign convention that makes the state space of $\mathbb{M}_+$ the future cone of $N$. The two ledgers of the exchange are mirror images under the algebra's imaginary unit.

This is a structural statement and it should not be over-read. The factor $i$ exchanges the sectors and their quadratic forms; it does not by itself produce the conversion factor $T$, and it does not produce the value $\log 2$ per bit. Those are thermodynamic facts about the memory and its environment, and the framework expresses them rather than deriving them. What the factor $i$ does supply is the reason the exchange is natural in this algebra: the quantity that carries the entropy and the quantity that carries the heat are the two real forms of the same complexified object.

## Erasure in Biquaternionic Form

### The Erasure Map

**Erasure** is the reset of the memory to one standard pointer state, independent of its prior state. In the sector it is the map

$$
\mathcal{E}_{\hat{\mathbf{n}}} : \tilde{\rho} \longmapsto \tilde{P}_+(\hat{\mathbf{n}})\,\mathrm{Tr}(\tilde{\rho}),
$$

which discards the state entirely and returns the fixed idempotent, scaled by the trace; on the states of the sector, $\mathrm{Tr}(\tilde{\rho}) = 1$ and the image is $\tilde{P}_+(\hat{\mathbf{n}})$ itself. Written with the trace factor the map is linear; on the Bloch ball it acts by

$$
\mathbf{r} \longmapsto \hat{\mathbf{n}},
$$

a constant map, which drives every state to the same point of the sphere.

The reset is **not** the limit of the dephasing flow, and the distinction is worth drawing because the two are easily conflated. Dephasing preserves the axial component $\hat{\mathbf{n}}\cdot\mathbf{r}$ and converges only to the projection $\mathbf{r}\mapsto(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$ onto the pointer diameter, so it never moves a state that points the other way; a state with $\mathbf{r} = -\tfrac{1}{2}\hat{\mathbf{n}}$, for instance, is fixed by full dephasing and is sent to $+\hat{\mathbf{n}}$ by the reset. The reset is instead the $t\to\infty$ limit of a **non-unital** contraction semigroup — the amplitude-damping, or thermalising, semigroup whose stationary state is $\tilde{P}_+(\hat{\mathbf{n}})$ — and it is precisely the non-unitality, absent from dephasing, that lets it move the state off the diameter and change the axial component.

The map is linear, completely positive, trace-preserving and idempotent, but it is **not unital**: it sends the maximally mixed state to a pure state, $\mathcal{E}_{\hat{\mathbf{n}}}(e_0/2) = \tilde{P}_+(\hat{\mathbf{n}}) \neq e_0/2$. It is therefore not a coarse-graining in the sense of the companion article, whose conditional expectations fix the maximally mixed state; it is the composition of the pointer coarse-graining with a reset, and the non-unital character is exactly what allows it to **lower** the entropy of the memory. The deficit is not created or destroyed by the map; it is exported to the environment, where it appears as the heat of the following section.

The map is **rank two**: it has a Kraus representation with two operators. In the pointer basis they are

$$
K_1 = |0\rangle\langle 0|, \qquad K_2 = |0\rangle\langle 1| ,
$$

where $K_1$ is $\tilde{P}_+(\hat{\mathbf{n}})$ itself and $K_2$ is its raising companion, the off-diagonal element that carries the second logical state into the first. They satisfy $\sum_a K_a^\dagger K_a = e_0$ and $\sum_a K_a\,\tilde{\rho}\,K_a^\dagger = \tilde{P}_+(\hat{\mathbf{n}})\,\mathrm{Tr}(\tilde{\rho})$, which is $\tilde{P}_+(\hat{\mathbf{n}})$ on every state. The completeness and the reset property are elementary matrix identities; they were checked explicitly in the $2\times2$ representation, where $\sum_a K_a^\dagger K_a = I$ and the image of an arbitrary state $\tilde{\rho}$ is $\tilde{P}_+$ independent of $\tilde{\rho}$. The minimal Kraus rank of the reset channel is two.

### The Entropy Change

The entropy change of the memory is the difference between the entropies of the image and the state:

$$
\Delta\mathcal{S} = \mathcal{S}\!\left(\tilde{P}_+(\hat{\mathbf{n}})\right) - \mathcal{S}(\tilde{\rho}) = 0 - \mathcal{S}(\tilde{\rho}) = -\mathcal{S}(\tilde{\rho}),
$$

because the erased state is pure, hence a zero divisor, hence of zero entropy. Erasure therefore removes exactly the state's entropy and nothing else. Three cases are worth isolating.

**A full bit.** For the maximally ignorant pointer state, $p_\pm = \tfrac{1}{2}$,

$$
\Delta\mathcal{S} = -\log 2 = -0.6931471806 ,
$$

using $h(0) = \log 2$.

**A biased bit.** For a classical bit with $|\mathbf{r}| = |p_+ - p_-| \ne 0$, the removal is $\Delta\mathcal{S} = -h(|\mathbf{r}|)$, less than a full bit.

**A superposition.** For the interior state $\tilde{\rho} = \tfrac{1}{2}(\tilde{P}_+(e_1) + \tilde{P}_+(e_2))$, with $\mathbf{r} = \tfrac{1}{2}(e_1+e_2)$ and $|\mathbf{r}| = 1/\sqrt{2}$, the functional gives $\mathcal{S} = 0.4164955307$ and erasure to any idempotent gives

$$
\Delta\mathcal{S} = -0.4164955307 .
$$

The entropy removed is the state's own, whether the state is a classical mixture or a superposition; the erasure map does not care which. Note the direction: the entropy **falls**, which is the opposite of the behavior of a coarse-graining in the companion article, where the functional is monotone increasing under the map. The difference is the non-unitality. A unital trace-preserving map cannot lower the entropy of its input; a non-unital one can, and the deficit is exported to whatever the map is coupled to. Erasure is the extreme case, in which the whole entropy of the state is removed and the whole of it must appear elsewhere.

### Erasure Is Irreversible

The erasure map is a contraction with an empty spectrum: its linear part on the Bloch vector is $L = 0$, so in the language of the companion article *The Lyapunov Exponent and Information Loss in the Biquaternion Framework* the state is contracted to a point and no distinction survives. The map is not invertible — infinitely many states share the image $\tilde{P}_+$ — and it is the prototype of an **irreversible** operation. A reversible operation, by contrast, is a rotor conjugation, which preserves the norm form and increases no entropy. Erasure is where the framework's reversible and irreversible classes separate, and it is the operation that carries the entire thermodynamic cost.

## The Material Cost and the Exchange Rate

### The Combined Statement

The memory is not isolated. Its entropy change is compensated by the environment, and the second law for the pair is

$$
\Delta\mathcal{S}_{\rm info} + \Delta\mathcal{S}_{\rm env} \ge 0 ,
$$

both entropies measured in nats. For erasure of a full bit, $\Delta\mathcal{S}_{\rm info} = -\log 2$, so

$$
\Delta\mathcal{S}_{\rm env} \ge \log 2 .
$$

Multiplying by $k_B$ to pass to thermodynamic entropy and using the Clausius relation $\Delta S_{\rm th,env} = Q/T$ gives the heat delivered to the bath,

$$
Q = k_B T\,\Delta\mathcal{S}_{\rm env} \ge k_B T \log 2 ,
$$

which is Landauer's principle. The **exchange rate** is therefore $k_B T$ per nat of erased information, or $k_B T \log 2$ per bit; the heat is the material ledger's entry corresponding to the informational ledger's debit.

For a general state the same argument gives

$$
Q \ge k_B T\,\mathcal{S}(\tilde{\rho}) ,
$$

so the cost is the entropy functional of the erased state, read in units of $k_B T$. The material cost is thus controlled by the norm form that controls the entropy: a state near the null cone is cheap to erase, and the maximally mixed state is the most expensive, at $k_BT\log2$.

### A Worked Model

The standard model makes the exchange explicit. Take a single particle in a box of volume $V$, and let the memory record which half of the box it occupies. Erasure resets the record to one half; the implementation is an isothermal compression of the particle from volume $V$ to volume $V/2$ in contact with a bath at temperature $T$. The work done on the gas is

$$
W = -\int_{V}^{V/2} P\,dV = -k_BT\int_V^{V/2}\frac{dV}{V} = k_BT\log 2 ,
$$

using the ideal-gas equation of state $P = k_BT/V$ for a single particle and the isothermal condition. Since the internal energy of an ideal gas at fixed temperature is unchanged, the work is delivered to the bath as heat,

$$
Q = W = k_BT\log 2 ,
$$

and the entropy of the gas falls by $k_B\log2$ while that of the bath rises by $k_B\log2$. The ledger balances exactly. The integral was checked numerically: $k_BT\log 2 = 0.6931471806$ and the isothermal work is the same.

The exactness is special to the **degenerate** memory, and the qualification matters. The two cells of the box are degenerate, so the free-energy cost of the compression is exactly $\Delta F = k_BT\log 2$. Give the two logical states an energy separation $\epsilon$ and start the memory in maximal ignorance, and the free-energy argument shows that the *work* falls to $k_BT\log 2 - \epsilon/2$ — the second term being the energy the memory releases as it settles into its lower state — while the *heat* delivered to the bath is unchanged at $k_BT\log 2$. If the memory is instead in thermal equilibrium at temperature $T$, its entropy is no longer a full bit, and both quantities fall; the minimum **work** is then the free-energy difference, $k_BT\log(1 + e^{-\beta\epsilon})$, while the **heat** is $k_BT$ times the smaller entropy, $k_BT\left(\log(1 + e^{-\beta\epsilon}) + \beta\epsilon\,e^{-\beta\epsilon}/(1 + e^{-\beta\epsilon})\right)$. The two coincide only in the degenerate limit, where both return $k_BT\log2$ as $\epsilon\to0$. The universal statement, and the one the framework's ledger expresses, is that the cost is $k_BT$ per nat of entropy erased; the number of nats is the memory's own entropy, and a gap reduces it. The ideal-gas compression is used above because it is the degenerate case in which the work and the heat coincide, and it exposes the mechanical work directly.

The model also shows what the framework's sectors are doing. The gas and the bath are material, carrying energy in $\mathbb{M}_-$; the record is informational, carrying its entropy in $\mathbb{M}_+$; and the compression converts the informational debit into a material credit at the rate $T$.

## Reversible and Irreversible Operations

The accounting separates the operations of the framework into two classes, and the separation is the content of the exchange.

| Operation | Algebra | Entropy change | Lyapunov spectrum |
|---|---|---|---|
| Reversible gate (rotor conjugation) | $\tilde{\rho}\mapsto\tilde{R}\tilde{\rho}\tilde{R}^\dagger$, $\tilde{R}\tilde{R}^\dagger=e_0$ | $0$ | $\{0,0,0\}$ |
| Coarse-graining | conditional expectation $\Phi$ | $\ge 0$ | $\le 0$ |
| Erasure | reset to $\tilde{P}_+(\hat{\mathbf{n}})$ | $-\mathcal{S}(\tilde{\rho})$ on the memory, $+\mathcal{S}(\tilde{\rho})$ on the environment | $-\infty$ (linear part $L=0$) |

A **reversible** operation is an isometry: it preserves the norm form, produces no entropy, and has a vanishing Lyapunov spectrum. An **irreversible** operation is a contraction: it destroys distinctions, produces entropy in the combined account, and has non-positive exponents. Erasure is the extreme case of the second class. The thermodynamic cost appears **only** in the second class, and it appears as the compensating environment entropy required by the second law. This is the operational meaning of the material–informational exchange: the informational sector's reversible operations are free, and its irreversible operations are paid for in the material sector.

It is worth stating what is not claimed. The framework does not derive the Landauer bound; the bound follows from the second law and the Clausius relation, both standard. The framework's contribution is the exact expression of the informational debit — the entropy functional of the state, a function of the norm form — and the identification of the material credit with the energy component of a material-sector four-vector. The rate $T$ is thermodynamic input.

## What Is Derived and What Is Imported

**Derived from the algebra.** The representation of a classical bit as a diagonal state $\tilde{\rho} = p_+\tilde{P}_+ + p_-\tilde{P}_-$ and the identification of its entropy with the Shannon entropy of the pointer distribution; the erasure map, its idempotent and non-unital character, and its minimal Kraus rank two, with the completeness and reset identities checked in the $2\times2$ representation; the entropy debit $\Delta\mathcal{S} = -\mathcal{S}(\tilde{\rho})$ and its contrast with the monotonicity of a unital coarse-graining; the value $-\log 2$ for a full bit and the superposition value $-0.4164955307$ for the interior state $\tfrac{1}{2}(\tilde{P}_+(e_1)+\tilde{P}_+(e_2))$; the energy-carrying role of the material sector; and the sector exchange $N(i\tilde{Q}) = -N(\tilde{Q})$.

**Imported from standard thermodynamics.** Landauer's principle and its derivation from the second law; the tightness of the bound and the refinements for correlated memories; the Clausius relation and the ideal-gas isothermal work; and the ideal-gas equation of state. These are copied from the standard literature.

**Not supplied.** The framework does not produce the value $k_BT\log2$, does not select a physical implementation of erasure, and does not derive the temperature of the environment. It predicts no departure from the standard Landauer accounting; it reorganises that accounting into the two sectors of the algebra.

## Summary

The informational and material sectors of the framework are the two ledgers of Landauer's principle. A classical bit is a state $\tilde{\rho} = p_+\tilde{P}_+(\hat{\mathbf{n}}) + p_-\tilde{P}_-(\hat{\mathbf{n}})$ of the informational sector, with entropy $\mathcal{S}(\tilde{\rho}) = h(|p_+ - p_-|)$ equal to the Shannon entropy of its pointer distribution. Energy and heat are carried by the material sector as the four-vector $\tilde{P} = i(E/c)e_0 + \mathbf{p}$.

**Erasure** is the reset $\tilde{\rho}\mapsto\tilde{P}_+(\hat{\mathbf{n}})$, a rank-two completely positive trace-preserving map and the extreme case of the irreversible class. Its entropy debit is

$$
\Delta\mathcal{S} = -\mathcal{S}(\tilde{\rho}) \qquad (\text{a full bit: } -\log 2),
$$

and the second law forces a compensating environment entropy $\Delta\mathcal{S}_{\rm env}\ge\mathcal{S}(\tilde{\rho})$, hence a heat

$$
Q \ge k_B T\,\mathcal{S}(\tilde{\rho}) \qquad (\text{a full bit: } k_BT\log 2).
$$

The exchange rate between the sectors is $k_BT$ per nat. The two ledgers are related by the central factor $i$, which exchanges the sectors and reverses the sign of the norm form, $N(i\tilde{Q}) = -N(\tilde{Q})$.

Reversible operations — rotor conjugations — preserve the norm form, produce no entropy and have a vanishing Lyapunov spectrum; irreversible operations — coarse-grainings, and erasure above all — contract, produce entropy in the combined account, and are paid for in the material sector. This is the material–informational exchange: the reversible part of the informational sector is free, and the irreversible part costs $k_BT$ per nat, at the exchange rate set by the temperature.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) subspaces |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary; exchanges the sectors |
| $\tilde{\rho} = \tfrac{1}{2}(e_0+i\mathbf{r})$ | State of the informational sector |
| $\tilde{P}_\pm(\hat{\mathbf{n}}) = \tfrac{1}{2}(e_0\pm i\hat{\mathbf{n}})$ | Pointer idempotents (logical states) |
| $\tilde{\rho} = p_+\tilde{P}_+ + p_-\tilde{P}_-$ | Classical bit (diagonal state) |
| $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ | Trace, $\mathrm{Tr}(e_0)=2$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form |
| $N(i\tilde{Q}) = -N(\tilde{Q})$ | Sector exchange of the quadratic form |
| $\mathcal{S}(\tilde{\rho}) = -2\,\mathrm{Sc}(\tilde{\rho}\log\tilde{\rho}) = h(|\mathbf{r}|)$ | Entropy functional (nats) |
| $h(x) = -\tfrac{1+x}{2}\log\tfrac{1+x}{2} - \tfrac{1-x}{2}\log\tfrac{1-x}{2}$ | Binary entropy, bias argument: $h(0)=\log 2$, $h(1)=0$ |
| $\mathcal{E}_{\hat{\mathbf{n}}}(\tilde{\rho}) = \tilde{P}_+(\hat{\mathbf{n}})\,\mathrm{Tr}(\tilde{\rho})$ | Erasure map (non-unital reset) |
| $K_1, K_2$ | Kraus operators of erasure, $\sum_a K_a^\dagger K_a = e_0$ |
| $\Delta\mathcal{S} = -\mathcal{S}(\tilde{\rho})$ | Entropy debit of erasure |
| $\tilde{P} = i(E/c)e_0 + \mathbf{p}$ | Material four-momentum (energy-momentum) |
| $E = -i\,c\,\mathrm{Sc}(\tilde{P})$ | Energy (timelike component) |
| $Q$, $T$, $k_B$ | Heat, temperature, Boltzmann constant |
| $\Delta S_{\rm th,env} = Q/T$ | Clausius relation |
| $Q_{\min} = k_BT\log 2$ | Landauer cost of erasing one bit |
| $Q \ge k_BT\,\mathcal{S}(\tilde{\rho})$ | Landauer bound for a general state |

## Further Reading

- R. Landauer, "Irreversibility and heat generation in the computing process," *IBM Journal of Research and Development* **5** (1961) 183–191, for the original statement of the erasure cost.
- C. H. Bennett, "The thermodynamics of computation — a review," *International Journal of Theoretical Physics* **21** (1982) 905–940, for the derivation and the logical-reversibility programme.
- C. H. Bennett, "Notes on the history of reversible computation," *IBM Journal of Research and Development* **32** (1988) 16–23, for the history of the reversible/irreversible distinction.
- D. Reeb and M. M. Wolf, "An improved Landauer principle with finite-size corrections," *New Journal of Physics* **16** (2014) 103011, for the tightness of the bound and its finite-size corrections.
- C. H. Bennett, "Demons, engines and the second law," *Scientific American* **257** (1987) 108–116, for the erasure resolution of the paradox and the physical reading of the bound.
- L. Szilard, "On the decrease of entropy in a thermodynamic system by the intervention of intelligent beings," *Zeitschrift für Physik* **53** (1929) 840–856, for the single-particle model of the exchange.
- H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics* (Wiley, 1985), for the Clausius relation, the ideal-gas isothermal work, and the free-energy balance.
- K. Maruyama, F. Nori, and V. Vedral, "Colloquium: The physics of Maxwell's demon and information," *Reviews of Modern Physics* **81** (2009) 1–23, for the modern synthesis of erasure, measurement and feedback.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Kraus representation and the rank of a completely positive map.
