# __The Upper-Index Problem: The Extent of the Infestation__

## The Rule

The rule is one sentence, and it turns on what the caret marks. *Operator and Calculus Conventions*, §*Conventions for Derivation*, states it in one sentence:

> A caret marks a power or a name, never a frame slot: $e^\lambda$, $2^k$ and $(-1)^k$ are powers, and $\mathrm{Cl}^i$, $K^0$, $M_4^\sigma$ and $\mathbb{B}^\sigma$ are names; a coordinate, a field component, a basis vector, a gamma and a sign symbol are written with a low index — $x_\mu$, $A_\mu$, $\vec e_i$, $\gamma_i$, $\varepsilon_{ijk}$ — and a contraction is written as an explicit sum with the sign vector or as the quaternionic product that carries it.

*Index, Notation and Corpus Conventions* states the same rule for the mathematical corpus, with the form that replaces the contraction. Both articles are linked in §*Further Reading*.

The rule does not forbid every caret. It forbids a caret that marks a frame slot. A spatial matrix $\sigma^i$, a stress component $T^{ij}$ and a field component $F^{jk}$ are frame slots, and they are debt exactly as $x^\mu$ was debt. The exponent $e^\lambda$ is not.

## What the Screens Find

The count is made on the mathematics regions, on a component symbol. A caret on a power, a name, a grade, a star, a dual or a parameter is not an index and is excluded: $(-1)^k$, $2^k$, $\mathrm{Cl}^i$, $\operatorname{Sym}^l$, $k^l$, $r^l$ and $\sum^k$ are powers and grades, and they stay.

| Corpus | Articles | Carets | Frame slots | Verdict |
|---|---:|---:|---:|---|
| Physics | 403 | 71 | 19 in 14 articles | infested |
| Part VI | 889 | 51 | 0 | clean |
| Maths, Parts I to IV | 1508 | 1814 | 357 in 4 articles | infested |

The Greek screen of physics and the whole of Part VI are clean of frame slots: no raised $\mu,\nu,\rho,\lambda,\kappa,\sigma,\tau$ marks a component there. The five physics carets are three integration limits $\int_0^\tau$ in [The Electro-Gravimagnetic Field and the Magnetic Charge–Mass Hypothesis](../articles_physics/the-electro-gravimagnetic-field-and-the-magnetic-charge-mass-hypothesis.html), one exponent $(\alpha/\pi)^\lambda$ in [The Anomalous Magnetic Moment in Biquaternionic Form](../articles_physics/the-anomalous-magnetic-moment-in-biquaternionic-form.html), and the sign label $\nabla^\sigma$ in [Bispinor Fields and the Fundamental Solution](../articles_physics/bispinor-fields-and-the-fundamental-solution-of-the-generalized-maxwell-dirac-equation.html). None is an index.

The Latin screen is not clean. **19 raised $i,j,k,l$ frame slots in 14 physics articles** are the live infestation. A further 52 carets on the same letters sit on powers, grades and names, and they are not counted. The Greek pass never touched the Latin ones.

## The Named Cases

Two of the three tokens named in the report have been rewritten. The field component $F_{jk}$ was lowered in both of its articles, and the stress component $T_{ij}$ no longer appears raised anywhere in the physics corpus. The third, the Pauli matrix, survives raised in one place:

| Token | Where | Meaning |
|---|---|---|
| $\sigma^i$ | [The Bloch Ball as the Normalised Slice of the Future Light Cone](../articles_physics/the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.html) | Pauli matrices; the $k$ and $i$ forms are the same object |

The list is longer than three. The remaining bases are $x$, $\sigma$, $\alpha$, $\pi$, $K$, $J$, $F$, $E$, $H$, $T$, $\eta$ and $\Lambda$, one or two each; the grouped signs $\varepsilon^{ijk}$ and $\delta^{jk}$ are already gone.

## The Physics Infestation, Article by Article

