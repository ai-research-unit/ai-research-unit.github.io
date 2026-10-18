# __The Lorentz Force in Biquaternion Form__

## Introduction

A charged particle moving in an electromagnetic field is acted on by the **Lorentz force**. In the four-dimensional language of relativity this force is the contraction of the field-strength tensor with the four-velocity, $K^\mu = ϙ\,F^{\mu\nu}v_\nu$; in three-vector language it reads $ϙ(\vec E + \vec v\times\vec B)$ for the spatial part, together with the power $ϙ\,\vec E\cdot\vec v$ in the time part. The companion article *Relativistic Mechanics in Biquaternionic Form* recorded the biquaternion component form of this four-force and identified it as an element of the anti-Hermitian subspace $\mathbb{M}_-$. That article also recorded, explicitly and twice, an open problem: the expression of the same four-force as a **biquaternion product** of the field-strength biquaternion $\tilde{F}$ and the four-velocity $\tilde{V}$ is *not* simply the real part of $\tilde{F}\circ\tilde{V}$, the correct expression "involves the representation theory of $\mathbb{B}$ in the even subalgebra of $\mathrm{Cl}_{1,3}$", and it "remains to be worked out cleanly".

This article carries out that work. The result is a two-term product formula, bilinear in the field and the four-velocity, that reproduces the component form exactly. In its most compact shape the formula is a single projection:

$$
\boxed{\;\tilde{K}_{\mathrm{f}} = -\,ϙ\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{V}\,\tilde{F}\right),\qquad
P_{\mathbb{M}_-}(\tilde{Q}) = \tfrac{1}{2}\left(\tilde{Q} - \tilde{Q}^{*}\right).\;}
$$

The projection $P_{\mathbb{M}_-}$ is the anti-Hermitian part, and it lands in the material sector $\mathbb{M}_-$ automatically. Written out, the formula is

$$
\tilde{K}_{\mathrm{f}} = -\,\frac{ϙ\sqrt{\mu}}{2}\left(\tilde{V}\,\tilde{F} + \tilde{F}^{*}\,\tilde{V}\right),
$$

or, since $\tilde{F}^{*} = -\tilde{F}^*$,

$$
\tilde{K}_{\mathrm{f}} = -\,\frac{ϙ\sqrt{\mu}}{2}\left(\tilde{V}\,\tilde{F} - \tilde{F}^*\,\tilde{V}\right).
$$

Here $\tilde{F}^{*}$ is the Hermitian conjugate of the field strength and $\tilde{F}^*$ its complex conjugate. The appearance of the conjugate field is not a technicality: $\tilde{F}$ and $\tilde{F}^{*}$ are (up to constant factors) the self-dual and anti-self-dual halves of the field tensor, and the formula pairs the four-velocity with both halves. This is the sense in which the result "involves the representation theory of $\mathbb{B}$" — but, as the derivation below shows, the formula itself lives entirely inside $\mathbb{B}$ and needs no Clifford algebra beyond the identification $\mathbb{B}\cong\mathbb{C}\ell_{1,3}^{+}$.

**A note on notation.** The companion article *The Field-Strength Biquaternion and Its Invariants* fixes the symbol $\tilde{F}$ for the field-strength biquaternion "once and for all". The companion article *Relativistic Mechanics in Biquaternionic Form* wrote $\tilde{F}_{\text{EM}}$ for the field and, in its earlier versions, $\tilde{F}$ for the four-force. To remove the collision this article adopts, and the corpus now uses, the letter $\tilde{K}_{\mathrm{f}}$ for the **four-force biquaternion** (the Minkowski force), reserving $\tilde{F}$ for the field strength. Thus

$$
\tilde{K}_{\mathrm{f}} = \frac{d\tilde{P}}{d\tau}, \qquad \tilde{P} = m\tilde{V},
$$

and the field strength keeps the canonical form $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ of the field-strength article.

The conventions are those of the read-list articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$, and the scalar imaginary is $i$ (central, $i^2 = -1$). The conjugate of a biquaternion $\tilde{Q} = \tilde{Q}_te_t + \tilde{Q}_x\vec e_x + \tilde{Q}_y\vec e_y + \tilde{Q}_z\vec e_z$ is $\bar{X} = \tilde{Q}_te_t - \vec Q$, its complex conjugate is $\tilde{Q}^* = \sum_\mu \tilde{Q}_\mu^* e_\mu$, and its Hermitian conjugate is $\tilde{Q}^{*} = \bar{X}^{\,*} = \sum_\mu \tilde{Q}_\mu^* e_\mu$ with the vector components negated. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium, $\vec v$ is the particle velocity, $\vec v_b$ is a frame (boost) velocity, and $\vec B = \mu\vec H$ is the magnetic induction.

## The Lorentz Four-Force in Component Form

The component form is the established result, and it is the starting point of everything that follows. For a particle of charge $ϙ$ and velocity $\vec v$ in fields $\vec E$ and $\vec B$, the **Lorentz four-force biquaternion** is

$$
\tilde{K}_{\mathrm{f}} = i\,\frac{\gamma ϙ}{c}\left(\vec E\cdot\vec v\right)e_t + \gamma ϙ\left(\vec E + \vec v\times\vec B\right),
$$

where

$$
\gamma = \frac{1}{\sqrt{1 - \vec v^2/c^2}}
$$

is the Lorentz factor. The scalar part is purely imaginary and the vector part is real, so $\tilde{K}_{\mathrm{f}}$ lies in the anti-Hermitian subspace $\mathbb{M}_-$, like the four-velocity $\tilde{V} = \gamma(ic\,e_t + \vec v)$ and the four-momentum $\tilde{P} = m\tilde{V}$. Writing $\vec f = ϙ(\vec E + \vec v\times\vec B)$ for the (relativistic) three-force and $P_{\text{mech}} = \vec f\cdot\vec v = ϙ\,\vec E\cdot\vec v$ for the mechanical power, the component form reads

$$
\tilde{K}_{\mathrm{f}} = i\,\frac{\gamma P_{\text{mech}}}{c}\,e_t + \gamma\,\vec f.
$$

This is the biquaternion transcription of the Minkowski force $K^\mu = (i\gamma P_{\text{mech}}/c,\ \gamma\vec f)$ in the $ict$ convention, so the coefficient of $e_t$ is the $ict$ time component $K^0$.

**Origin in the field tensor.** The component form is the contraction $K^\mu = ϙ\,F^{\mu\nu}v_\nu$. In the $ict$ convention the metric is Euclidean, so no metric factor arises and $v_\nu = v^\nu = (i\gamma c,\ \gamma\vec v)$. The field tensor is the one fixed by the field-strength article,

$$
F^{\mu\nu} =
\begin{pmatrix}
0 & iE_x/c & iE_y/c & iE_z/c \\
-iE_x/c & 0 & B_z & -B_y \\
-iE_y/c & -B_z & 0 & B_x \\
-iE_z/c & B_y & -B_x & 0
\end{pmatrix},
$$

