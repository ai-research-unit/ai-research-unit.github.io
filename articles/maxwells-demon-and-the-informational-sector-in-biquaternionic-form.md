# __Maxwell's Demon and the Informational Sector in Biquaternionic Form__

## Introduction

Maxwell's demon is a being who watches the molecules of a gas, sorts the fast ones from the slow, and thereby makes a hot region out of a cold one without doing work. The paradox is that the demon seems to convert information into work, and to defeat the second law. The resolution, completed by Landauer and Bennett, is that the demon must keep a record, and that erasing the record costs at least as much work as the sorting can deliver. The cycle closes with nothing gained.

This article works the demon's cycle through the biquaternion framework. The demon's device uses both of the framework's sectors, and the accounting between them is the whole content of the paradox. The **gas** is a material system: its energy is carried by the material sector $\mathbb{M}_-$ as the timelike component of a four-vector. The **record** is an informational state: it is an element of the sector $\mathbb{M}_+$, a classical bit in a pointer basis, and its information content is the entropy functional of the companion article *Coarse-Graining and the Biquaternion Entropy Functional*, a function of the sector's norm form. The demon's three operations are then the framework's three operations: a **correlation** step, which creates the mutual information between gas and record at no cost to the total entropy and belongs to the algebra's reversible class; a **feedback** step, also reversible, which converts the correlation into work; and an **erasure** step, which is the non-unital channel of the companion article *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form* and is the only irreversible operation of the three.

The accounting is exact in the ideal case and losing in every other. If the record is a perfect record of the gas, the extractable work is $k_BT\log2$ and the erasure cost is $k_BT\log2$, so the net work of the cycle is zero: the demon breaks even and no more. If the record is imperfect, with error probability $e$, the extractable work is bounded by $k_BT\,I$ with the mutual information $I = \log 2 - H_2(e)$, while the erasure still costs the full $k_BT\log2$ of the record; the cycle then **loses** at least $k_BT\,H_2(e)$ per run. The demon's failure is quantitative and monotone in its noise. The general statement is

$$
W_{\rm net} \;\le\; k_BT\left(I - H(D)\right) \;\le\; 0 ,
$$

where $H(D)$ is the entropy of the demon's memory and $I$ is its mutual information with the gas; since $I \le H(D)$, the bracket is never positive.

The framework's contribution is the localisation of each step. The correlation and feedback steps belong to the algebra's **reversible class**: a permutation of the joint classical states in the first case, an entropy-neutral quasistatic process in the second, whose single-sector representative is the rotor conjugation that preserves the norm form and has a vanishing Lyapunov spectrum. The erasure step is a non-unital contraction, which lowers the memory's entropy and exports the difference to the material sector as heat. The second law is restored at the erasure, and it is the framework's reversible/irreversible dichotomy that says where to look. One further framework object, the **idempotent projection** of the companion article *Decoherence as Idempotent Projection*, appears when the record is required to be definite; whether the irreversibility is charged to that projection or to the erasure is a bookkeeping choice, and the two accounts agree that the cycle gains nothing.

The treatment is classical. The gas is a classical one-particle gas, the record is a classical bit, and the mutual information is Shannon's. The demon does not need entanglement, and none is used; the quantum demon, whose memory is entangled with the gas, belongs to the informational subcategory of the sibling quantum category, and is cited there rather than developed here.

The conventions are those of the companion articles. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$; $i$ is the central scalar imaginary; the sectors are $\mathbb{M}_+$ (Hermitian, informational) and $\mathbb{M}_-$ (anti-Hermitian, material); the trace is $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ with $\mathrm{Tr}(e_0) = 2$; the norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$; a state is $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ with $|\mathbf{r}|\le1$; and entropies are measured in nats.

## The Demon's Cycle in Two Sectors

### The Device

The standard realisation is Szilard's engine. A single particle is confined to a box of volume $V$ in contact with a heat bath at temperature $T$, and a removable partition divides the box into two halves. The demon's cycle has four steps.