Every article below still carries at least one raised frame slot. The last column lists the tokens and their count in that article. Twenty-six articles have been rewritten and are no longer listed. [Scattering for the Quaternionic Dirac Operator](../articles_physics/scattering-for-the-quaternionic-dirac-operator.html) had 28 frame slots, now zero: its $M^k$ became $L_k$, its $M_k$ became $R_k$, its $M^{ik}$ became $L_{ik}$, and its $u^i$ and $u^s$ became the upright names $u^{\mathrm{inc}}$ and $u^{\mathrm{sc}}$. [The Spinor Module in Biquaternionic Form and Its Lorentz Action](../articles_physics/the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) had 27, now zero: its triple became $\varsigma_1=\sigma_3$, $\varsigma_2=i\sigma_2$, $\varsigma_3=-i\sigma_1$, its components became $v_i$, and its two contractions were written out with $\sum_{k,l}\varepsilon_{ijk}\eta_{kl}$. [Zitterbewegung in Biquaternionic Form](../articles_physics/zitterbewegung-in-biquaternionic-form.html) had 25 frame slots, now zero: $\alpha^k$, $\alpha^j$ and $\boldsymbol{\alpha}^k$ became $\alpha_k$, $\alpha_j$ and $\boldsymbol{\alpha}_k$, $x^k$ became $x_k$, and $\delta^{jk}$ became $\delta_{jk}$. [The Lorentz Group — Structure and Representations](../articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.html) had 20, now zero: its triple became $\varsigma_1=\sigma_3$, $\varsigma_2=i\sigma_2$, $\varsigma_3=-i\sigma_1$, its components became $v_i$, and the $SU(1,1)$ closure is written out with $\sum_{k,l}\varepsilon_{ijk}\eta^{(1,2)}_{kl}$. [The Foldy–Wouthuysen Transformation](../articles_physics/the-foldy-wouthuysen-transformation-in-biquaternionic-form.html) had 15, now zero: $\alpha^k$, $\alpha^j$ and $\sigma^k$ became $\alpha_k$, $\alpha_j$ and $\sigma_k$, and $\delta^{jk}$ became $\delta_{jk}$. [The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) had 13, now zero: $\Sigma^k$ became $\Sigma_k$ and $\sigma^k$ became $\sigma_k$, down to the entry-by-entry check $\sigma_{01}\gamma_5=i\,\mathrm{diag}(\sigma_1,\sigma_1)$. [Quantum Gravity under the Biquaternion Framework](../articles_physics/quantum-gravity-under-the-biquaternion-framework-a-research-agenda.html) had 12, now zero: $v^i$ and $\varsigma^i$ became $v_i$ and $\varsigma_i$, the triple was written componentwise, and the closure as $\{v_i,v_j\}=-\sum_{k,l}\varepsilon_{ijk}\eta_{kl}v_l$. [Canonical Quantization of the Biquaternion Proca Field](../articles_physics/canonical-quantization-of-the-biquaternion-proca-field.html) had 11, now zero: $\pi^i$ became $\pi_i$, and each Gauss-law contraction is written $\sum_i\partial/\partial Q_i\,\pi_i$. [The Neutrino and Majorana Fermions in Biquaternionic Form](../articles_physics/the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) had 10, now zero: its spinor-model summary became $v_i=\langle z|\sigma_i|z\rangle$, $v_i=\tfrac12\langle z|\sigma_3\varsigma_i|z\rangle$ and $v_i=\langle z_2|\sigma_3\varsigma_i|z_1\rangle$, with the triple defined once. [The Rarita–Schwinger Equation](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) had 10, now zero: $\sigma^k$ became $\sigma_k$, and $\Gamma^{jk}$, $\Gamma^{00}$ became $\Gamma_{jk}$, $\Gamma_{00}$. [Matter Makes Space](../articles_physics/matter-makes-space-an-external-construction-from-quaternionic-spinors.html) had 9, now zero: $q_k=-i\sigma^k$ became $q_k=-i\sigma_k$, $[q_0,q^i]$ and $[q^i,q^j]$ became $[q_0,q_i]$ and $[q_i,q_j]$, and $q^{ij}$ became $q_{ij}$. [The Classical Spinning Particle](../articles_physics/the-classical-spinning-particle-the-bargmann-michel-telegdi-equation-in-biquaternionic-form.html) had 8, now zero: $F^{tk}$, $F^{kt}$, $F^{jk}$, $F^{kj}$ became $F_{tk}$, $F_{kt}$, $F_{jk}$, $F_{kj}$, and $v^k$, $s^k$, $X^k$ became $v_k$, $s_k$, $X_k$. [The Dirac Oscillator](../articles_physics/the-dirac-oscillator-in-biquaternionic-form.html) had 7, now zero: $\alpha^k$ and $\sigma^k$ became $\alpha_k$ and $\sigma_k$. [Exercise: The Non-Relativistic Limit and the Pauli Equation](../articles_physics/exercise-the-non-relativistic-limit-and-the-pauli-equation.html) had 6, now zero: $\alpha^k$ became $\alpha_k$, and $\alpha^i\alpha^j=\delta^{ij}+i\epsilon^{ijk}\Sigma_k$ became $\alpha_i\alpha_j=\delta_{ij}+i\sum_k\varepsilon_{ijk}\Sigma_k$. [Anomalies and Anomaly Cancellation](../articles_physics/anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) had 3, now zero: $\sigma^k$ became $\sigma_k$, and the boundary flux is written $\sum_i\oint dS_i\,K_i$. [The Path Integral](../articles_physics/the-path-integral-in-biquaternionic-form.html) had 3, now zero: $dx^i/dt'\,dx^j/dt'$ became $dx_i/dt'\,dx_j/dt'$ with $\sum_{i,j}$, and the inverse metric $g^{ij}$ became $(g^{-1})_{ij}$. [Chiral Fermions](../articles_physics/chiral-fermions-in-the-biquaternion-framework.html) had 2, now zero: $\sigma^k$ became $\sigma_k$. [Operator and Calculus Conventions](../articles_physics/conventions-of-the-operators-and-the-calculus.html) had 2, now zero: the rule names the raised Pauli matrix and the raised stress component in words, instead of writing $\sigma^i$ and $T^{ij}$. [Exercise: Chirality and the Weyl Spinors](../articles_physics/exercise-chirality-and-the-weyl-spinors.html) had 2, now zero: $\sigma^k$ became $\sigma_k$. [The Chiral Condensate](../articles_physics/the-chiral-condensate-and-dynamical-symmetry-breaking-in-biquaternionic-form.html) had 2, now zero: $\sigma^k$ became $\sigma_k$. [The Daviau Map](../articles_physics/the-daviau-map-and-the-space-clifford-formulation-of-the-dirac-equation.html) had 2, now zero: the duplicated $\partial/\partial x^k=\partial/\partial x^k$ became the single $\partial/\partial x_k$. [Lagrangian and Hamiltonian Mechanics](../articles_physics/lagrangian-and-hamiltonian-mechanics-in-biquaternionic-form.html) had 6, now zero: the velocities became $dq_i/dt'$, and both quadratic forms are written with $\sum_{ij}$. [The Quantized Dirac Field](../articles_physics/the-quantized-dirac-field-in-biquaternionic-form.html) had 6, now zero: $S^k$, $\Sigma^k$ and $\sigma^k$ became $S_k$, $\Sigma_k$ and $\sigma_k$. [Fisher Information and the Biquaternion Norm](../articles_physics/fisher-information-and-the-biquaternion-norm.html) had 4, now zero: $d\theta^i\,d\theta^j$ and $\partial^2/\partial\theta^i\partial\theta^j$ became $d\theta_i\,d\theta_j$ and $\partial^2/\partial\theta_i\partial\theta^j$. [The CPT Theorem](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html) had 4, now zero: $\sigma^k$ became $\sigma_k$, and $\partial/\partial x^k$ became $\partial/\partial x_k$. [The Dirac Equation](../articles_physics/the-dirac-equation-in-biquaternionic-form.html) had 4, now zero: $\sigma^k$ became $\sigma_k$ in the algebra map and in the $\gamma_k$ blocks.

