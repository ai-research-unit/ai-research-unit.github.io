# __The Lorentz Force in Biquaternion Form__

## Introduction

A charged particle moving in an electromagnetic field is acted on by the **Lorentz force**. In the four-dimensional language of relativity this force is the contraction of the field-strength tensor with the four-velocity, $K^\mu = q\,F^{\mu\nu}u_\nu$; in three-vector language it reads $q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ for the spatial part, together with the power $q\,\mathbf{E}\cdot\mathbf{v}$ in the time part. The companion article *Relativistic Mechanics in Biquaternionic Form* recorded the biquaternion component form of this four-force and identified it as an element of the anti-Hermitian subspace $\mathbb{M}_-$. That article also recorded, explicitly and twice, an open problem: the expression of the same four-force as a **biquaternion product** of the field-strength biquaternion $\tilde{F}$ and the four-velocity $\tilde{U}$ is *not* simply the real part of $\tilde{F}\circ\tilde{U}$, the correct expression "involves the representation theory of $\mathbb{B}$ in the even subalgebra of $\mathrm{Cl}_{1,3}$", and it "remains to be worked out cleanly".

This article carries out that work. The result is a two-term product formula, bilinear in the field and the four-velocity, that reproduces the component form exactly. In its most compact shape the formula is a single projection:

$$
\boxed{\;\tilde{K} = -\,q\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{U}\,\tilde{F}\right),\qquad
P_{\mathbb{M}_-}(X) = \tfrac{1}{2}\left(X - X^\dagger\right).\;}
$$

The projection $P_{\mathbb{M}_-}$ is the anti-Hermitian part, and it lands in the material sector $\mathbb{M}_-$ automatically. Written out, the formula is

$$
\tilde{K} = -\,\frac{q\sqrt{\mu}}{2}\left(\tilde{U}\,\tilde{F} + \tilde{F}^\dagger\,\tilde{U}\right),
$$

or, since $\tilde{F}^\dagger = -\tilde{F}^*$,

$$
\tilde{K} = -\,\frac{q\sqrt{\mu}}{2}\left(\tilde{U}\,\tilde{F} - \tilde{F}^*\,\tilde{U}\right).
$$

Here $\tilde{F}^\dagger$ is the Hermitian conjugate of the field strength and $\tilde{F}^*$ its complex conjugate. The appearance of the conjugate field is not a technicality: $\tilde{F}$ and $\tilde{F}^\dagger$ are (up to constant factors) the self-dual and anti-self-dual halves of the field tensor, and the formula pairs the four-velocity with both halves. This is the sense in which the result "involves the representation theory of $\mathbb{B}$" — but, as the derivation below shows, the formula itself lives entirely inside $\mathbb{B}$ and needs no Clifford algebra beyond the identification $\mathbb{B}\cong\mathbb{C}\ell_{1,3}^{+}$.

**A note on notation.** The companion article *The Field-Strength Biquaternion and Its Invariants* fixes the symbol $\tilde{F}$ for the field-strength biquaternion "once and for all". The companion article *Relativistic Mechanics in Biquaternionic Form* instead used $\tilde{F}$ for the four-force and wrote $\tilde{F}_{\text{EM}}$ for the field. To remove the collision this article adopts, and recommends for the corpus, the letter $\tilde{K}$ for the **four-force biquaternion** (the Minkowski force), reserving $\tilde{F}$ for the field strength. Thus

$$
\tilde{K} = \frac{d\tilde{P}}{d\tau}, \qquad \tilde{P} = m\tilde{U},
$$

and the field strength keeps the canonical form $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ of the field-strength article.

The conventions are those of the read-list articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and the scalar imaginary is $i$ (central, $i^2 = -1$). The conjugate of a biquaternion $X = X_0e_0 + X_1e_1 + X_2e_2 + X_3e_3$ is $\bar{X} = X_0e_0 - \mathbf{X}$, its complex conjugate is $X^* = \sum_\mu X_\mu^* e_\mu$, and its Hermitian conjugate is $X^\dagger = \bar{X}^{\,*} = \sum_\mu X_\mu^* e_\mu$ with the vector components negated. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium, $\mathbf{v}$ is the particle velocity, $\mathbf{u}$ is a frame (boost) velocity, and $\mathbf{B} = \mu\mathbf{H}$ is the magnetic induction.

## The Lorentz Four-Force in Component Form

The component form is the established result, and it is the starting point of everything that follows. For a particle of charge $q$ and velocity $\mathbf{v}$ in fields $\mathbf{E}$ and $\mathbf{B}$, the **Lorentz four-force biquaternion** is

$$
\tilde{K} = i\,\frac{\gamma q}{c}\left(\mathbf{E}\cdot\mathbf{v}\right)e_0 + \gamma q\left(\mathbf{E} + \mathbf{v}\times\mathbf{B}\right),
$$

where

$$
\gamma = \frac{1}{\sqrt{1 - \mathbf{v}^2/c^2}}
$$

is the Lorentz factor. The scalar part is purely imaginary and the vector part is real, so $\tilde{K}$ lies in the anti-Hermitian subspace $\mathbb{M}_-$, like the four-velocity $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ and the four-momentum $\tilde{P} = m\tilde{U}$. Writing $\mathbf{f} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ for the (relativistic) three-force and $P_{\text{mech}} = \mathbf{f}\cdot\mathbf{v} = q\,\mathbf{E}\cdot\mathbf{v}$ for the mechanical power, the component form reads