1. **Measurement.** The demon determines which half contains the particle and records the answer.
2. **Feedback.** A piston is placed on the empty half and the particle is allowed to expand isothermally against it from volume $V/2$ to volume $V$.
3. **Restoration.** The partition and the piston are returned to their initial positions, with the particle again somewhere in the box and the gas in its initial macrostate.
4. **Erasure.** The record is reset to a standard value, ready for the next cycle.

Steps 1 and 2 create the work; steps 3 and 4 return the device to its initial state, so that the whole cycle is closed and the second law can be applied to it.

### The Two Sectors

The gas is a material system. Its energy, and the heat it exchanges with the bath, are carried by the material sector: the four-momentum

$$
\tilde{P} = i\,\frac{E}{c}\,e_0 + \mathbf{p} \in \mathbb{M}_- ,
$$

whose timelike component is the energy. The heat $Q$ delivered to the bath is a change of that component, and the bath's entropy change is $Q/T$ by the Clausius relation.

The record is an informational state. It is a classical bit in a pointer basis,

$$
\tilde{\rho}_D = p_+\,\tilde{P}_+(\hat{\mathbf{n}}) + p_-\,\tilde{P}_-(\hat{\mathbf{n}}) \in \mathbb{M}_+ ,
\qquad \tilde{P}_\pm(\hat{\mathbf{n}}) = \tfrac{1}{2}\left(e_0 \pm i\hat{\mathbf{n}}\right),
$$

with entropy $\mathcal{S}(\tilde{\rho}_D) = h(|p_+ - p_-|)$ equal to the Shannon entropy of the pointer distribution. The record is diagonal in the pointer basis, so it is genuinely classical and carries no coherence.

The demon's cycle is thus a closed loop through both sectors: work is drawn from the material sector in the feedback step, and the informational sector is debited in the erasure step. The exchange rate between the two ledgers is the temperature, as in the companion article *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*.

## Measurement, Correlation and the Idempotent Projection

### The Correlating Step

The demon's measurement must leave a record correlated with the gas. In the reversible account — the standard one for thermodynamic bookkeeping — the correlation is created by an interaction that copies the relevant bit of the gas onto a memory prepared in a standard state. For a classical bit this is a controlled copy, and it is reversible: the joint transformation is a permutation of the joint states, so it leaves the joint entropy unchanged while redistributing entropy within it — the record's marginal entropy rises from zero to $\log2$, and the mutual information rises by exactly the same amount. The framework's reversible class is the algebraic representative of such a step. Conjugation by a matrix-unitary rotor,

$$
\tilde{\rho} \longmapsto \tilde{R}\,\tilde{\rho}\,\tilde{R}^\dagger , \qquad \tilde{R}\tilde{R}^\dagger = e_0 ,
$$

preserves the norm form, produces no entropy, and has a vanishing Lyapunov spectrum; a permutation of a classical joint distribution shares those three properties, and it is in that sense that the correlating step belongs to the same class. The interaction costs no work and no entropy; what it does is create **mutual information** between the gas and the record.

Take the gas bit $G$ uniformly distributed over its two values and the memory initialised to a standard value. After the copy the joint distribution is perfectly correlated, and the mutual information is

$$
I(G\!:\!D) = H(G) + H(D) - H(G,D) = \log 2 .
$$

The gas's marginal is uniform, as it was before the copy, and the record's marginal is now uniform as well; the joint entropy is unchanged at $\log2$, and the measurement has created one nat of mutual information. The record's marginal entropy has risen by one nat, and that rise is exactly the correlation. This is the demon's entire informational resource, and it is obtained reversibly.

### The Record as a State of the Informational Sector

It is useful to write the record's numbers in the algebra. Averaged over the measurement outcomes, the record is the maximally mixed state of the sector, because the gas bit is unbiased:

$$
\tilde{\rho}_D = \tfrac{1}{2}\tilde{P}_+(\hat{\mathbf{n}}) + \tfrac{1}{2}\tilde{P}_-(\hat{\mathbf{n}}) = \tfrac{1}{2}e_0,
\qquad
N(\tilde{\rho}_D) = \tfrac{1}{4}e_0,
\qquad
\mathcal{S}(\tilde{\rho}_D) = \log 2 .
$$

The norm form is at its maximum and the entropy functional at its maximum, exactly as in the companion article: the more mixed the record, the larger its norm form and the more expensive its erasure. For a biased gas bit with weights $p_\pm$, the record's Bloch vector is $\mathbf{r}_D = (p_+ - p_-)\hat{\mathbf{n}}$, its norm form is $\tfrac{1}{4}(1-|\mathbf{r}_D|^2)e_0$, and its entropy is

$$
\mathcal{S}(\tilde{\rho}_D) = h\!\left(\sqrt{1 - 4\,\mathrm{Sc}\,N(\tilde{\rho}_D)}\right) = h\!\left(|p_+ - p_-|\right) \le \log 2 ,
$$

so a biased record is cheaper to erase than a uniform one. Conditioned on a single outcome, on the other hand, the record is **pure**: $\tilde{\rho}_D = \tilde{P}_\pm(\hat{\mathbf{n}})$, an element of the null cone, with $N(\tilde{\rho}_D) = 0$ and $\mathcal{S}(\tilde{\rho}_D) = 0$. The record is pure when the demon conditions on its knowledge and mixed when the demon averages over it, and the erasure cost is set by the mixture — a distinction that the norm form makes visible, since it is maximal on the mixed record and vanishes on the conditioned one.

### The Definite Record and the Idempotent Projection

A demon that acts must have a **definite** record: it must know the bit, not be in a superposition of knowing and not knowing. If the record is represented by an element that carries coherence between the two pointer values, the coherence is unobservable to the demon's classical logic and must be removed. The removal is the **idempotent projection** onto the pointer basis:

$$
\Phi_{\hat{\mathbf{n}}}(\tilde{\rho}_D) = \tilde{P}_+(\hat{\mathbf{n}})\,\tilde{\rho}_D\,\tilde{P}_+(\hat{\mathbf{n}}) + \tilde{P}_-(\hat{\mathbf{n}})\,\tilde{\rho}_D\,\tilde{P}_-(\hat{\mathbf{n}}),
$$

the fully dephasing conditional expectation of the companion article *Coarse-Graining and the Biquaternion Entropy Functional*, which is idempotent and unital and does not decrease the entropy. The projection is itself irreversible: it is a coarse-graining, and it maps a continuum of records to the classical diameter.

There are therefore two irreversible steps available in the cycle — the registration of the record and the erasure of the record — and the second law requires the account to be balanced by at least one of them. The standard thermodynamic accounting charges only the **erasure**, because the correlating interaction can be arranged so that the record is already classical and the projection is trivial; the decoherence accounting charges the **projection**, because registration is irreversible; and the two agree that the cycle wins nothing. The framework contains both objects and does not privilege one account. The article follows the standard accounting below and records the alternative where it bears.

## Extractable Work

### The Szilard Bound and Its Saturation

The feedback step converts the correlation into work. For the Szilard engine in step 2, the particle occupies one half of the box with certainty once the record is definite, and the isothermal expansion from $V/2$ to $V$ against the piston does

$$
W_{\rm ext} = \int_{V/2}^{V} P\,dV = k_BT\int_{V/2}^{V}\frac{dV}{V} = k_BT\log 2 = 0.6931471806\,k_BT
$$

of work on the piston, using the ideal-gas relation $P = k_BT/V$ for one particle. The numerical value is that of $\log 2$ in units of $k_BT$. The gas returns to its initial macrostate at the end, so its entropy change over the cycle is zero and its internal energy is unchanged; the work comes from the bath's heat, absorbed during the expansion.