that is, $F^{0k} = iE_k/c$ and $F^{jk} = \epsilon_{jkl}B_l$. The time component of the contraction is

$$
K^0 = ϙ\,F^{0k}u_k = ϙ\,\frac{iE_k}{c}\,\gamma v_k = i\,\frac{\gamma ϙ}{c}\,\vec E\cdot\vec v,
$$

and the spatial components are

$$
K^k = ϙ\,F^{k0}u_0 + ϙ\,F^{kj}u_j
= ϙ\left(-\frac{iE_k}{c}\right)(i\gamma c) + ϙ\,\epsilon_{kjl}B_l\,\gamma v_j
= \gamma ϙ\,E_k + \gamma ϙ\left(\vec v\times\vec B\right)_k,
$$

which is exactly the vector part above. The component form and the tensor contraction are the same statement.

## The Four-Force as an Element of $\mathbb{M}_-$

The four-force is a four-vector, and it lives in the same subspace as the four-velocity and the four-momentum. Two structural facts make this precise.

**1. Anti-Hermiticity.** Because the scalar part of $\tilde{K}_{\mathrm{f}}$ is purely imaginary and its vector part is real, it satisfies

$$
\tilde{K}_{\mathrm{f}}^{*} = -\tilde{K}_{\mathrm{f}}.
$$

This is the defining property of $\mathbb{M}_-$. Equivalently, $\tilde{K}_{\mathrm{f}}$ has no Hermitian part:

$$
\tfrac{1}{2}\left(\tilde{K}_{\mathrm{f}} + \tilde{K}_{\mathrm{f}}^{*}\right) = 0.
$$

The whole content of the four-force is in its anti-Hermitian half. The same is true of $\tilde{V}$ and $\tilde{P}$, and this is why $\mathbb{M}_-$ is called the material sector: it is the subspace of four-vectors.

**2. Orthogonality to the four-momentum.** The four-momentum has fixed biquaternion norm, $\tilde{P}\tilde{P}^{\natural} = -m^2c^2$, along the worldline. Differentiating and using $\tilde{K}_{\mathrm{f}} = d\tilde{P}/d\tau$ gives

$$
\tilde{K}_{\mathrm{f}}\tilde{P}^{\natural} + \tilde{P}\tilde{K}_{\mathrm{f}}^{\natural} = 0,
$$

the biquaternion form of the Minkowski orthogonality $K^\mu P_\mu = 0$. The four-force changes the direction of the four-momentum but not its norm. This is examined further in the section on invariants.

## The Product Problem

The natural first guess is that the four-force is obtained by multiplying the field strength by the four-velocity and taking a real or imaginary part, in analogy with the way the field energy is obtained from $\tilde{F}\tilde{F}^{*}$. That guess fails, and it is worth seeing exactly why, because the failure dictates the shape of the correct formula.

The field strength is a pure-vector biquaternion, $\tilde{F} = \vec F$ with $\vec F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$, so its quaternion conjugate is $\tilde{F}^{\natural} = -\tilde{F}$. For a pure vector $\vec a$ and the four-velocity $\tilde{V} = i\gamma c + \gamma\vec v$, the quaternion product rule $\vec a\vec b = -\vec a\cdot\vec b + \vec a\times\vec b$ gives

$$
\tilde{F}\tilde{V} = i\gamma c\,\tilde{F} - \gamma\left(\tilde{F}\cdot\vec v\right) + \gamma\left(\tilde{F}\times\vec v\right),
\qquad
\tilde{V}\tilde{F} = i\gamma c\,\tilde{F} - \gamma\left(\tilde{F}\cdot\vec v\right) - \gamma\left(\tilde{F}\times\vec v\right),
$$

so that

$$
\tilde{F}\tilde{V} + \tilde{V}\tilde{F} = 2i\gamma c\,\tilde{F} - 2\gamma\left(\tilde{F}\cdot\vec v\right),
\qquad
\tilde{F}\tilde{V} - \tilde{V}\tilde{F} = 2\gamma\left(\tilde{F}\times\vec v\right).
$$

The product $\tilde{F}\tilde{V}$ has scalar part $-\gamma\,\tilde{F}\cdot\vec v$, which is a **complex** number in general, and vector part $i\gamma c\,\tilde{F} + \gamma\,\tilde{F}\times\vec v$. Its real part therefore has a **real** scalar part, whereas the four-force has a **purely imaginary** scalar part. Consequently $\operatorname{Re}(\tilde{F}\tilde{V})$ does not lie in $\mathbb{M}_-$ at all: it cannot be the four-force, for the elementary reason that it is the wrong kind of biquaternion. This is the precise content of the statement in the relativistic-mechanics article that the four-force is "not simply the real part of $\tilde{F}\circ\tilde{V}$".

There is a second obstruction. The field strength mixes $\vec E$ and $\vec B$ with the fixed weights $\sqrt{\epsilon}$, $\sqrt{\mu}$ and with opposite reality properties — the electric part imaginary, the magnetic part real — whereas the four-force requires $\vec E$ and the magnetic force $\vec v\times\vec B$ to enter with the *same* coefficient $\gamma ϙ$. A single product of $\tilde{F}$ with $\tilde{V}$ keeps these weights locked together. Separating them requires the conjugate field $\tilde{F}^{*}$, in which the relative sign of the electric and magnetic parts is reversed:

$$
\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H,
\qquad
\tilde{F}^{*} = i\sqrt{\epsilon}\,\vec E + \sqrt{\mu}\,\vec H.
$$

The combination that extracts $\vec E$ is $\tilde{F} + \tilde{F}^{*} = 2i\sqrt{\epsilon}\,\vec E$; the combination that extracts $\vec B$ is $\tilde{F}^{*} - \tilde{F} = 2\sqrt{\mu}\,\vec H = 2\vec B/\sqrt{\mu}$. So the correct product formula must involve both $\tilde{F}$ and $\tilde{F}^{*}$. This is the technical reason the earlier article anticipated "the representation theory of $\mathbb{B}$ in the even subalgebra of $\mathrm{Cl}_{1,3}$": the two objects $\tilde{F}$ and $\tilde{F}^{*}$ are the self-dual and anti-self-dual halves of the field tensor, and the Lorentz force pairs the four-velocity with both.

**A different route.** The obstruction above is real but it is not the only way to the force. If one lets the boost rotor of the particle depend on proper time — the **eigenspinor** $\tilde U(\tau)$ of *The Eigenspinor: The Lorentz Rotor as a Function of Proper Time* — then the force arises from a **linear** source rather than a product: $d\tilde U/d\tau = \tfrac12\vec\Omega_{\mathrm{LT}}\tilde U$ with $\vec\Omega_{\mathrm{LT}} = -(ϙ/m)\tilde{F}^{*}$, and the equation of motion is $d\tilde{P}/d\tau = P_{\mathbb{M}_-}(\vec\Omega_{\mathrm{LT}}\tilde{P})$. The force is still not a single product of $\tilde{F}$ with $\tilde{V}$, so the finding of this section stands; what the eigenspinor shows is that the product formula of the next section is a *derived* corollary of a linear evolution, not the primitive statement of the law. The two routes agree on every configuration, and the agreement was checked in the eigenspinor article.