$$
\tilde{K} = i\,\frac{\gamma P_{\text{mech}}}{c}\,e_0 + \gamma\,\mathbf{f}.
$$

This is the biquaternion transcription of the Minkowski force $K^\mu = (i\gamma P_{\text{mech}}/c,\ \gamma\mathbf{f})$ in the $ict$ convention, so the coefficient of $e_0$ is the $ict$ time component $K^0$.

**Origin in the field tensor.** The component form is the contraction $K^\mu = q\,F^{\mu\nu}u_\nu$. In the $ict$ convention the metric is Euclidean, so indices are raised and lowered trivially and $u_\nu = u^\nu = (i\gamma c,\ \gamma\mathbf{v})$. The field tensor is the one fixed by the field-strength article,

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
K^0 = q\,F^{0k}u_k = q\,\frac{iE_k}{c}\,\gamma v_k = i\,\frac{\gamma q}{c}\,\mathbf{E}\cdot\mathbf{v},
$$

and the spatial components are

$$
K^k = q\,F^{k0}u_0 + q\,F^{kj}u_j
= q\left(-\frac{iE_k}{c}\right)(i\gamma c) + q\,\epsilon_{kjl}B_l\,\gamma v_j
= \gamma q\,E_k + \gamma q\left(\mathbf{v}\times\mathbf{B}\right)_k,
$$

which is exactly the vector part above. The component form and the tensor contraction are the same statement.

## The Four-Force as an Element of $\mathbb{M}_-$

The four-force is a four-vector, and it lives in the same subspace as the four-velocity and the four-momentum. Two structural facts make this precise.

**1. Anti-Hermiticity.** Because the scalar part of $\tilde{K}$ is purely imaginary and its vector part is real, it satisfies

$$
\tilde{K}^\dagger = -\tilde{K}.
$$

This is the defining property of $\mathbb{M}_-$. Equivalently, $\tilde{K}$ has no Hermitian part:

$$
\tfrac{1}{2}\left(\tilde{K} + \tilde{K}^\dagger\right) = 0.
$$

The whole content of the four-force is in its anti-Hermitian half. The same is true of $\tilde{U}$ and $\tilde{P}$, and this is why $\mathbb{M}_-$ is called the material sector: it is the subspace of four-vectors.

**2. Orthogonality to the four-momentum.** The four-momentum has fixed norm form, $\tilde{P}\bar{\tilde{P}} = -m^2c^2$, along the worldline. Differentiating and using $\tilde{K} = d\tilde{P}/d\tau$ gives

$$
\tilde{K}\bar{\tilde{P}} + \tilde{P}\bar{\tilde{K}} = 0,
$$

the biquaternion form of the Minkowski orthogonality $K^\mu P_\mu = 0$. The four-force changes the direction of the four-momentum but not its norm. This is examined further in the section on invariants.

## The Product Problem

The natural first guess is that the four-force is obtained by multiplying the field strength by the four-velocity and taking a real or imaginary part, in analogy with the way the field energy is obtained from $\tilde{F}\tilde{F}^\dagger$. That guess fails, and it is worth seeing exactly why, because the failure dictates the shape of the correct formula.

The field strength is a pure-vector biquaternion, $\tilde{F} = \mathbf{F}$ with $\mathbf{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$, so its quaternion conjugate is $\bar{\tilde{F}} = -\tilde{F}$. For a pure vector $\mathbf{a}$ and the four-velocity $\tilde{U} = i\gamma c + \gamma\mathbf{v}$, the quaternion product rule $\mathbf{a}\mathbf{b} = -\mathbf{a}\cdot\mathbf{b} + \mathbf{a}\times\mathbf{b}$ gives

$$
\tilde{F}\tilde{U} = i\gamma c\,\tilde{F} - \gamma\left(\tilde{F}\cdot\mathbf{v}\right) + \gamma\left(\tilde{F}\times\mathbf{v}\right),
\qquad
\tilde{U}\tilde{F} = i\gamma c\,\tilde{F} - \gamma\left(\tilde{F}\cdot\mathbf{v}\right) - \gamma\left(\tilde{F}\times\mathbf{v}\right),
$$

so that

$$
\tilde{F}\tilde{U} + \tilde{U}\tilde{F} = 2i\gamma c\,\tilde{F} - 2\gamma\left(\tilde{F}\cdot\mathbf{v}\right),
\qquad
\tilde{F}\tilde{U} - \tilde{U}\tilde{F} = 2\gamma\left(\tilde{F}\times\mathbf{v}\right).
$$

The product $\tilde{F}\tilde{U}$ has scalar part $-\gamma\,\tilde{F}\cdot\mathbf{v}$, which is a **complex** number in general, and vector part $i\gamma c\,\tilde{F} + \gamma\,\tilde{F}\times\mathbf{v}$. Its real part therefore has a **real** scalar part, whereas the four-force has a **purely imaginary** scalar part. Consequently $\operatorname{Re}(\tilde{F}\tilde{U})$ does not lie in $\mathbb{M}_-$ at all: it cannot be the four-force, for the elementary reason that it is the wrong kind of biquaternion. This is the precise content of the statement in the relativistic-mechanics article that the four-force is "not simply the real part of $\tilde{F}\circ\tilde{U}$".

There is a second obstruction. The field strength mixes $\mathbf{E}$ and $\mathbf{B}$ with the fixed weights $\sqrt{\epsilon}$, $\sqrt{\mu}$ and with opposite reality properties — the electric part imaginary, the magnetic part real — whereas the four-force requires $\mathbf{E}$ and the magnetic force $\mathbf{v}\times\mathbf{B}$ to enter with the *same* coefficient $\gamma q$. A single product of $\tilde{F}$ with $\tilde{U}$ keeps these weights locked together. Separating them requires the conjugate field $\tilde{F}^\dagger$, in which the relative sign of the electric and magnetic parts is reversed:

$$
\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H},
\qquad
\tilde{F}^\dagger = i\sqrt{\epsilon}\,\mathbf{E} + \sqrt{\mu}\,\mathbf{H}.
$$