The entropy balance of the step is exact. During the isothermal expansion the entropy of the one-particle gas rises by

$$
\Delta S_{\rm gas} = k_B\log\frac{V}{V/2} = k_B\log 2 ,
$$

and the heat absorbed from the bath is $Q = T\,\Delta S_{\rm gas} = k_BT\log2$, so the bath's entropy falls by $k_B\log2$ and the total of gas and bath is unchanged. The work delivered to the piston is exactly the heat absorbed, $W_{\rm ext} = Q$, because the internal energy of an ideal gas is unchanged at fixed temperature. Nothing in this step is irreversible, and the bound is saturated.

### The General Bound

For an imperfect record the extractable work is less. The standard result for measurement-feedback processes — the Sagawa–Ueda bound — is

$$
W_{\rm ext} \;\le\; -\Delta F_{\rm gas} + k_BT\,I ,
$$

where $I$ is the mutual information established by the measurement and $\Delta F_{\rm gas}$ the change of the free energy of the gas. For the isothermal expansion the internal energy of the ideal gas is unchanged, so $-\Delta F_{\rm gas} = k_BT\,\Delta S_{\rm gas}$, and in that case the bound may equally be written $W_{\rm ext} \le k_BT(I + \Delta S_{\rm gas})$. For the cyclic engine the gas returns to its initial macrostate, so $\Delta F_{\rm gas} = 0$ and

$$
W_{\rm ext} \;\le\; k_BT\,I .
$$

The bound is saturated by a quasistatic feedback that uses all the correlation. For a record with error probability $e$ — the demon's bit agrees with the gas with probability $1-e$ — the mutual information is

$$
I = \log 2 - H_2(e), \qquad H_2(e) = -e\log e - (1-e)\log(1-e),
$$

which is verified numerically: $I(0) = \log 2 = 0.6931472$, $I(0.1) = 0.3680642$, $I(0.5) = 0$. A perfect demon extracts $k_BT\log2$; a maximally noisy demon extracts nothing.

### The Gas as a Coarse-Grained Description

The measurement does not change the gas, and it is worth saying so, because the phrase "the demon lowers the entropy of the gas" invites the opposite reading. Before the measurement the gas's position bit is uniformly distributed and its entropy is $\log 2$; after the measurement the marginal distribution of the bit is still uniform, and so its marginal entropy is still $\log 2$. What the measurement changes is the **conditional** entropy: for a record of error $e$,

$$
H(G\mid D) = H_2(e), \qquad H(G) = \log 2, \qquad
I = H(G) - H(G\mid D) = \log 2 - H_2(e) .
$$

The demon's advantage is entirely in the conditional description. The unconditional state of the gas is untouched, no work has yet been extracted, and the sorting has not by itself lowered any thermodynamic entropy.

This is the framework's coarse-graining structure read on the gas. The gas bit is a two-cell classical description; its marginal is a state of the informational sector with entropy $\log2$; and the demon's knowledge is a joint classical distribution with the record. The coarse-graining that the demon performs is the replacement of the gas's fine description by the two-cell one, and its yield is the conditional entropy it removes. The work itself is extracted later, from the bath, in the reversible feedback step; the demon's information is the *licence* to extract it, not the source of the energy.

## Erasure and the Closing of the Cycle

### The Cost

After the feedback the record still holds the bit, and it must be reset for the next run. The erasure is the map

$$
\mathcal{E}_{\hat{\mathbf{n}}} : \tilde{\rho}_D \longmapsto \tilde{P}_+(\hat{\mathbf{n}}),
$$

the non-unital channel of the companion article *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*, whose entropy debit on the memory is $\Delta\mathcal{S} = -\mathcal{S}(\tilde{\rho}_D)$ and whose material cost is at least $k_BT\,\mathcal{S}(\tilde{\rho}_D)$. For the ideal demon the record is a full bit, $\mathcal{S}(\tilde{\rho}_D) = \log 2$, so