## The Biquaternion Product Formula

We now derive the formula. The derivation is elementary: invert the product identities above to obtain the electric and magnetic fields in terms of the symmetrized and antisymmetrized products of $\tilde{F}$ and $\tilde{V}$, substitute into the component form, and collect terms.

**Step 1: the fields from the products.** From the identities of the previous section, and the same identities with $\tilde{F}$ replaced by $\tilde{F}^{*}$,

$$
\operatorname{Sc}\!\left(\tilde{F}\tilde{V} + \tilde{V}\tilde{F}\right) = -2\gamma\,\tilde{F}\cdot\vec v,
\qquad
\tilde{F}\tilde{V} - \tilde{V}\tilde{F} = 2\gamma\,\tilde{F}\times\vec v.
$$

(Here $\tilde{F}\cdot\vec v$ is the scalar biquaternion $\sum_k F_k v_k$ and $\tilde{F}\times\vec v$ the pure-vector biquaternion with components $\epsilon_{jkl}F_j v_l$.) The electric and magnetic fields are recovered from

$$
\vec E = \frac{\tilde{F} + \tilde{F}^{*}}{2i\sqrt{\epsilon}},
\qquad
\vec B = \mu\vec H = \frac{\sqrt{\mu}}{2}\left(\tilde{F}^{*} - \tilde{F}\right).
$$

**Step 2: the scalar part.** The scalar part of the four-force is

$$
\operatorname{Sc}(\tilde{K}_{\mathrm{f}}) = i\,\frac{\gamma ϙ}{c}\,\vec E\cdot\vec v
= \frac{\gamma ϙ}{2c\sqrt{\epsilon}}\left(\tilde{F} + \tilde{F}^{*}\right)\cdot\vec v
= -\,\frac{ϙ}{4c\sqrt{\epsilon}}\,
\operatorname{Sc}\!\left(S + S^{*}\right),
$$

where

$$
S = \tilde{F}\tilde{V} + \tilde{V}\tilde{F}, \qquad
S^{*} = \tilde{F}^{*}\tilde{V} + \tilde{V}\tilde{F}^{*} .
$$
Here $S^{*}$ denotes the expression obtained from $S$ by the replacement $\tilde F\to\tilde F^{*}$, not the Hermitian conjugate of $S$; the two differ by a sign, since $\tilde V^{*} = -\tilde V$ gives $\left(\tilde F\tilde V+\tilde V\tilde F\right)^\dagger = -\left(\tilde F^{*}\tilde V+\tilde V\tilde F^{*}\right)$. The derivation below uses $S^{*}$ in this replacement sense throughout.

**Step 3: the vector part.** The vector part of the four-force is

$$
\operatorname{Vect}(\tilde{K}_{\mathrm{f}}) = \gamma ϙ\,\vec E + \gamma ϙ\,\vec v\times\vec B.
$$

The first term is

$$
\gamma ϙ\,\vec E = \frac{\gamma ϙ}{2i\sqrt{\epsilon}}\left(\tilde{F} + \tilde{F}^{*}\right)
= -\,\frac{ϙ}{4c\sqrt{\epsilon}}\operatorname{Vect}\!\left(S + S^{*}\right),
$$

using $\operatorname{Vect}(S + S^{*}) = 2i\gamma c\,(\tilde{F} + \tilde{F}^{*})$, and the second is

$$
\gamma ϙ\,\vec v\times\vec B
= \frac{\gamma ϙ\sqrt{\mu}}{2}\,\vec v\times\left(\tilde{F}^{*} - \tilde{F}\right)
= \frac{ϙ\sqrt{\mu}}{4}\left(A - A^\dagger\right),
$$

where

$$
A = \tilde{F}\tilde{V} - \tilde{V}\tilde{F}, \qquad
A^\dagger = \tilde{F}^{*}\tilde{V} - \tilde{V}\tilde{F}^{*} .
$$

**Step 4: collect.** Adding the scalar and vector parts gives the **master identity**

$$
\tilde{K}_{\mathrm{f}} = -\,\frac{ϙ}{4c\sqrt{\epsilon}}\left(S + S^{*}\right)
+ \frac{ϙ\sqrt{\mu}}{4}\left(A - A^\dagger\right),
$$

which, expanded in the four general products, is

$$
\boxed{\;
\tilde{K}_{\mathrm{f}} = \frac{ϙ}{4}\!\left(\sqrt{\mu} - \frac{1}{c\sqrt{\epsilon}}\right)\!\left(\tilde{F}\tilde{V} + \tilde{V}\tilde{F}^{*}\right)
- \frac{ϙ}{4}\!\left(\sqrt{\mu} + \frac{1}{c\sqrt{\epsilon}}\right)\!\left(\tilde{V}\tilde{F} + \tilde{F}^{*}\tilde{V}\right).
\;}
$$

This is the general form, valid for the symbols $c, \epsilon, \mu$ taken independently.

**Step 5: use the medium relation.** In the biquaternion framework the speed of light in the medium is not independent of the electromagnetic properties: $c = 1/\sqrt{\epsilon\mu}$. Equivalently,

$$
\frac{1}{c\sqrt{\epsilon}} = \frac{\sqrt{\epsilon\mu}}{\sqrt{\epsilon}} = \sqrt{\mu}.
$$

With this relation the coefficient of the first bracket vanishes identically, and the master identity collapses to a one-bracket formula:

$$
\boxed{\;
\tilde{K}_{\mathrm{f}} = -\,\frac{ϙ\sqrt{\mu}}{2}\left(\tilde{V}\tilde{F} + \tilde{F}^{*}\tilde{V}\right)
= -\,\frac{ϙ}{2c\sqrt{\epsilon}}\left(\tilde{V}\tilde{F} + \tilde{F}^{*}\tilde{V}\right).
\;}
$$

The two coefficients are equal, $\sqrt{\mu} = 1/(c\sqrt{\epsilon})$, so either may be used. Since $\tilde{F}^{*} = -\tilde{F}^*$, the formula may also be written

$$
\tilde{K}_{\mathrm{f}} = -\,\frac{ϙ\sqrt{\mu}}{2}\left(\tilde{V}\tilde{F} - \tilde{F}^*\tilde{V}\right).
$$

**Step 6: the projection form.** Because $\tilde{V}\in\mathbb{M}_-$ and $\tilde{V}^{*} = -\tilde{V}$, the Hermitian conjugate of the product is