The combination that extracts $\mathbf{E}$ is $\tilde{F} + \tilde{F}^\dagger = 2i\sqrt{\epsilon}\,\mathbf{E}$; the combination that extracts $\mathbf{B}$ is $\tilde{F}^\dagger - \tilde{F} = 2\sqrt{\mu}\,\mathbf{H} = 2\mathbf{B}/\sqrt{\mu}$. So the correct product formula must involve both $\tilde{F}$ and $\tilde{F}^\dagger$. This is the technical reason the earlier article anticipated "the representation theory of $\mathbb{B}$ in the even subalgebra of $\mathrm{Cl}_{1,3}$": the two objects $\tilde{F}$ and $\tilde{F}^\dagger$ are the self-dual and anti-self-dual halves of the field tensor, and the Lorentz force pairs the four-velocity with both.

## The Biquaternion Product Formula

We now derive the formula. The derivation is elementary: invert the product identities above to obtain the electric and magnetic fields in terms of the symmetrized and antisymmetrized products of $\tilde{F}$ and $\tilde{U}$, substitute into the component form, and collect terms.

**Step 1: the fields from the products.** From the identities of the previous section, and the same identities with $\tilde{F}$ replaced by $\tilde{F}^\dagger$,

$$
\operatorname{Sc}\!\left(\tilde{F}\tilde{U} + \tilde{U}\tilde{F}\right) = -2\gamma\,\tilde{F}\cdot\mathbf{v},
\qquad
\tilde{F}\tilde{U} - \tilde{U}\tilde{F} = 2\gamma\,\tilde{F}\times\mathbf{v}.
$$

(Here $\tilde{F}\cdot\mathbf{v}$ is the scalar biquaternion $\sum_k F_k v_k$ and $\tilde{F}\times\mathbf{v}$ the pure-vector biquaternion with components $\epsilon_{jkl}F_j v_l$.) The electric and magnetic fields are recovered from

$$
\mathbf{E} = \frac{\tilde{F} + \tilde{F}^\dagger}{2i\sqrt{\epsilon}},
\qquad
\mathbf{B} = \mu\mathbf{H} = \frac{\sqrt{\mu}}{2}\left(\tilde{F}^\dagger - \tilde{F}\right).
$$

**Step 2: the scalar part.** The scalar part of the four-force is

$$
\operatorname{Sc}(\tilde{K}) = i\,\frac{\gamma q}{c}\,\mathbf{E}\cdot\mathbf{v}
= \frac{\gamma q}{2c\sqrt{\epsilon}}\left(\tilde{F} + \tilde{F}^\dagger\right)\cdot\mathbf{v}
= -\,\frac{q}{4c\sqrt{\epsilon}}\,
\operatorname{Sc}\!\left(S + S^\dagger\right),
$$

where

$$
S = \tilde{F}\tilde{U} + \tilde{U}\tilde{F}, \qquad
S^\dagger = \tilde{F}^\dagger\tilde{U} + \tilde{U}\tilde{F}^\dagger .
$$
Here $S^\dagger$ denotes the expression obtained from $S$ by the replacement $\tilde F\to\tilde F^\dagger$, not the Hermitian conjugate of $S$; the two differ by a sign, since $\tilde U^\dagger = -\tilde U$ gives $\left(\tilde F\tilde U+\tilde U\tilde F\right)^\dagger = -\left(\tilde F^\dagger\tilde U+\tilde U\tilde F^\dagger\right)$. The derivation below uses $S^\dagger$ in this replacement sense throughout.

**Step 3: the vector part.** The vector part of the four-force is

$$
\operatorname{Vect}(\tilde{K}) = \gamma q\,\mathbf{E} + \gamma q\,\mathbf{v}\times\mathbf{B}.
$$

The first term is

$$
\gamma q\,\mathbf{E} = \frac{\gamma q}{2i\sqrt{\epsilon}}\left(\tilde{F} + \tilde{F}^\dagger\right)
= -\,\frac{q}{4c\sqrt{\epsilon}}\operatorname{Vect}\!\left(S + S^\dagger\right),
$$

using $\operatorname{Vect}(S + S^\dagger) = 2i\gamma c\,(\tilde{F} + \tilde{F}^\dagger)$, and the second is

$$
\gamma q\,\mathbf{v}\times\mathbf{B}
= \frac{\gamma q\sqrt{\mu}}{2}\,\mathbf{v}\times\left(\tilde{F}^\dagger - \tilde{F}\right)
= \frac{q\sqrt{\mu}}{4}\left(A - A^\dagger\right),
$$