$$
W_{\rm erase} \;\ge\; k_BT\log 2 .
$$

### The Net Work

Collect the terms. The cycle is closed, so the work extracted minus the work spent cannot be positive:

$$
W_{\rm net} = W_{\rm ext} - W_{\rm erase}
\;\le\; k_BT\,I - k_BT\,H(D) ,
$$

where $H(D) = \mathcal{S}(\tilde{\rho}_D)$ is the entropy of the memory. Since the memory's entropy is at least its correlation with the gas,

$$
I \;\le\; H(D) ,
$$

with equality exactly when the record is a deterministic function of the gas — a perfect copy, or its complement — so that there is no residual uncertainty in the record once the gas is known. Therefore

$$
\boxed{\;W_{\rm net} \;\le\; k_BT\left(I - H(D)\right) \;\le\; 0 .\;}
$$

The demon never gains. Three regimes make the accounting concrete.

- **Perfect demon** ($e = 0$): $I = H(D) = \log 2$, so $W_{\rm ext} = W_{\rm erase} = k_BT\log2$ and $W_{\rm net} = 0$. The cycle is reversible and breaks even.
- **Noisy demon** ($0 < e < \tfrac{1}{2}$): $I = \log2 - H_2(e) < \log2 = H(D)$, so $W_{\rm net}\le -k_BT\,H_2(e) < 0$. The demon loses, and loses more the noisier it is. At $e = 0.1$ the guaranteed loss is $0.3250830\,k_BT$ per run.
- **Useless demon** ($e = \tfrac{1}{2}$): $I = 0$, so $W_{\rm net}\le -k_BT\log2$; the demon pays the erasure and extracts nothing.

The general bound is the modern form of the demon's resolution: the extractable work is bounded by the mutual information, the erasure cost is bounded below by the memory's entropy, and the second is never smaller than the first.

### The Ledger of the Cycle

The whole cycle can be written as a work-and-heat ledger, one row per step. For the ideal demon, per run:

| Step | Sector touched | Work done by the device | Heat exchanged with the bath |
|---|---|---|---|
| Correlation (measurement) | $\mathbb{M}_+$ (record) | $0$ | $0$ |
| Feedback (isothermal expansion) | $\mathbb{M}_-$ (gas, bath) | $+k_BT\log 2$ | $-k_BT\log 2$ (absorbed) |
| Restoration | $\mathbb{M}_-$ | $0$ | $0$ |
| Erasure | $\mathbb{M}_+$ (record) | $-k_BT\log 2$ | $+k_BT\log 2$ (released) |
| **Total** | | $\mathbf{0}$ | $\mathbf{0}$ |

The work extracted in the feedback is exactly returned in the erasure, and the heat absorbed during the expansion is exactly released during the reset, so the bath returns to its initial state. The correlation step is thermodynamically free: the joint state of gas and record is unchanged in entropy by the measurement, because the record's marginal entropy is paid for by the correlation rather than by the bath. For the noisy demon the feedback row delivers only $k_BT(\log2 - H_2(e))$ while the erasure row still costs $k_BT\log2$, so the total work is $-k_BT\,H_2(e)$ and the deficit is released as extra heat. The two-sector ledger is the bookkeeping that the demon cannot evade.

### The Alternative Accounting

If the registration of the record is charged instead of the erasure — that is, if the idempotent projection of the measurement is treated as the irreversible step — then the cost appears at the projection rather than at the reset. The projection is a coarse-graining and produces at least the entropy that separates the record's coherence from the classical bookkeeping, and the demon's net work is again non-positive. The two accounts are bookkeeping conventions for the same physical cycle, and the framework's reversible/irreversible dichotomy locates the irreversible step in both cases: a rotor cannot produce entropy, and one of the two non-rotor steps must pay.

## Where the Demon Fails

The cycle fails for a structural reason, and the framework states it exactly. The demon's operations divide into the framework's two dynamical classes.