$$
\left(\tilde{V}\tilde{F}\right)^\dagger = \tilde{F}^{*}\tilde{V}^{*} = -\,\tilde{F}^{*}\tilde{V}.
$$

The bracket is therefore twice the anti-Hermitian part of $\tilde{V}\tilde{F}$:

$$
\tilde{V}\tilde{F} + \tilde{F}^{*}\tilde{V}
= \tilde{V}\tilde{F} - \left(\tilde{V}\tilde{F}\right)^\dagger
= 2\,P_{\mathbb{M}_-}\!\left(\tilde{V}\tilde{F}\right),
$$

and the formula becomes the single statement

$$
\tilde{K}_{\mathrm{f}} = -\,ϙ\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{V}\tilde{F}\right),
\qquad
P_{\mathbb{M}_-}(\tilde{Q}) = \tfrac{1}{2}\left(\tilde{Q} - \tilde{Q}^{*}\right).
$$

This is the cleanest form of the result. It says that the Lorentz four-force is, up to the constant $ϙ\sqrt{\mu}$, the **projection of the product $\tilde{V}\tilde{F}$ onto the material sector** $\mathbb{M}_-$. No real part is taken, and no Clifford algebra outside $\mathbb{B}$ is needed.

**Reading by sector.** The projection form has a transparent **physical interpretation**. Split the field strength into its Hermitian and anti-Hermitian parts,

$$
\tilde{F}^{(+)} = \tfrac{1}{2}\left(\tilde{F} + \tilde{F}^{*}\right) = i\sqrt{\epsilon}\,\vec E
\;\in\;\mathbb{M}_+,
\qquad
\tilde{F}^{(-)} = \tfrac{1}{2}\left(\tilde{F} - \tilde{F}^{*}\right) = -\sqrt{\mu}\,\vec H
\;\in\;\mathbb{M}_-,
$$

the electric part in the informational (Hermitian) sector and the magnetic part in the material (anti-Hermitian) sector. Then

$$
\tilde{V}\tilde{F} + \tilde{F}^{*}\tilde{V}
= \left\{\tilde{V}, \tilde{F}^{(+)}\right\} + \left[\tilde{V}, \tilde{F}^{(-)}\right],
$$

where $\{,\}$ is the anticommutator and $[,]$ the commutator, so that

$$
\tilde{K}_{\mathrm{f}} = -\,\frac{ϙ}{2c\sqrt{\epsilon}}
\left(\left\{\tilde{V}, \tilde{F}^{(+)}\right\} + \left[\tilde{V}, \tilde{F}^{(-)}\right]\right).
$$

The electric field couples to the four-velocity through the **anticommutator**, the magnetic field through the **commutator**. This asymmetry is the algebraic origin of the different roles the two fields play in the force: the electric field does work and changes the energy, the magnetic field does not.

**Checks.** The formula is verified by direct substitution. Two special cases are instructive.

*Particle at rest.* With $\vec v = 0$ we have $\gamma = 1$ and $\tilde{V} = ic$. Then

$$
\tilde{K}_{\mathrm{f}} = -\,\frac{ϙ\sqrt{\mu}}{2}\left(ic\,\tilde{F} + \tilde{F}^{*} ic\right)
= -\,\frac{iϙ\sqrt{\mu}c}{2}\left(\tilde{F} + \tilde{F}^{*}\right)
= -\,\frac{iϙ\sqrt{\mu}c}{2}\left(2i\sqrt{\epsilon}\,\vec E\right)
= ϙ\sqrt{\mu}\,c\sqrt{\epsilon}\,\vec E = ϙ\,\vec E,
$$

since $c\sqrt{\epsilon\mu} = 1$. The scalar part vanishes, as it must for a particle at rest.

*Pure magnetic field.* With $\vec E = 0$ we have $\tilde{F}^{*} = -\tilde{F} = \sqrt{\mu}\,\vec H$, and

$$
\tilde{K}_{\mathrm{f}} = -\,\frac{ϙ\sqrt{\mu}}{2}\left(-\sqrt{\mu}\,\tilde{V}\vec H + \sqrt{\mu}\,\vec H\tilde{V}\right)
= \frac{ϙ\mu}{2}\left(\tilde{V}\vec H - \vec H\tilde{V}\right)
= ϙ\mu\,\gamma\left(\vec v\times\vec H\right)
= \gamma ϙ\left(\vec v\times\vec B\right),
$$

which is the magnetic part of the component form, with vanishing scalar part: a pure magnetic field does no work.

*General case.* For arbitrary $\vec E$, $\vec B$, $\vec v$, the identity $\tilde{K}_{\mathrm{f}} = -ϙ\sqrt{\mu}\,P_{\mathbb{M}_-}(\tilde{V}\tilde{F})$ was checked numerically against the component form at random field configurations, with agreement to machine precision (maximum discrepancy of order $10^{-15}$ relative to terms of order unity). It is an algebraic identity, not an approximation.

## The Force, the Four-Velocity, and the Four-Momentum

The product formula makes the relation between the four-force and the kinematic four-vectors of $\mathbb{M}_-$ explicit.

The four-velocity and four-momentum are

$$
\tilde{V} = \gamma\left(ic\,e_t + \vec v\right),
\qquad
\tilde{P} = m\tilde{V} = i\,\frac{E}{c}\,e_t + \vec p,
$$

with $E = \gamma mc^2$ and $\vec p = \gamma m\vec v$, and they satisfy the normalization and mass-shell conditions

$$
\tilde{V}\tilde{V}^{\natural} = -c^2,
\qquad
\tilde{P}\tilde{P}^{\natural} = -m^2c^2.
$$

The four-force is the proper-time derivative $\tilde{K}_{\mathrm{f}} = d\tilde{P}/d\tau$, and the product formula expresses it directly in terms of $\tilde{V}$ and the field:

$$
\tilde{K}_{\mathrm{f}} = -\,ϙ\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{V}\tilde{F}\right)
= -\,\frac{ϙ}{2c\sqrt{\epsilon}}\left(\tilde{V}\tilde{F} + \tilde{F}^{*}\tilde{V}\right).
$$

The four-force is thus built from the same ingredients as the four-momentum — the four-velocity and the field — and inherits its membership in $\mathbb{M}_-$ from the projection.

Three consequences follow at once.

**Orthogonality.** Differentiating the mass shell, $\frac{d}{d\tau}(\tilde{P}\tilde{P}^{\natural}) = \tilde{K}_{\mathrm{f}}\tilde{P}^{\natural} + \tilde{P}\tilde{K}_{\mathrm{f}}^{\natural} = 0$. In components this is the familiar $K^\mu P_\mu = 0$, which for the Lorentz force reads

$$
\left(i\frac{\gamma P_{\text{mech}}}{c}\right)\left(i\gamma mc\right) + \left(\gamma\vec f\right)\cdot\left(\gamma m\vec v\right)
= -\gamma^2 m\,P_{\text{mech}} + \gamma^2 m\left(\vec f\cdot\vec v\right) = 0,
$$