where

$$
A = \tilde{F}\tilde{U} - \tilde{U}\tilde{F}, \qquad
A^\dagger = \tilde{F}^\dagger\tilde{U} - \tilde{U}\tilde{F}^\dagger .
$$

**Step 4: collect.** Adding the scalar and vector parts gives the **master identity**

$$
\tilde{K} = -\,\frac{q}{4c\sqrt{\epsilon}}\left(S + S^\dagger\right)
+ \frac{q\sqrt{\mu}}{4}\left(A - A^\dagger\right),
$$

which, expanded in the four products, is

$$
\boxed{\;
\tilde{K} = \frac{q}{4}\!\left(\sqrt{\mu} - \frac{1}{c\sqrt{\epsilon}}\right)\!\left(\tilde{F}\tilde{U} + \tilde{U}\tilde{F}^\dagger\right)
- \frac{q}{4}\!\left(\sqrt{\mu} + \frac{1}{c\sqrt{\epsilon}}\right)\!\left(\tilde{U}\tilde{F} + \tilde{F}^\dagger\tilde{U}\right).
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
\tilde{K} = -\,\frac{q\sqrt{\mu}}{2}\left(\tilde{U}\tilde{F} + \tilde{F}^\dagger\tilde{U}\right)
= -\,\frac{q}{2c\sqrt{\epsilon}}\left(\tilde{U}\tilde{F} + \tilde{F}^\dagger\tilde{U}\right).
\;}
$$

The two coefficients are equal, $\sqrt{\mu} = 1/(c\sqrt{\epsilon})$, so either may be used. Since $\tilde{F}^\dagger = -\tilde{F}^*$, the formula may also be written

$$
\tilde{K} = -\,\frac{q\sqrt{\mu}}{2}\left(\tilde{U}\tilde{F} - \tilde{F}^*\tilde{U}\right).
$$

**Step 6: the projection form.** Because $\tilde{U}\in\mathbb{M}_-$ and $\tilde{U}^\dagger = -\tilde{U}$, the Hermitian conjugate of the product is

$$
\left(\tilde{U}\tilde{F}\right)^\dagger = \tilde{F}^\dagger\tilde{U}^\dagger = -\,\tilde{F}^\dagger\tilde{U}.
$$

The bracket is therefore twice the anti-Hermitian part of $\tilde{U}\tilde{F}$:

$$
\tilde{U}\tilde{F} + \tilde{F}^\dagger\tilde{U}
= \tilde{U}\tilde{F} - \left(\tilde{U}\tilde{F}\right)^\dagger
= 2\,P_{\mathbb{M}_-}\!\left(\tilde{U}\tilde{F}\right),
$$

and the formula becomes the single statement

$$
\tilde{K} = -\,q\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{U}\tilde{F}\right),
\qquad
P_{\mathbb{M}_-}(X) = \tfrac{1}{2}\left(X - X^\dagger\right).
$$

This is the cleanest form of the result. It says that the Lorentz four-force is, up to the constant $q\sqrt{\mu}$, the **projection of the product $\tilde{U}\tilde{F}$ onto the material sector** $\mathbb{M}_-$. No real part is taken, and no Clifford algebra outside $\mathbb{B}$ is needed.

**Reading by sector.** The projection form has a transparent physical reading. Split the field strength into its Hermitian and anti-Hermitian parts,

$$
\tilde{F}^{(+)} = \tfrac{1}{2}\left(\tilde{F} + \tilde{F}^\dagger\right) = i\sqrt{\epsilon}\,\mathbf{E}
\;\in\;\mathbb{M}_+,
\qquad
\tilde{F}^{(-)} = \tfrac{1}{2}\left(\tilde{F} - \tilde{F}^\dagger\right) = -\sqrt{\mu}\,\mathbf{H}
\;\in\;\mathbb{M}_-,
$$

the electric part in the informational (Hermitian) sector and the magnetic part in the material (anti-Hermitian) sector. Then

$$
\tilde{U}\tilde{F} + \tilde{F}^\dagger\tilde{U}
= \left\{\tilde{U}, \tilde{F}^{(+)}\right\} + \left[\tilde{U}, \tilde{F}^{(-)}\right],
$$

where $\{,\}$ is the anticommutator and $[,]$ the commutator, so that

$$
\tilde{K} = -\,\frac{q}{2c\sqrt{\epsilon}}
\left(\left\{\tilde{U}, \tilde{F}^{(+)}\right\} + \left[\tilde{U}, \tilde{F}^{(-)}\right]\right).
$$

The electric field couples to the four-velocity through the **anticommutator**, the magnetic field through the **commutator**. This asymmetry is the algebraic origin of the different roles the two fields play in the force: the electric field does work and changes the energy, the magnetic field does not.

**Checks.** The formula is verified by direct substitution. Two special cases are instructive.

*Particle at rest.* With $\mathbf{v} = 0$ we have $\gamma = 1$ and $\tilde{U} = ic$. Then