| Article | Raised | Problematic notations |
|---|---:|---|
| [The First-Order Root of the Biquaternion Klein–Gordon Operator](../articles_physics/the-first-order-root-of-the-biquaternion-klein-gordon-operator.html) | 2 | $x^{k}$ (2) |
| [The Fujikawa Method and the Path-Integral Anomaly in Biquaternionic Form](../articles_physics/the-fujikawa-method-and-the-path-integral-anomaly-in-biquaternionic-form.html) | 2 | $\sigma^{k}$ (2) |
| [The Lorentz Force in Biquaternion Form](../articles_physics/the-lorentz-force-in-biquaternion-form.html) | 2 | $F^{kj}$, $K^{k}$ |
| [The s-Vector Representation of the Dirac Spinor in Biquaternionic Form](../articles_physics/the-s-vector-representation-of-the-dirac-spinor-in-biquaternionic-form.html) | 2 | $E^{i}$, $H^{i}$ |
| [The Stueckelberg Mechanism in Biquaternionic Form](../articles_physics/the-stueckelberg-mechanism-in-biquaternionic-form.html) | 2 | $\pi^{i}$ (2) |
| [Canonical Quantization of the Biquaternion Graviton Field](../articles_physics/canonical-quantization-of-the-biquaternion-graviton-field.html) | 1 | $T^{l}$ |
| [Confinement and the Loss of Partonic Information in Biquaternionic Form](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) | 1 | $x^{k}$ |
| [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](../articles_physics/exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html) | 1 | $x^{k}$ |
| [Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form](../articles_physics/fermion-doubling-and-the-nielsen-ninomiya-theorem-in-biquaternionic-form.html) | 1 | $x^{k}$ |
| [Gravitational Waves in Biquaternionic Form](../articles_physics/gravitational-waves-in-biquaternionic-form.html) | 1 | $\eta^{ij}$ |
| [Noether's Theorem in Biquaternionic Form](../articles_physics/noethers-theorem-in-biquaternionic-form.html) | 1 | $J^{k}$ |
| [Non-Abelian Gauge Fields in Biquaternionic Form](../articles_physics/non-abelian-gauge-fields-in-biquaternionic-form.html) | 1 | $x^{k}$ |
| [The Bloch Ball as the Normalised Slice of the Future Light Cone](../articles_physics/the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.html) | 1 | $\sigma^{i}$ |
| [The Hydrogen Atom in Biquaternionic Form — The Relativistic Case](../articles_physics/the-hydrogen-atom-in-biquaternionic-form-the-relativistic-case.html) | 1 | $\alpha^{k}$ |

**Total: 19 in 14 articles.**

Three rows have left the list without a rewrite. [SU(3) Representations and the Gell-Mann–Okubo Mass Formula](../articles_physics/su3-representations-and-the-gell-mann-okubo-mass-formula-in-biquaternionic-form.html) carries carets only on Okubo's basis $A^{i}_{\ k}$. The pair is mixed, one fundamental and one antifundamental index, and the height is the representation: it carries the trace $A^{k}_{\ k}$, the product $A^{i}_{\ k}A^{k}_{\ l}$, and the invariant $\delta^{i}_{\ k}$, which is not a metric. Lowering the upper index would replace the mixed delta by a Euclidean one and hide the representation, so the screen over-counted these and they stay.

[The ADHM Construction and Biquaternion Instanton Data](../articles_physics/the-adhm-construction-and-biquaternion-instanton-data.html) carries carets only on the dimensions $\mathbb{C}^k$ and $\mathbb{C}^N$ of the ADHM matrix data. The letter is the dimension of the vector space, not a frame slot: it indexes no coordinate, no basis vector and no gamma, and the corpus writes $\mathbb{C}^3$ the same way. The screen over-counted these six and they stay.

[The Bhabha Multi-Mass Wave Equations and the Bivector Space in Biquaternionic Form](../articles_physics/bhabha-multi-mass-wave-equations-and-the-bivector-space-in-biquaternionic-form.html) carries carets only on $\Lambda^{l}_j$ and $\Lambda^{\bar l}_j$. The letters $l$ and $\bar l$ label the two representations, as the factors $\mathbf{1}_{2l+1}$ and $\mathbf{1}_{2\bar l+1}$ in the same display show; $j$ is the generator label and is already low. The height records the representation, as in Okubo's $A^{i}_{\ k}$, and lowering it would hide which representation the generator acts on. The screen over-counted these two and they stay.

## The Part VI Screen

Part VI has 51 raised Greek carets in 19 articles, and none is a coordinate. They are the exponential $e^\lambda$, the exponential $e^\mu$, the power $\tilde\xi^\nu$, the character $a^\lambda$, the fixed algebra $M_4^\sigma$ and the module twist $\mathbb{B}^\sigma$. The Latin carets in Part VI are powers of a formal variable and unit labels, not components. Part VI is clean for the index rule.

The count is spread thin: the largest case is [The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra](../articles_maths/the-canonical-hermitian-form-on-the-regular-module-of-the-biquaternion-algebra.html) with eight twists $\mathbb{B}^\sigma$, then [The Exponential and the Lie Group of $M_6(\mathbb{C})$](../articles_maths/the-exponential-and-the-lie-group-of-m6c.html) and [The Exponential and the Lie Group of $M_3(\mathbb{C})$](../articles_maths/the-exponential-and-the-lie-group-of-m3c.html) with the powers of the exponential. The rest carry one to five.

## The Maths Infestation, Parts I to IV

Parts I to IV hold 1814 raised Greek carets, and most of them are not frame slots: the fixed set $A^\sigma$ of an involution, the character $\chi^\lambda$ of a partition, the Specht module $S^\lambda$, the monomial $x^\lambda$ of a symmetric function and the zeta term $x^\rho$. Those are names and powers, and they stay.

Four articles carry a frame slot. They are the field-theory and tensor-calculus articles, where the caret marks a coordinate, a momentum, a current, a gamma trace or a structure constant.

| Article | Frame slots | Problematic notations |
|---|---:|---|
| [Noether's Two Theorems](../articles_maths/noethers-two-theorems.html) | 199 | $x^{\mu}$ (53), $L^{\mu}$ (20), $x^{\nu}$ (19), $F^{\mu}$ (16), $j^{\mu}$ (14), $\varepsilon^{\alpha}$ (12), $\partial^{\mu}$ (11), $F^{\mu\nu}$ (8), $E^{\nu}$ (6), $A^{\mu}$ (5), $T^{\mu}$ (5), $\Theta^{\mu}$ (5), $\xi^{\nu}$ (5), $\xi^{\mu}$ (4), $A^{\nu}$ (3), $\partial^{\nu}$ (3), $j^{\nu}$ (3), $F^{\lambda\mu}$ (2), $\delta^{\mu}$ (2), $x^{\lambda}$ (2), $\xi^{\phi}$ |
| [Multisymplectic and Covariant Hamiltonian Field Theory](../articles_maths/multisymplectic-and-covariant-hamiltonian-field-theory.html) | 131 | $x^{\mu}$ (58), $p^{\mu}$ (41), $x^{\nu}$ (12), $J^{\mu}$ (7), $g^{\mu\nu}$ (6), $\delta^{\mu}$ (4), $\partial^{\mu}$ (3) |
| [The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System](../articles_maths/the-lie-jordan-decomposition-of-a-bilinear-product-and-the-jordan-triple-system.html) | 15 | $c^{\mu\nu\lambda}$ (6), $t^{\mu\nu\lambda\rho}$ (5), $c^{\mu\lambda\nu}$ (2), $k^{\mu}$ (2) |
| [The Dirac–Kähler Equation](../articles_maths/the-dirac-kahler-equation.html) | 12 | $x^{\mu}$ (10), $\delta^{\mu\nu}$, $x^{\nu}$ |

**Total: 357 in 4 articles.**

The two largest cases are the field-theory pair, and they hold 330 of the 357. [Noether's Two Theorems](../articles_maths/noethers-two-theorems.html) carries every ingredient of the covariant notation at once: $x^\mu$, $\partial^\mu$, $F^{\mu\nu}$, $j^\mu$, $\Theta^\mu$ and the spinor $\varepsilon^\alpha$. [Multisymplectic and Covariant Hamiltonian Field Theory](../articles_maths/multisymplectic-and-covariant-hamiltonian-field-theory.html) carries the multimomentum $p^\mu$ alongside $x^\mu$ and $g^{\mu\nu}$.

## The Order of Repair

1. **The physics Latin pass.** 19 tokens, 14 articles. The twenty-six largest cases are done: *Scattering for the Quaternionic Dirac Operator* (28), *The Spinor Module and Its Lorentz Action* (27), *Zitterbewegung in Biquaternionic Form* (25), *The Lorentz Group — Structure and Representations* (20), *The Foldy–Wouthuysen Transformation* (15), *The Electric Dipole Moment* (13), *Quantum Gravity under the Biquaternion Framework* (12), *Canonical Quantization of the Proca Field* (11), *The Neutrino and Majorana Fermions* (10), *The Rarita–Schwinger Equation* (10), *Matter Makes Space* (9), *The Classical Spinning Particle* (8), *The Dirac Oscillator* (7), *The Non-Relativistic Limit exercise* (6), *Lagrangian and Hamiltonian Mechanics* (6), *The Quantized Dirac Field* (6), *Fisher Information and the Biquaternion Norm* (4), *The CPT Theorem* (4) and *The Dirac Equation* (4), *Anomalies and Anomaly Cancellation* (3), *The Path Integral* (3), *Chiral Fermions* (2), *Operator and Calculus Conventions* (2), *Exercise: Chirality and the Weyl Spinors* (2), *The Chiral Condensate* (2) and *The Daviau Map* (2). Every $\sigma^i$, $T^{ij}$ and $F^{jk}$ is lowered to $\sigma_i$, $T_{ij}$, $F_{jk}$; the spatial sum is written explicitly with $\delta_{ij}$ or with the Euclidean sign vector, exactly as the Greek pass wrote $\varepsilon$. The Pauli and Dirac matrices keep their letter and lose their height: $\sigma_k$, $\alpha_k$, $\gamma_k$.
2. **The grouped pairs come with the same pass.** Two of the three are done: $\varepsilon^{ijk}$ and $\delta^{jk}$ are already low everywhere in physics. The third, $\eta^{ij}$, becomes $\eta_{ij}$ with the sum written out.
3. **The maths field-theory pass.** 357 tokens, 4 articles. $x^\mu$ becomes $x_\mu$, $\partial^\mu$ becomes $\partial_\mu$, $F^{\mu\nu}$ becomes $F_{\mu\nu}$, and every contraction is written as an explicit sum. The two field-theory articles hold 330 of them; the Dirac–Kähler and Lie–Jordan articles hold the other 27.
4. **The labels stay.** $K^0$, $H^0$, $A^0$, $(-1)^k$, $2^k$, $\mathrm{Cl}^i$, $e^\lambda$, $A^\sigma$, $S^\lambda$, $\chi^\lambda$ and $x^\rho$ of a zeta term are names, powers and grades, not frame slots. The mixed pair $A^{i}_{\ k}$ of the Okubo basis is a representation index, not a frame slot. Lowering any of them would be an error, not a repair.
5. **The convention article is the gate.** A new raised frame index in either corpus is a regression. The check reads the same sentence as the rule.

## Summary

The rule: a caret marks a power or a name, never a frame slot. The physics Greek screen and Part VI are clean: 0 frame slots. The infestation is **19 raised frame slots in 14 physics articles**, including the last named case, $\sigma^i$, and **357 in 4 articles of Parts I to IV**, led by $x^\mu$ and $p^\mu$ in the two field-theory articles. A further 52 physics carets on $i,j,k,l$ are powers and names, and they stay.

The infestation is therefore open, quantified and located. The audit is not a report of work done; it is the list of what is left.

## Summary of Notation

| Token | Meaning |
|---|---|
| $\sigma_i$, $T_{ij}$, $F_{jk}$ | the target form: every index low |
| $\sigma^i$ | the infestation: still raised, still counted |
| $\varepsilon=(1,-1,-1,-1)$ | sign vector inside the product; the Lorentzian signs |
| $\delta_{ij}$ | Euclidean sign vector for the spatial sum |
| $K^0$, $H^0$, $A^0$ | names, not indices; they stay |
| $e^\lambda$, $\mathrm{Cl}^i$, $(-1)^k$ | a power and two grades, not indices |

## Further Reading

- [Operator and Calculus Conventions](../articles_physics/conventions-of-the-operators-and-the-calculus.html) — the rule itself, now free of raised specimens.
- [Index, Notation and Corpus Conventions](../articles_maths/conventions-of-the-indices-the-notation-and-the-corpus.html) — the same rule for the mathematical corpus.
- [The First-Order Root of the Biquaternion Klein–Gordon Operator](../articles_physics/the-first-order-root-of-the-biquaternion-klein-gordon-operator.html) — 2 of the 19, tied for the largest physics case with *The Fujikawa Method*, *The Lorentz Force*, *The s-Vector Representation* and *The Stueckelberg Mechanism*.
- [Noether's Two Theorems](../articles_maths/noethers-two-theorems.html) — 199, the largest case of the whole corpus.
- [Multisymplectic and Covariant Hamiltonian Field Theory](../articles_maths/multisymplectic-and-covariant-hamiltonian-field-theory.html) — 131.