since $\vec f\cdot\vec v = ϙ(\vec E + \vec v\times\vec B)\cdot\vec v = ϙ\,\vec E\cdot\vec v = P_{\text{mech}}$. The cancellation is exact.

**Conservation of rest mass.** Since $\tilde{P}\tilde{P}^{\natural} = -m^2c^2$ is constant along the worldline, the rest mass is unchanged by the Lorentz force. The force can rotate the four-momentum in $\mathbb{M}_-$ but cannot change its biquaternion norm.

**The non-relativistic limit.** For $|\vec v| \ll c$ the scalar part of $\tilde{K}_{\mathrm{f}}$ is negligible relative to the vector part, and the four-force reduces to the Newtonian Lorentz force $ϙ(\vec E + \vec v\times\vec B)$.

## The Invariants of the Motion and the Field Invariants

The electromagnetic field has exactly two independent local invariants, fixed by the field-strength article:

$$
I_1 = \vec E^2 - c^2\vec B^2,
\qquad
I_2 = \vec E\cdot\vec B.
$$

They are the real and imaginary parts of the biquaternion norm of the field,

$$
\langle\tilde{F}\rangle_{\natural} = \langle\tilde{F},\tilde{F}\rangle_{\natural} = \tilde{F}\tilde{F}^{\natural} = -\epsilon\left(I_1 + 2ic\,I_2\right),
$$

and they are invariant under the proper orthochronous Lorentz group. It is natural to ask what these field invariants imply for the *motion* of a charged particle. The answer has two parts, and it is worth separating them carefully.

### The invariant of the motion

The motion's own invariant is the **mass shell**,

$$
\tilde{P}\tilde{P}^{\natural} = -m^2c^2,
$$

which, as shown above, is preserved by the Lorentz force because the force is orthogonal to the four-momentum. This invariant is independent of the field: every charged particle retains its rest mass, whatever the field. In the biquaternion framework this is the statement that the four-force lies in $\mathbb{M}_-$ and is orthogonal to $\tilde{P}$ in the biquaternion norm.

### The force's Lorentz scalar

The biquaternion norm of the four-force itself,

$$
\langle\tilde{K}_{\mathrm{f}}\rangle_{\natural} = \langle\tilde{K}_{\mathrm{f}},\tilde{K}_{\mathrm{f}}\rangle_{\natural} = \tilde{K}_{\mathrm{f}}\tilde{K}_{\mathrm{f}}^{\natural} = -\left(K^0\right)^2 + \left|\vec K\right|^2,
$$

is a Lorentz scalar; it is not conserved along the motion. Substituting the component form,

$$
\langle\tilde{K}_{\mathrm{f}}\rangle_{\natural} = \gamma^2 ϙ^2\left[\left|\vec E + \vec v\times\vec B\right|^2 - \frac{\left(\vec E\cdot\vec v\right)^2}{c^2}\right].
$$

Evaluated in the instantaneous rest frame of the particle, where $\vec v = 0$ and $\gamma = 1$, this is $ϙ^2\vec E_{\text{rest}}^2$, and since $\langle\tilde{K}_{\mathrm{f}}\rangle_{\natural}$ is a Lorentz scalar,

$$
\langle\tilde{K}_{\mathrm{f}}\rangle_{\natural} = ϙ^2\,\vec E_{\text{rest}}^2
$$

in every frame. The scalar measures the electric field in the particle's rest frame. Unlike the field invariants $I_1, I_2$, it is not determined by the field alone, because the rest frame depends on the particle's velocity.

### The field invariants classify the force

The invariants $I_1, I_2$ determine the Lorentz type of the field, and therefore the possible shapes of the force. The classification, established in the field-strength article, is the following.

- **Null field** ($I_1 = I_2 = 0$). Then $\vec E\perp\vec B$ and $|\vec E| = c|\vec B|$ pointwise, and no Lorentz transformation can remove either field. The field is radiative. The biquaternion norm of the field vanishes, and $\tilde{F}$ is a zero divisor of $\mathbb{B}$.
- **Electric type** ($I_2 = 0$, $I_1 > 0$). Then there is a frame in which $\vec B = 0$, with $\vec E^2 = I_1$. In that frame the four-force is $\tilde{K}_{\mathrm{f}} = i\gamma ϙ(\vec E\cdot\vec v)/c\,e_t + \gamma ϙ\,\vec E$: purely electric.
- **Magnetic type** ($I_2 = 0$, $I_1 < 0$). Then there is a frame in which $\vec E = 0$, with $c^2\vec B^2 = -I_1$. In that frame the four-force is $\tilde{K}_{\mathrm{f}} = \gamma ϙ(\vec v\times\vec B)$: purely magnetic, and no work is done.
- **Generic field** ($I_2 \neq 0$). Then no frame removes either field, but there is a frame in which $\vec E$ and $\vec B$ are parallel, with magnitudes determined by the two invariants through

$$
E_0^2 = \frac{I_1 + \sqrt{I_1^2 + 4c^2I_2^2}}{2},
\qquad
B_0 = \frac{I_2}{E_0}.
$$

The invariants do not determine the force, because the force also depends on the particle velocity; what they determine is the *type* of field, and hence the family of forces the field can exert. In the frames just listed the force takes its simplest form: electric in the electric frame, magnetic in the magnetic frame, and dominated by the parallel electric and magnetic fields in the generic frame.

### The characteristic rates of the motion

There is one further sense in which the field invariants govern the motion, and it is the sharpest one. For a particle in a **uniform** field the equation of motion is linear,

$$
\frac{dP^\mu}{d\tau} = \frac{ϙ}{m}\,F^{\mu}{}_{\nu}P^\nu,
$$

so the proper-time motion is a superposition of exponentials whose rates are $(ϙ/m)$ times the eigenvalues of the field matrix $F^{\mu}{}_{\nu}$. In the $ict$ convention those eigenvalues are determined by the two invariants: the characteristic polynomial is

$$
\det\!\left(\lambda\,\mathbb{1} - F\right)
= \lambda^4 - \frac{I_1}{c^2}\,\lambda^2 - \frac{I_2^2}{c^2},
$$

so the eigenvalues are $\pm\lambda_+,\pm\lambda_-$ with

$$
\lambda_\pm^2 = \frac{I_1 \pm \sqrt{I_1^2 + 4c^2I_2^2}}{2c^2}.
$$