$$
\tilde{K} = -\,\frac{q\sqrt{\mu}}{2}\left(ic\,\tilde{F} + \tilde{F}^\dagger ic\right)
= -\,\frac{iq\sqrt{\mu}c}{2}\left(\tilde{F} + \tilde{F}^\dagger\right)
= -\,\frac{iq\sqrt{\mu}c}{2}\left(2i\sqrt{\epsilon}\,\mathbf{E}\right)
= q\sqrt{\mu}\,c\sqrt{\epsilon}\,\mathbf{E} = q\,\mathbf{E},
$$

since $c\sqrt{\epsilon\mu} = 1$. The scalar part vanishes, as it must for a particle at rest.

*Pure magnetic field.* With $\mathbf{E} = 0$ we have $\tilde{F}^\dagger = -\tilde{F} = \sqrt{\mu}\,\mathbf{H}$, and

$$
\tilde{K} = -\,\frac{q\sqrt{\mu}}{2}\left(-\sqrt{\mu}\,\tilde{U}\mathbf{H} + \sqrt{\mu}\,\mathbf{H}\tilde{U}\right)
= \frac{q\mu}{2}\left(\tilde{U}\mathbf{H} - \mathbf{H}\tilde{U}\right)
= q\mu\,\gamma\left(\mathbf{v}\times\mathbf{H}\right)
= \gamma q\left(\mathbf{v}\times\mathbf{B}\right),
$$

which is the magnetic part of the component form, with vanishing scalar part: a pure magnetic field does no work.

*General case.* For arbitrary $\mathbf{E}$, $\mathbf{B}$, $\mathbf{v}$, the identity $\tilde{K} = -q\sqrt{\mu}\,P_{\mathbb{M}_-}(\tilde{U}\tilde{F})$ was checked numerically against the component form at random field configurations, with agreement to machine precision (maximum discrepancy of order $10^{-15}$ relative to terms of order unity). It is an algebraic identity, not an approximation.

## The Force, the Four-Velocity, and the Four-Momentum

The product formula makes the relation between the four-force and the kinematic four-vectors of $\mathbb{M}_-$ explicit.

The four-velocity and four-momentum are

$$
\tilde{U} = \gamma\left(ic\,e_0 + \mathbf{v}\right),
\qquad
\tilde{P} = m\tilde{U} = i\,\frac{E}{c}\,e_0 + \mathbf{p},
$$

with $E = \gamma mc^2$ and $\mathbf{p} = \gamma m\mathbf{v}$, and they satisfy the normalization and mass-shell conditions

$$
\tilde{U}\bar{\tilde{U}} = -c^2,
\qquad
\tilde{P}\bar{\tilde{P}} = -m^2c^2.
$$

The four-force is the proper-time derivative $\tilde{K} = d\tilde{P}/d\tau$, and the product formula expresses it directly in terms of $\tilde{U}$ and the field:

$$
\tilde{K} = -\,q\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{U}\tilde{F}\right)
= -\,\frac{q}{2c\sqrt{\epsilon}}\left(\tilde{U}\tilde{F} + \tilde{F}^\dagger\tilde{U}\right).
$$

The four-force is thus built from the same ingredients as the four-momentum — the four-velocity and the field — and inherits its membership in $\mathbb{M}_-$ from the projection.

Three consequences follow at once.

**Orthogonality.** Differentiating the mass shell, $\frac{d}{d\tau}(\tilde{P}\bar{\tilde{P}}) = \tilde{K}\bar{\tilde{P}} + \tilde{P}\bar{\tilde{K}} = 0$. In components this is the familiar $K^\mu P_\mu = 0$, which for the Lorentz force reads

$$
\left(i\frac{\gamma P_{\text{mech}}}{c}\right)\left(i\gamma mc\right) + \left(\gamma\mathbf{f}\right)\cdot\left(\gamma m\mathbf{v}\right)
= -\gamma^2 m\,P_{\text{mech}} + \gamma^2 m\left(\mathbf{f}\cdot\mathbf{v}\right) = 0,
$$

since $\mathbf{f}\cdot\mathbf{v} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})\cdot\mathbf{v} = q\,\mathbf{E}\cdot\mathbf{v} = P_{\text{mech}}$. The cancellation is exact.

**Conservation of rest mass.** Since $\tilde{P}\bar{\tilde{P}} = -m^2c^2$ is constant along the worldline, the rest mass is unchanged by the Lorentz force. The force can rotate the four-momentum in $\mathbb{M}_-$ but cannot change its norm form.

**The non-relativistic limit.** For $|\mathbf{v}| \ll c$ the scalar part of $\tilde{K}$ is negligible relative to the vector part, and the four-force reduces to the Newtonian Lorentz force $q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$.

## The Invariants of the Motion and the Field Invariants

The electromagnetic field has exactly two independent local invariants, fixed by the field-strength article:

$$
I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2,
\qquad
I_2 = \mathbf{E}\cdot\mathbf{B}.
$$

They are the real and imaginary parts of the norm form of the field,

$$
N(\tilde{F}) = \tilde{F}\bar{\tilde{F}} = -\epsilon\left(I_1 + 2ic\,I_2\right),
$$

and they are invariant under the proper orthochronous Lorentz group. It is natural to ask what these field invariants imply for the *motion* of a charged particle. The answer has two parts, and it is worth separating them carefully.

### The invariant of the motion

The motion's own invariant is the **mass shell**,

$$
\tilde{P}\bar{\tilde{P}} = -m^2c^2,
$$