| Step | Algebra | Reversible? | Work | Entropy change of the sector touched |
|---|---|---|---|---|
| Correlation (measure) | reversible permutation (rotor class) | yes | $0$ | record: $+k_B\log2$, offset by the correlation |
| Feedback | reversible step (rotor class) | yes | $\le k_BT I$ | gas: $+k_B\log2$; bath: $-k_B\log2$ |
| Registration (if charged) | idempotent projection $\Phi_{\hat{\mathbf{n}}}$ | no | $\ge 0$ | record: $\ge 0$ |
| Erasure (standard charge) | non-unital reset $\mathcal{E}_{\hat{\mathbf{n}}}$ | no | $\ge k_BT H(D)$ | memory: $-k_BH(D)$; bath: $+k_BH(D)$ |

Each entry is the change of the object the row touches, and the reversible rows balance exactly within themselves: the gas gains what the bath loses, and the memory's debit is the bath's credit. At the close of the cycle the gas and the record have returned to their initial states, so the net entropy produced is the bath's own, $-k_B\,I + k_B\,H(D)$: it vanishes for the ideal cycle, where $I = H(D) = \log2$, and equals $k_BH_2(e)$ for the noisy demon, which must dump the shortfall as extra heat. Two entries carry a qualification. The gas's $+k_B\log2$ in the feedback row is a **coarse-grained** increase: the demon's description of the gas is the two-cell description "which half", and it is the entropy of that description which rises as the accessible volume widens, while the gas bit's marginal state in $\mathbb{M}_+$ — the maximally mixed state — is the same before and after, and the fine-grained (Gibbs) entropy of the gas is conserved by the underlying Hamiltonian evolution, as in the companion article *Coarse-Graining and the Biquaternion Entropy Functional*. The record's $+k_B\log2$ in the correlation row is likewise a marginal entropy, and it is returned as the correlation, so that the joint entropy of gas and record is unchanged by the copy.

The reversible steps are the demon's power: they create and consume the correlation at no cost to the total entropy, and they have a vanishing Lyapunov spectrum, because a permutation of the joint classical states and a rotor conjugation are both isometries of the description they act on. The irreversible steps are its price: they are contractions, they lower the memory's entropy without returning what they remove to the description itself, and they produce entropy once the compensating environment is included. The demon's entire scheme would work if the record could be reused forever — if the cycle could close with reversible steps alone. It cannot, because the record must be made definite and must be reset, and both are contractions. That is the content of the paradox in this algebra: **the informational sector can hold a correlation reversibly, and it cannot dispose of one reversibly.**

The framework also makes plain what it does not supply. The interaction that correlates the gas with the record is a physical coupling, and the framework's linear structure has no coupling between the sectors to offer: rotor conjugation acts within each sector, carrying $\mathbb{M}_+$ to $\mathbb{M}_+$ and $\mathbb{M}_-$ to $\mathbb{M}_-$ because it preserves Hermiticity, and the only algebraic link between the two sectors is the central factor $i$, which exchanges them without copying anything. The coupling that performs the copy is an input from the physical model, not an output of the algebra. The joint statistics of gas and record are classical and are represented by an ordinary probability table; no tensor product of algebras and no entanglement are used, and the record and the gas **bit** — the two-cell classical description, not the gas itself, which is material — are each represented by a state of $\mathbb{M}_+$, with their correlation carried by the joint classical distribution. The quantum demon, whose memory is entangled with the gas, is a different and larger problem, treated in the sibling quantum category.

## What Is Derived and What Is Imported