In the frame in which $\vec E$ and $\vec B$ are parallel these reduce to $\lambda = \pm E_0/c$ and $\lambda = \pm iB_0$. Two familiar cases are immediate. A pure magnetic field ($I_1 < 0$, $I_2 = 0$, frame with $\vec E = 0$) gives eigenvalues $\pm iB$ and the cyclotron frequency $\omega = ϙB/m$: uniform circular motion, with constant energy. A pure electric field ($I_2 = 0$, $I_1 > 0$, frame with $\vec B = 0$) gives eigenvalues $\pm E/c$ and hyperbolic (uniformly accelerated) motion. The field invariants, not the field components, are the Lorentz-invariant data that fix these rates.

### A null-field invariant

One genuine extra invariant of the motion exists in the null case. A null field is radiative: its field matrix has a null eigenvector $k$ (the propagation direction), satisfying $k_\mu F^{\mu}{}_{\nu} = 0$. Then

$$
\frac{d}{d\tau}\left(k\cdot P\right)
= k_\mu\,\frac{dP^\mu}{d\tau}
= \frac{ϙ}{m}\,k_\mu F^{\mu}{}_{\nu}P^\nu = 0,
$$

so $k\cdot P$ is constant along the worldline. This is the invariant of the motion associated with the degenerate (radiative) type of the field, and it exists precisely when $I_1 = I_2 = 0$. For non-null fields the mass shell is the only invariant of this simple kind.

## The Transformation of the Force under Boosts

Because the four-force is a four-vector, it transforms under the Lorentz group by the same **rotor conjugation** as every other element of $\mathbb{M}_-$:

$$
\tilde{K}_{\mathrm{f}}' = \tilde U\,\tilde{K}_{\mathrm{f}}\,\tilde U^{*},
$$

where $\tilde U$ is the unit-norm biquaternion of the boost, and $\tilde{K}_{\mathrm{f}}' = d\tilde{P}'/d\tau$ is the force measured in the boosted frame (the proper time is invariant). This is the statement that the force transforms in the **vector representation** of the Lorentz group.

For a pure boost with velocity $\vec v_b$ — a frame boost, distinct from the particle velocity $\vec v$ — the boost biquaternion is

$$
\tilde U = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\vec u,
\qquad
\tanh\psi = \frac{v_b}{c},
\qquad
\gamma_b = \cosh\psi = \frac{1}{\sqrt{1 - \vec v_b^2/c^2}},
$$

an element of $\mathbb{M}_+$ (Hermitian, unit norm). The rotor conjugation then reproduces the standard component transformation

$$
K'^0 = \gamma_b\left(K^0 - i\,\frac{\vec v_b\cdot\vec K}{c}\right),
$$

$$
\vec K' = \vec K + \frac{\gamma_b - 1}{v_b^2}\left(\vec v_b\cdot\vec K\right)\vec v_b - \gamma_b\,\frac{K^0}{c}\,\vec v_b.
$$

Written in the biquaternion variables, with $\tilde{K}_{\mathrm{f}} = K^0e_t + \vec K$ and $\tilde{K}_{\mathrm{f}}' = K'^0e_t + \vec K'$, these are exactly the components of $\tilde U\tilde{K}_{\mathrm{f}}\tilde U^{*}$. The verification is direct: the rotor conjugation and the component formulas agree to machine precision at random boosts and random forces (maximum discrepancy of order $10^{-15}$).

**How the field transforms.** The field strength is *not* a four-vector, and it does not transform like one. Under the same boost it transforms in the rank-two (bivector) representation,

$$
\tilde{F}' = \tilde U^{\natural}\,\tilde{F}\,\tilde U,
$$

with $\tilde U^{\natural}$ the quaternion conjugate of the rotor (equivalently $\tilde U^{-1}$ for a unit-norm rotor). This reproduces the standard field transformation

$$
\vec E' = \gamma_b\left(\vec E + \vec v_b\times\vec B\right) - \frac{\gamma_b - 1}{v_b^2}\left(\vec v_b\cdot\vec E\right)\vec v_b,
$$

$$
\vec B' = \gamma_b\left(\vec B - \frac{1}{c^2}\,\vec v_b\times\vec E\right) - \frac{\gamma_b - 1}{v_b^2}\left(\vec v_b\cdot\vec B\right)\vec v_b,
$$

and it is this bivector rule — not the vector rule — that leaves the field invariants $I_1$ and $I_2$ unchanged. The distinction between the vector and bivector transformation laws is the algebraic expression of the fact that four-vectors live in $\mathbb{M}_-$ while the field strength does not.

**Covariance of the product formula.** The product formula is manifestly covariant under pure boosts, in the following precise sense. Apply the vector rule to the four-velocity, $\tilde{V}' = \tilde U\tilde{V}\tilde U^{*}$, and the bivector rule to the field, $\tilde{F}' = \tilde U^{\natural}\tilde{F}\tilde U$. Then the right-hand side of the product formula transforms into the right-hand side computed with the primed fields, and equals $\tilde U\tilde{K}_{\mathrm{f}}\tilde U^{*}$:

$$
-ϙ\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{V}'\tilde{F}'\right)
= \tilde U\left[-ϙ\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{V}\tilde{F}\right)\right]\tilde U^{*}
= \tilde{K}_{\mathrm{f}}'.
$$

In this sense the product formula is not merely a frame-dependent identity but a covariant statement: transforming the ingredients and transforming the result give the same answer.

## The Power–Force Density Biquaternion and Its Four-Term Split

The four-force $\tilde{K}_{\mathrm{f}}$ of this article acts on a single charged particle. The companion programme of *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis* works instead at the level of **densities**, and its force object is a different biquaternion — worth recording here because it is the density counterpart of the same product $\tilde{V}\tilde{F}$, and because its structure is what the programme's Newton-law analogues are built on.

Let a field's **charge–current biquaternion** be

$$
\tilde J_{\mathrm{eg}} = i\rho + \vec J,
\qquad
\rho = \frac{\rho_E}{\sqrt{\epsilon}} - i\,\frac{\rho_H}{\sqrt{\mu}},
\qquad
\vec J = \sqrt{\mu}\,\vec j_E - i\sqrt{\epsilon}\,\vec j_H,
$$

where $\rho_E = \mathrm{div}\,\vec D$ and $\rho_H = -\mathrm{div}\,\vec B$ are the electric and magnetic charge densities, $\vec j_E$ and $\vec j_H$ the corresponding currents, $\vec D = \epsilon\vec E$, and $\vec B = \mu\vec H$. Let a second field have field strength

$$
\tilde F' = i\sqrt{\epsilon}\,\vec E' - \sqrt{\mu}\,\vec H',
$$

the field strength of *The Magnetic-Charge–Mass Hypothesis*, in that article's sign convention. The programme's **power–force biquaternion** is the product

$$
\tilde{\mathcal F} = i\,\tilde J_{\mathrm{eg}}\circ\tilde F' .
$$

Its scalar and vector parts were recomputed here and are