which, as shown above, is preserved by the Lorentz force because the force is orthogonal to the four-momentum. This invariant is independent of the field: every charged particle retains its rest mass, whatever the field. In the biquaternion framework this is the statement that the four-force lies in $\mathbb{M}_-$ and is orthogonal to $\tilde{P}$ in the norm form.

### The force's Lorentz scalar

The norm form of the four-force itself,

$$
N(\tilde{K}) = \tilde{K}\bar{\tilde{K}} = -\left(K^0\right)^2 + \left|\mathbf{K}\right|^2,
$$

is a Lorentz scalar; it is not conserved along the motion. Substituting the component form,

$$
N(\tilde{K}) = \gamma^2 q^2\left[\left|\mathbf{E} + \mathbf{v}\times\mathbf{B}\right|^2 - \frac{\left(\mathbf{E}\cdot\mathbf{v}\right)^2}{c^2}\right].
$$

Evaluated in the instantaneous rest frame of the particle, where $\mathbf{v} = 0$ and $\gamma = 1$, this is $q^2\mathbf{E}_{\text{rest}}^2$, and since $N(\tilde{K})$ is a Lorentz scalar,

$$
N(\tilde{K}) = q^2\,\mathbf{E}_{\text{rest}}^2
$$

in every frame. The scalar measures the electric field in the particle's rest frame. Unlike the field invariants $I_1, I_2$, it is not determined by the field alone, because the rest frame depends on the particle's velocity.

### The field invariants classify the force

The invariants $I_1, I_2$ determine the Lorentz type of the field, and therefore the possible shapes of the force. The classification, established in the field-strength article, is the following.

- **Null field** ($I_1 = I_2 = 0$). Then $\mathbf{E}\perp\mathbf{B}$ and $|\mathbf{E}| = c|\mathbf{B}|$ pointwise, and no Lorentz transformation can remove either field. The field is radiative. The norm form of the field vanishes, and $\tilde{F}$ is a zero divisor of $\mathbb{B}$.
- **Electric type** ($I_2 = 0$, $I_1 > 0$). Then there is a frame in which $\mathbf{B} = 0$, with $\mathbf{E}^2 = I_1$. In that frame the four-force is $\tilde{K} = i\gamma q(\mathbf{E}\cdot\mathbf{v})/c\,e_0 + \gamma q\,\mathbf{E}$: purely electric.
- **Magnetic type** ($I_2 = 0$, $I_1 < 0$). Then there is a frame in which $\mathbf{E} = 0$, with $c^2\mathbf{B}^2 = -I_1$. In that frame the four-force is $\tilde{K} = \gamma q(\mathbf{v}\times\mathbf{B})$: purely magnetic, and no work is done.
- **Generic field** ($I_2 \neq 0$). Then no frame removes either field, but there is a frame in which $\mathbf{E}$ and $\mathbf{B}$ are parallel, with magnitudes determined by the two invariants through

$$
E_0^2 = \frac{I_1 + \sqrt{I_1^2 + 4c^2I_2^2}}{2},
\qquad
B_0 = \frac{I_2}{E_0}.
$$

The invariants do not determine the force, because the force also depends on the particle velocity; what they determine is the *type* of field, and hence the family of forces the field can exert. In the frames just listed the force takes its simplest form: electric in the electric frame, magnetic in the magnetic frame, and dominated by the parallel electric and magnetic fields in the generic frame.

### The characteristic rates of the motion

There is one further sense in which the field invariants govern the motion, and it is the sharpest one. For a particle in a **uniform** field the equation of motion is linear,

$$
\frac{dP^\mu}{d\tau} = \frac{q}{m}\,F^{\mu}{}_{\nu}P^\nu,
$$

so the proper-time motion is a superposition of exponentials whose rates are $(q/m)$ times the eigenvalues of the field matrix $F^{\mu}{}_{\nu}$. In the $ict$ convention those eigenvalues are determined by the two invariants: the characteristic polynomial is

$$
\det\!\left(\lambda\,\mathbb{1} - F\right)
= \lambda^4 - \frac{I_1}{c^2}\,\lambda^2 - \frac{I_2^2}{c^2},
$$

so the eigenvalues are $\pm\lambda_+,\pm\lambda_-$ with

$$
\lambda_\pm^2 = \frac{I_1 \pm \sqrt{I_1^2 + 4c^2I_2^2}}{2c^2}.
$$

In the frame in which $\mathbf{E}$ and $\mathbf{B}$ are parallel these reduce to $\lambda = \pm E_0/c$ and $\lambda = \pm iB_0$. Two familiar cases are immediate. A pure magnetic field ($I_1 < 0$, $I_2 = 0$, frame with $\mathbf{E} = 0$) gives eigenvalues $\pm iB$ and the cyclotron frequency $\omega = qB/m$: uniform circular motion, with constant energy. A pure electric field ($I_2 = 0$, $I_1 > 0$, frame with $\mathbf{B} = 0$) gives eigenvalues $\pm E/c$ and hyperbolic (uniformly accelerated) motion. The field invariants, not the field components, are the Lorentz-invariant data that fix these rates.

### A null-field invariant

One genuine extra invariant of the motion exists in the null case. A null field is radiative: its field matrix has a null eigenvector $k$ (the propagation direction), satisfying $k_\mu F^{\mu}{}_{\nu} = 0$. Then