**Derived from the algebra.** The representation of the demon's record as a classical state $\tilde{\rho}_D = p_+\tilde{P}_+ + p_-\tilde{P}_-$ of the informational sector, with entropy $\mathcal{S}(\tilde{\rho}_D) = h(|p_+ - p_-|)$; the identification of the reversible steps with the algebra's reversible class — the correlation as a permutation of the joint classical states and the feedback as a reversible thermodynamic step, whose single-sector representative is the rotor conjugation that preserves the norm form and has a vanishing Lyapunov spectrum; the identification of the registration step with the idempotent projection; the identification of the erasure step with the non-unital reset and its entropy debit; the sector assignment of the gas to $\mathbb{M}_-$ and the record to $\mathbb{M}_+$; and the final inequality $W_{\rm net}\le k_BT(I - H(D))\le0$, with the perfect demon saturating at zero and the noisy demon strictly losing. The numerical values — $\log2 = 0.6931472$ for the perfect work and cost, $I(0.1) = 0.3680642$, and the loss $0.3250830\,k_BT$ at $e=0.1$ — were checked by direct computation of the Shannon quantities.

**Imported from standard thermodynamics and information theory.** The Szilard engine and its isothermal work; the Sagawa–Ueda bound on measurement-feedback work; the Landauer cost of erasure; the ideal-gas equation of state; the Clausius relation; and the definition and properties of the mutual information. These are standard, and are transcribed as such.

**Not supplied.** The framework does not derive the work bounds, does not supply the gas–record coupling, does not fix the temperature of the bath, and predicts no violation of the second law in either direction. It predicts, and enforces, only the standard non-positive net work, expressed in the coordinates of the two sectors.

## Summary

The demon's device is a loop through both sectors of the framework. The gas is material, carrying energy and heat in $\mathbb{M}_-$; the record is informational, a classical bit $\tilde{\rho}_D = p_+\tilde{P}_+(\hat{\mathbf{n}}) + p_-\tilde{P}_-(\hat{\mathbf{n}})$ in $\mathbb{M}_+$ with entropy $\mathcal{S}(\tilde{\rho}_D) = h(|p_+ - p_-|)$.

The cycle's four steps are the framework's operations. The **correlation** created by the measurement is a reversible permutation — the rotor class of the algebra: reversible, no work, no entropy — and it creates the mutual information $I$ between gas and record. The **registration** of a definite record is an idempotent projection, a coarse-graining. The **feedback** is a reversible step, and it extracts work bounded by

$$
W_{\rm ext} \;\le\; -\Delta F_{\rm gas} + k_BT\,I ,
$$

which for the cyclic engine, where $\Delta F_{\rm gas} = 0$, reduces to $W_{\rm ext}\le k_BT\,I$. The Szilard realisation attains $W_{\rm ext} = k_BT\log2$ for a perfect record, and $I = \log2 - H_2(e) \le \log2$ for a record with error $e$. The **erasure** is a non-unital channel, the only step that lowers the memory's entropy, and it costs at least

$$
W_{\rm erase} \ge k_BT\,H(D) = k_BT\,\mathcal{S}(\tilde{\rho}_D) \ge k_BT\,I .
$$

The net work of the closed cycle is therefore

$$
W_{\rm net} \le k_BT\left(I - H(D)\right) \le 0 ,
$$