$$
\mathrm{Sc}\big(\tilde{\mathcal F}\big)
= \frac{1}{c}\left(\vec E'\cdot\vec j_E + \vec H'\cdot\vec j_H\right)
+ i\left(\vec B'\cdot\vec j_E - \vec D'\cdot\vec j_H\right),
\qquad
\mathrm{Vect}\big(\tilde{\mathcal F}\big) = -\,\rho\,\tilde F' - i\,\big[\tilde F',\vec J\big],
$$

where $(\cdot,\cdot)$ is the general plain bilinear form $\sum_k F_kG_k$. The scalar part is a **power density**: its real part is the rate at which the electric and gravimagnetic fields do work on their currents, and its imaginary part is the corresponding magnetic-charge quantity.

The vector part is the **force density**, and its relation to the two halves named below carries a factor of $i$:

$$
\mathrm{Vect}\big(\tilde{\mathcal F}\big) = -\,i\left(\vec F_H + i\,\vec F_E\right),
\qquad
\vec F_H + i\,\vec F_E = i\,\mathrm{Vect}\big(\tilde{\mathcal F}\big)
= -\,i\rho\,\tilde F' - \vec J\times\tilde F' ,
$$

so that $\vec F_E = \mathrm{Re}\,\mathrm{Vect}(\tilde{\mathcal F})$ and $\vec F_H = -\mathrm{Im}\,\mathrm{Vect}(\tilde{\mathcal F})$. Expanding with the definitions above gives the four terms of the first half with their coefficients,

$$
\vec F_H = \rho_E\,\vec E' + \rho_H\,\vec H' + \vec j_E\times\vec B' - \vec j_H\times\vec D' .
$$

The four terms are a **Coulomb** term from the electric charge density, a **gravitational** term from the mass (magnetic-charge) density, a **Lorentz** term from the electric current crossed with the magnetic induction, and a fourth term built from the electric displacement and the mass current, which the author names the **electromass force**. The second half, the force that changes the electric currents, is

$$
\vec F_E = c\,\rho_E\,\vec B' - c\,\rho_H\,\vec D' + \frac{1}{c}\,\vec E'\times\vec j_E + \frac{1}{c}\,\vec H'\times\vec j_H .
$$

The density $\tilde{\mathcal F}$ is not the per-particle $\tilde{K}_{\mathrm{f}}$ and the two must not be identified: $\tilde{K}_{\mathrm{f}}$ is the four-force on one charge, $\tilde{\mathcal F}$ is a force per unit volume on a continuous distribution, and only the latter carries the power–force pairing in one element.

**Status.** The object, the split and the coefficients above are algebra, and all were verified numerically: the scalar part against its component form, and both halves of the force against the direct expansion, with residuals at machine precision. The coefficients were previously withheld here because the source's own expansions of the two halves did not close against the vector part as it stands; the reconciliation is the factor of $i$ displayed above, which the source suppresses. Reading $\vec F_H$ as the real part of the vector part rather than as $-\mathrm{Im}$ of it produces the apparent mismatch; with the factor placed correctly the source's two expansions close term by term. One exception remains: the source prints $-\rho_H\vec D'$ where the derivation gives $-c\,\rho_H\vec D'$, a factor of the dimensionless speed of light in that single term, and the derived form is the one carried above. The coefficient-level expansion is hypothesis-dependent through the magnetic-charge–mass identification, so the individual terms remain the programme's rather than the corpus's; what the corpus certifies is that they are what the programme's own product yields. The programme's third-law relation, $\tilde J_{\mathrm{eg}}\circ\tilde F' = -\tilde J_{\mathrm{eg}}'\circ\tilde F$, is the statement that the two power densities are equal, and the author compares it to Betti's reciprocity identity; that comparison, and the hypothesis, are the programme's, not the corpus's. See *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis* for the provenance.


## The Lamb-Vector Reading of the Force Law

The force law of this article is a relativistic fact: $\vec f = ϙ(\vec E+\vec v\times\vec B)$ is what the field does to a charge, and the derivation above takes that law as given. A second interpretation of its *form* comes from fluid mechanics, and it belongs next to the first, because the corpus's magnetic-field material explains magnetism as a relativistic effect of the electric field, while the hydrodynamic correspondence offers an independent interpretation in which magnetism is vorticity.

The bridge is the **Lamb vector** $\vec\ell = \vec\omega\times\vec v_b$ of a fluid of velocity $\vec v_b$ and vorticity $\vec\omega = \nabla\times\vec v_b$, introduced in *Maxwell's Equations in the Biquaternionic Formulation*. It is bilinear in a velocity and a curl, and it is the pairing of a flow with its own rotation. The magnetic term of the Lorentz force density, $\vec j\times\vec B$, is bilinear in a current and a curl, and the electric term $\rho_E\vec E$ pairs a charge density with the irrotational part of the field. Under the dictionary

$$
\vec v_b\;\leftrightarrow\;\vec A,
\qquad
\vec\omega\;\leftrightarrow\;\vec B,
\qquad
\vec\ell\;\leftrightarrow\;\vec E
$$

the Lorentz force density has the same form as the Lamb force density $\rho\,\vec\ell$: in each case a source is paired with a quantity that is bilinear in a velocity-like field and its curl. The correspondence is attributed to H. Marmanis.

Two things must be kept apart in using it. First, it is a *formal* correspondence between the equations of two theories, with the limits stated in the Maxwell article; it is not a derivation of the force law, and the relativistic account of magnetism remains the standard one. Second, it lives in three-vector language and is not a biquaternion formula. It is recorded here because it supplies a second *why* for the shape of the force law, alongside the relativistic one, and not because it competes with the product formula of this article, which remains the biquaternionic statement.

## Summary

The Lorentz four-force has the component form

$$
\tilde{K}_{\mathrm{f}} = i\,\frac{\gamma ϙ}{c}\left(\vec E\cdot\vec v\right)e_t + \gamma ϙ\left(\vec E + \vec v\times\vec B\right),
$$

which is the contraction $K^\mu = ϙF^{\mu\nu}v_\nu$ written in the biquaternion basis, and it lies in the anti-Hermitian subspace $\mathbb{M}_-$. Its expression as a biquaternion product of the field strength and the four-velocity is not the real part of $\tilde{F}\tilde{V}$ — that object has the wrong reality structure and lies outside $\mathbb{M}_-$ — but the anti-Hermitian projection of $\tilde{V}\tilde{F}$:

$$
\boxed{\;\tilde{K}_{\mathrm{f}} = -\,ϙ\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{V}\tilde{F}\right)
= -\,\frac{ϙ\sqrt{\mu}}{2}\left(\tilde{V}\tilde{F} + \tilde{F}^{*}\tilde{V}\right).\;}
$$