$$
\frac{d}{d\tau}\left(k\cdot P\right)
= k_\mu\,\frac{dP^\mu}{d\tau}
= \frac{q}{m}\,k_\mu F^{\mu}{}_{\nu}P^\nu = 0,
$$

so $k\cdot P$ is constant along the worldline. This is the invariant of the motion associated with the degenerate (radiative) type of the field, and it exists precisely when $I_1 = I_2 = 0$. For non-null fields the mass shell is the only invariant of this simple kind.

## The Transformation of the Force under Boosts

Because the four-force is a four-vector, it transforms under the Lorentz group by the same **rotor conjugation** as every other element of $\mathbb{M}_-$:

$$
\tilde{K}' = \tilde{\Lambda}\,\tilde{K}\,\tilde{\Lambda}^\dagger,
$$

where $\tilde{\Lambda}$ is the unit-norm biquaternion of the boost, and $\tilde{K}' = d\tilde{P}'/d\tau$ is the force measured in the boosted frame (the proper time is invariant). This is the statement that the force transforms in the **vector representation** of the Lorentz group.

For a pure boost with velocity $\mathbf{u}$ — a frame boost, distinct from the particle velocity $\mathbf{v}$ — the boost biquaternion is

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}},
\qquad
\tanh\psi = \frac{u}{c},
\qquad
\gamma_u = \cosh\psi = \frac{1}{\sqrt{1 - \mathbf{u}^2/c^2}},
$$

an element of $\mathbb{M}_+$ (Hermitian, unit norm). The rotor conjugation then reproduces the standard component transformation

$$
K'^0 = \gamma_u\left(K^0 - i\,\frac{\mathbf{u}\cdot\mathbf{K}}{c}\right),
$$

$$
\mathbf{K}' = \mathbf{K} + \frac{\gamma_u - 1}{u^2}\left(\mathbf{u}\cdot\mathbf{K}\right)\mathbf{u} - \gamma_u\,\frac{K^0}{c}\,\mathbf{u}.
$$

Written in the biquaternion variables, with $\tilde{K} = K^0e_0 + \mathbf{K}$ and $\tilde{K}' = K'^0e_0 + \mathbf{K}'$, these are exactly the components of $\tilde{\Lambda}\tilde{K}\tilde{\Lambda}^\dagger$. The verification is direct: the rotor conjugation and the component formulas agree to machine precision at random boosts and random forces (maximum discrepancy of order $10^{-15}$).

**How the field transforms.** The field strength is *not* a four-vector, and it does not transform like one. Under the same boost it transforms in the rank-two (bivector) representation,

$$
\tilde{F}' = \bar{\tilde{\Lambda}}\,\tilde{F}\,\tilde{\Lambda},
$$

with $\bar{\tilde{\Lambda}}$ the quaternion conjugate of the rotor (equivalently $\tilde{\Lambda}^{-1}$ for a unit-norm rotor). This reproduces the standard field transformation

$$
\mathbf{E}' = \gamma_u\left(\mathbf{E} + \mathbf{u}\times\mathbf{B}\right) - \frac{\gamma_u - 1}{u^2}\left(\mathbf{u}\cdot\mathbf{E}\right)\mathbf{u},
$$

$$
\mathbf{B}' = \gamma_u\left(\mathbf{B} - \frac{1}{c^2}\,\mathbf{u}\times\mathbf{E}\right) - \frac{\gamma_u - 1}{u^2}\left(\mathbf{u}\cdot\mathbf{B}\right)\mathbf{u},
$$

and it is this bivector rule — not the vector rule — that leaves the field invariants $I_1$ and $I_2$ unchanged. The distinction between the vector and bivector transformation laws is the algebraic expression of the fact that four-vectors live in $\mathbb{M}_-$ while the field strength does not.

**Covariance of the product formula.** The product formula is manifestly covariant under pure boosts, in the following precise sense. Apply the vector rule to the four-velocity, $\tilde{U}' = \tilde{\Lambda}\tilde{U}\tilde{\Lambda}^\dagger$, and the bivector rule to the field, $\tilde{F}' = \bar{\tilde{\Lambda}}\tilde{F}\tilde{\Lambda}$. Then the right-hand side of the product formula transforms into the right-hand side computed with the primed fields, and equals $\tilde{\Lambda}\tilde{K}\tilde{\Lambda}^\dagger$:

$$
-q\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{U}'\tilde{F}'\right)
= \tilde{\Lambda}\left[-q\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{U}\tilde{F}\right)\right]\tilde{\Lambda}^\dagger
= \tilde{K}'.
$$

This was checked numerically at random boosts, random fields, and random velocities, with agreement at the $10^{-15}$ level. In this sense the product formula is not merely a frame-dependent identity but a covariant statement: transforming the ingredients and transforming the result give the same answer.

## Summary

The Lorentz four-force has the component form

$$
\tilde{K} = i\,\frac{\gamma q}{c}\left(\mathbf{E}\cdot\mathbf{v}\right)e_0 + \gamma q\left(\mathbf{E} + \mathbf{v}\times\mathbf{B}\right),
$$