with equality for the perfect demon, which breaks even at $k_BT\log2$ extracted and $k_BT\log2$ spent, and a strict loss $k_BT\,H_2(e)$ for the noisy demon. The demon's reversible steps create and consume the correlation for free; its irreversible steps — registration, when the record is not already definite, and erasure in every case — are where the cost appears. The informational sector can hold a correlation reversibly and cannot dispose of one reversibly, and that asymmetry is the demon's defeat.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) subspaces |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $\tilde{\rho} = \tfrac{1}{2}(e_0+i\mathbf{r})$ | State of the informational sector |
| $\tilde{P}_\pm(\hat{\mathbf{n}}) = \tfrac{1}{2}(e_0\pm i\hat{\mathbf{n}})$ | Pointer idempotents (logical states) |
| $\tilde{\rho}_D = p_+\tilde{P}_+ + p_-\tilde{P}_-$ | Demon's record (classical bit) |
| $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ | Trace, $\mathrm{Tr}(e_0)=2$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form |
| $\mathcal{S}(\tilde{\rho}) = -2\,\mathrm{Sc}(\tilde{\rho}\log\tilde{\rho}) = h(|\mathbf{r}|)$ | Entropy functional (nats) |
| $h(x) = -\tfrac{1+x}{2}\log\tfrac{1+x}{2} - \tfrac{1-x}{2}\log\tfrac{1-x}{2} = H_2\!\left(\tfrac{1-x}{2}\right)$ | Binary entropy, bias argument: $h(0)=\log 2$, $h(1)=0$ |
| $\tilde{P} = i(E/c)e_0 + \mathbf{p}$ | Material four-momentum (gas, bath) |
| $Q$, $T$, $k_B$ | Heat, temperature, Boltzmann constant |
| $\tilde{R}$, $\tilde{R}\tilde{R}^\dagger = e_0$ | Rotor (algebraic representative of the reversible steps) |
| $\Phi_{\hat{\mathbf{n}}}$ | Idempotent projection onto the pointer basis (registration) |
| $\mathcal{E}_{\hat{\mathbf{n}}} : \tilde{\rho}_D\mapsto\tilde{P}_+(\hat{\mathbf{n}})$ | Erasure (non-unital reset) |
| $I(G\!:\!D) = H(G)+H(D)-H(G,D)$ | Mutual information of gas and record |
| $I = \log 2 - H_2(e)$ | Mutual information of a record with error $e$ |
| $H_2(e) = -e\log e - (1-e)\log(1-e)$ | Binary entropy of the error |
| $W_{\rm ext} \le -\Delta F_{\rm gas} + k_BT\,I$ | Sagawa–Ueda bound; $W_{\rm ext}\le k_BT I$ for the closed cycle |
| $W_{\rm ext} = k_BT\log 2$ | Szilard work (one perfect bit) |
| $W_{\rm erase} \ge k_BT\,H(D)$ | Erasure cost (Landauer) |
| $W_{\rm net} \le k_BT(I - H(D)) \le 0$ | Demon's net work (second law restored) |

## Further Reading

- J. C. Maxwell, *Theory of Heat* (Longmans, 1871), for the original statement of the demon.
- L. Szilard, "On the decrease of entropy in a thermodynamic system by the intervention of intelligent beings," *Zeitschrift für Physik* **53** (1929) 840–856, for the one-particle engine and the measurement-feedback cycle.
- L. Brillouin, *Science and Information Theory* (Academic, 1962), for the earlier view that measurement itself is the compensating cost.
- R. Landauer, "Irreversibility and heat generation in the computing process," *IBM Journal of Research and Development* **5** (1961) 183–191, for the erasure cost that closes the cycle.
- C. H. Bennett, "The thermodynamics of computation — a review," *International Journal of Theoretical Physics* **21** (1982) 905–940, for the synthesis in which the demon is defeated by erasure.
- C. H. Bennett, "Demons, engines and the second law," *Scientific American* **257** (1987) 108–116, for an accessible account of the resolution.
- T. Sagawa and M. Ueda, "Minimal energy cost for thermodynamic information processing: measurement and information erasure," *Physical Review Letters* **102** (2009) 250602, for the erasure bound in the presence of correlation.
- T. Sagawa and M. Ueda, "Generalized Jarzynski equality under nonequilibrium feedback control," *Physical Review Letters* **104** (2010) 090602, for the bound on extractable work in terms of mutual information.
- K. Maruyama, F. Nori, and V. Vedral, "Colloquium: The physics of Maxwell's demon and information," *Reviews of Modern Physics* **81** (2009) 1–23, for the modern synthesis of measurement, feedback and erasure.
- J. M. R. Parrondo, J. M. Horowitz, and T. Sagawa, "Thermodynamics of information," *Nature Physics* **11** (2015) 131–139, for the unified account of information-to-work conversion.
- H. S. Leff and A. F. Rex (eds.), *Maxwell's Demon: Entropy, Information, Computing* (Princeton, 1990), for the collected literature on the paradox.