Equivalently, $\tilde{K}_{\mathrm{f}} = -\frac{ϙ}{2c\sqrt{\epsilon}}(\tilde{V}\tilde{F} + \tilde{F}^{*}\tilde{V})$, since $\sqrt{\mu} = 1/(c\sqrt{\epsilon})$; and since $\tilde{F}^{*} = -\tilde{F}^*$, the formula may be written $-\frac{ϙ\sqrt{\mu}}{2}(\tilde{V}\tilde{F} - \tilde{F}^*\tilde{V})$. The conjugate field is essential: it carries the anti-self-dual half of the field tensor, and the electric and magnetic contributions can be separated only by combining the two halves. This resolves the open question recorded in the relativistic-mechanics article, and fixes the force notation: the four-force is written $\tilde{K}_{\mathrm{f}}$, while $\tilde{F}$ is reserved for the field strength.

The structural consequences are these. The four-force is orthogonal to the four-momentum, $\tilde{K}_{\mathrm{f}}\tilde{P}^{\natural} + \tilde{P}\tilde{K}_{\mathrm{f}}^{\natural} = 0$, so the mass shell $\tilde{P}\tilde{P}^{\natural} = -m^2c^2$ is preserved and the rest mass is unchanged by the Lorentz force. The force's biquaternion norm $\langle\tilde{K}_{\mathrm{f}}\rangle_{\natural}$ is a Lorentz scalar equal to $ϙ^2\vec E_{\text{rest}}^2$, the squared electric field in the particle's rest frame. The field invariants $I_1 = \vec E^2 - c^2\vec B^2$ and $I_2 = \vec E\cdot\vec B$ classify the field as null, electric, magnetic, or generic, and thereby fix the simplest possible shape of the force and, for a uniform field, the characteristic rates of the motion: the eigenvalues of the field matrix solve $\lambda^4 - (I_1/c^2)\lambda^2 - I_2^2/c^2 = 0$. In the null case a null eigenvector $k$ of the field matrix gives one further invariant of the motion, $k\cdot P$. Finally, under boosts the four-force transforms in the vector representation, $\tilde{K}_{\mathrm{f}}' = \tilde U\tilde{K}_{\mathrm{f}}\tilde U^{*}$, while the field transforms in the bivector representation, $\tilde{F}' = \tilde U^{\natural}\tilde{F}\tilde U$, and the product formula is covariant under the pair.

At the level of densities the companion programme replaces the per-particle force by the power–force biquaternion $\tilde{\mathcal F} = i\tilde J_{\mathrm{eg}}\circ\tilde F'$, whose scalar part is a power density and whose vector part splits into a Coulomb, a gravitational, a Lorentz and an electromass term; it is the density counterpart of the same product, with the per-particle $\tilde{K}_{\mathrm{f}}$ and the per-volume $\tilde{\mathcal F}$ kept strictly apart.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\tilde{Q}^{*} = \bar{X}^{\,*}$ | Hermitian conjugate |
| $\tilde{Q}^*$, $\bar{X}$ | Complex conjugate, quaternion conjugate |
| $P_{\mathbb{M}_-}(\tilde{Q}) = \tfrac12(\tilde{Q} - \tilde{Q}^{*})$ | Projection onto $\mathbb{M}_-$ (anti-Hermitian part) |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion (pure vector) |
| $\tilde{F}^{*} = i\sqrt{\epsilon}\,\vec E + \sqrt{\mu}\,\vec H$ | Hermitian conjugate of the field strength |
| $\vec E, \vec H, \vec B = \mu\vec H$ | Electric field, magnetic field, magnetic induction |
| $\epsilon, \mu$ | Permittivity and permeability of the medium |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $ϙ$ | Particle charge |
| $\vec v$ | Particle three-velocity |
| $\vec v_b$ | Frame (boost) three-velocity |
| $\gamma = 1/\sqrt{1-\vec v^2/c^2}$ | Lorentz factor of the particle |
| $\gamma_b = 1/\sqrt{1-\vec v_b^2/c^2}$ | Lorentz factor of the boost |
| $\tau$ | Proper time |
| $\tilde{V} = \gamma(ic\,e_t + \vec v)$ | Four-velocity biquaternion |
| $\tilde{P} = m\tilde{V}$ | Four-momentum biquaternion |
| $\tilde{K}_{\mathrm{f}} = d\tilde{P}/d\tau$ | Four-force (Minkowski force) biquaternion |
| $\tilde J_{\mathrm{eg}} = i\rho + \vec J$ | Charge–current biquaternion of a field |
| $\tilde{\mathcal F} = i\tilde J_{\mathrm{eg}}\circ\tilde F'$ | Power–force density biquaternion (per unit volume; not $\tilde{K}_{\mathrm{f}}$) |
| $\rho_E, \rho_H$, $\vec j_E, \vec j_H$ | Electric and magnetic charge and current densities |
| $\vec D = \epsilon\vec E$, $\vec B = \mu\vec H$ | Electric displacement and magnetic induction |
| $\vec f = ϙ(\vec E + \vec v\times\vec B)$ | Relativistic three-force |
| $P_{\text{mech}} = ϙ\,\vec E\cdot\vec v$ | Mechanical power |
| $I_1 = \vec E^2 - c^2\vec B^2$ | First field invariant |
| $I_2 = \vec E\cdot\vec B$ | Second field invariant |
| $\tilde U = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\vec u$ | Boost biquaternion (Hermitian, unit norm) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the covariant Lorentz force, the field invariants, and the motion in a uniform field.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard four-vector formulation of the Lorentz force and its transformation under boosts.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the contraction $f = ϙ\,F\cdot u$ of a bivector with a vector in spacetime algebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of Lorentz transformations and the bivector treatment of the electromagnetic field.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even subalgebra of $\mathrm{Cl}_{1,3}$ and for the self-dual and anti-self-dual decomposition of the field tensor.
- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* 22 (1907) 579–586, for the complex-vector formulation of the electromagnetic field.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for the complex-vector and duality structure of electromagnetism.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for a biquaternionic treatment of the electromagnetic field and the Lorentz force.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation of the field equations.
- L. A. Alexeyeva, "One Biquaternion Model of the Electro-Gravimagnetic Field. Field Analogues of Newton's Laws" (2007), for the density-level power–force biquaternion, the four-term force split and the electromass force; see *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis* for the hypothesis and its status.
- L. A. Alexeyeva, "Newton's Laws for a Biquaternionic Model of the Electro-Gravimagnetic Field, Charges, Currents, and Their Interactions" (2009), for the revision of the programme, in which the charge–current conservation law is not Lorentz invariant under interaction and a scalar resistance field is added.
- G. Rousseaux and É. Guyon, "À propos d'une analogie entre la mécanique des fluides et l'électromagnétisme", *Bulletin de l'Union des Physiciens* **96** (2002), no. 841 (2), 125–134, for the Lamb-vector interpretation of the force law in *The Lamb-Vector Reading of the Force Law* — the hydrodynamic form of the Lorentz force density, attributed by the source to H. Marmanis. An expository article in a teachers' journal, in French; the dictionary and its limits are stated in *Maxwell's Equations in the Biquaternionic Formulation*.