which is the contraction $K^\mu = qF^{\mu\nu}u_\nu$ written in the biquaternion basis, and it lies in the anti-Hermitian subspace $\mathbb{M}_-$. Its expression as a biquaternion product of the field strength and the four-velocity is not the real part of $\tilde{F}\tilde{U}$ — that object has the wrong reality structure and lies outside $\mathbb{M}_-$ — but the anti-Hermitian projection of $\tilde{U}\tilde{F}$:

$$
\boxed{\;\tilde{K} = -\,q\sqrt{\mu}\;P_{\mathbb{M}_-}\!\left(\tilde{U}\tilde{F}\right)
= -\,\frac{q\sqrt{\mu}}{2}\left(\tilde{U}\tilde{F} + \tilde{F}^\dagger\tilde{U}\right).\;}
$$

Equivalently, $\tilde{K} = -\frac{q}{2c\sqrt{\epsilon}}(\tilde{U}\tilde{F} + \tilde{F}^\dagger\tilde{U})$, since $\sqrt{\mu} = 1/(c\sqrt{\epsilon})$; and since $\tilde{F}^\dagger = -\tilde{F}^*$, the formula may be written $-\frac{q\sqrt{\mu}}{2}(\tilde{U}\tilde{F} - \tilde{F}^*\tilde{U})$. The conjugate field is essential: it carries the anti-self-dual half of the field tensor, and the electric and magnetic contributions can be separated only by combining the two halves. This resolves the open question recorded in the relativistic-mechanics article, and fixes the force notation: the four-force is written $\tilde{K}$, while $\tilde{F}$ is reserved for the field strength.

The structural consequences are these. The four-force is orthogonal to the four-momentum, $\tilde{K}\bar{\tilde{P}} + \tilde{P}\bar{\tilde{K}} = 0$, so the mass shell $\tilde{P}\bar{\tilde{P}} = -m^2c^2$ is preserved and the rest mass is unchanged by the Lorentz force. The force's norm form $N(\tilde{K})$ is a Lorentz scalar equal to $q^2\mathbf{E}_{\text{rest}}^2$, the squared electric field in the particle's rest frame. The field invariants $I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2$ and $I_2 = \mathbf{E}\cdot\mathbf{B}$ classify the field as null, electric, magnetic, or generic, and thereby fix the simplest possible shape of the force and, for a uniform field, the characteristic rates of the motion: the eigenvalues of the field matrix solve $\lambda^4 - (I_1/c^2)\lambda^2 - I_2^2/c^2 = 0$. In the null case a null eigenvector $k$ of the field matrix gives one further invariant of the motion, $k\cdot P$. Finally, under boosts the four-force transforms in the vector representation, $\tilde{K}' = \tilde{\Lambda}\tilde{K}\tilde{\Lambda}^\dagger$, while the field transforms in the bivector representation, $\tilde{F}' = \bar{\tilde{\Lambda}}\tilde{F}\tilde{\Lambda}$, and the product formula is covariant under the pair.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $X^\dagger = \bar{X}^{\,*}$ | Hermitian conjugate |
| $X^*$, $\bar{X}$ | Complex conjugate, quaternion conjugate |
| $P_{\mathbb{M}_-}(X) = \tfrac12(X - X^\dagger)$ | Projection onto $\mathbb{M}_-$ (anti-Hermitian part) |
| $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ | Field-strength biquaternion (pure vector) |
| $\tilde{F}^\dagger = i\sqrt{\epsilon}\,\mathbf{E} + \sqrt{\mu}\,\mathbf{H}$ | Hermitian conjugate of the field strength |
| $\mathbf{E}, \mathbf{H}, \mathbf{B} = \mu\mathbf{H}$ | Electric field, magnetic field, magnetic induction |
| $\epsilon, \mu$ | Permittivity and permeability of the medium |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $q$ | Particle charge |
| $\mathbf{v}$ | Particle three-velocity |
| $\mathbf{u}$ | Frame (boost) three-velocity |
| $\gamma = 1/\sqrt{1-\mathbf{v}^2/c^2}$ | Lorentz factor of the particle |
| $\gamma_u = 1/\sqrt{1-\mathbf{u}^2/c^2}$ | Lorentz factor of the boost |
| $\tau$ | Proper time |
| $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | Four-velocity biquaternion |
| $\tilde{P} = m\tilde{U}$ | Four-momentum biquaternion |
| $\tilde{K} = d\tilde{P}/d\tau$ | Four-force (Minkowski force) biquaternion |
| $\mathbf{f} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ | Relativistic three-force |
| $P_{\text{mech}} = q\,\mathbf{E}\cdot\mathbf{v}$ | Mechanical power |
| $I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2$ | First field invariant |
| $I_2 = \mathbf{E}\cdot\mathbf{B}$ | Second field invariant |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Boost biquaternion (Hermitian, unit norm) |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the covariant Lorentz force, the field invariants, and the motion in a uniform field.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard four-vector formulation of the Lorentz force and its transformation under boosts.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the contraction $f = q\,F\cdot u$ of a bivector with a vector in spacetime algebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of Lorentz transformations and the bivector treatment of the electromagnetic field.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even subalgebra of $\mathrm{Cl}_{1,3}$ and for the self-dual and anti-self-dual decomposition of the field tensor.
- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* 22 (1907) 579–586, for the complex-vector formulation of the electromagnetic field.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for the complex-vector and duality structure of electromagnetism.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for a biquaternionic treatment of the electromagnetic field and the Lorentz force.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation of the field equations.
