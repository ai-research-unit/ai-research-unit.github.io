# __Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem__

## Introduction

Unitarity is the statement that the norm of a state does not change in time. In the biquaternion framework there are two norms on the algebra, and they behave differently: the **Hermitian norm** $\mathrm{Tr}(\tilde Q_1^{*}\tilde Q_1)$, which is positive definite and is the Hilbert–Schmidt norm of the matrix model, and the **biquaternion norm** $\langle\tilde Q_1\rangle_{\natural} = \langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=\tilde Q_1\tilde Q_1^{\natural}$, which is central-valued and indefinite. This article asks, for each of them, under exactly which elements of $\mathbb{B}$ the conjugation action
$$
\Gamma_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}
$$
preserves it. The answer is a norm-preservation theorem with a single organising theme: **the conditions are conditions on the centre of the algebra.**

Three statements are proved. The first is that $\Gamma_{\tilde Q}$ preserves the Hermitian norm if and only if $\tilde Q$ is $*$-unitary, $\tilde Q\tilde Q^{*}=e_t$. The second is that $\Gamma_{\tilde Q}$ scales the biquaternion norm by a **central scalar**,
$$
\langle\Gamma_{\tilde Q}\tilde Q_1\rangle_{\natural}=\bigl|\langle\tilde Q\rangle_{\natural}\bigr|^2\,\langle\tilde Q_1\rangle_{\natural},
$$
so that it preserves the biquaternion norm exactly when $|\langle\tilde Q\rangle_{\natural}|=1$, i.e. when $\langle\tilde Q\rangle_{\natural}$ lies on the unit circle of the centre $\mathbb{C}_{\mathbb{B}}$. The third is the structural reason behind the word *centrality* in the title: the product $\tilde Q^{*}\tilde Q$, which measures the failure of $\Gamma_{\tilde Q}$ to be multiplicative, is central if and only if that failure is a scalar rather than an operator-valued anomaly; and it equals $e_t$ — the case of a genuine algebra automorphism — if and only if $\tilde Q$ is $*$-unitary. Thus

$$
\Gamma_{\tilde Q}\ \text{is multiplicative} \iff \tilde Q^{*}\tilde Q=e_t \iff \tilde Q\ \text{}{}^{*}\text{-unitary},
$$

and the intermediate case $\tilde Q^{*}\tilde Q=\lambda e_t$ with central $\lambda$ is a homomorphism up to the central scalar $\lambda$.

The same theme governs the dynamics. The state-vector equation requires a unit $J$ with $J^2=-e_t$ and a Hermitian generator $\tilde{H}$; the flow it generates preserves the Hermitian norm **for every Hermitian $\tilde{H}$** if and only if $J$ commutes with every Hermitian element, i.e. if and only if $J$ is central. The centre contains exactly the two roots $\pm i$, so the norm-preserving unit of the Schrödinger equation is forced to be the scalar imaginary. This is the precise sense of the title: unitarity follows from centrality.

The article is organised as follows. The two norms are written down and their natures contrasted; the conjugation action and its defect are introduced; the two norm-preservation theorems are proved; the norm-preserving groups are identified as $\mathrm{U}(2)$ for the Hermitian norm and $\mathrm{U}(1)\cdot SL(2,\mathbb{C})$ for the biquaternion norm, the second containing the first, so that the intersection of the two is $\mathrm{U}(2)$ itself while $\mathrm{U}(2)\cap SL(2,\mathbb{C})=SU(2)$; the flow version and the forced centrality of the unit are proved; and the standard and algebraic parts of the result are separated. Worked counterexamples show what fails when the centrality hypothesis is dropped.

## The Two Norms

The word "norm" carries two distinct objects in this framework, and the whole article turns on not confusing them.

**The Hermitian norm.** For $\tilde Q_1,\tilde Q_1\in\mathbb{B}$ define
$$
\langle\tilde Q_1,\tilde Q_1\rangle_{\dagger}=\mathrm{Tr}\bigl(\tilde Q_1^{*}\tilde Q_1\bigr),
\qquad
\|\tilde Q_1\|_{\dagger}^2=\mathrm{Tr}\bigl(\tilde Q_1^{*}\tilde Q_1\bigr).
$$
Writing $\tilde Q_1=x_te_t+x_x\vec e_x+x_y\vec e_y+x_z\vec e_z$ with $x_\mu\in\mathbb{C}$ and using $\tilde Q_1^{*}=x_t^{*}e_t-x_x^{*}\vec e_x-x_y^{*}\vec e_y-x_z^{*}\vec e_z$, one finds
$$
\|\tilde Q_1\|_{\dagger}^2
=2\bigl(|x_t|^2+|x_x|^2+|x_y|^2+|x_z|^2\bigr)>0\quad(\tilde Q_1\neq0).
$$
This form is positive definite of signature $(8,0)$ on the real eight-dimensional algebra. It is the Hilbert–Schmidt form of the matrix model, $\langle \tilde Q_1,\tilde Q_1\rangle_{*}=\mathrm{tr}(M(\tilde Q_1)^\dagger M(\tilde Q_1))$ with $\mathrm{tr}$ the ordinary $2\times2$ matrix trace, and its restriction to the state module is the quantity $\mathrm{Tr}(\psi^\dagger\psi)$ that normalizes spinors. This is the norm whose preservation is the unitarity statement of quantum physics: the Born probability is written with the Hermitian form, whose trace reading at normalisation is $\operatorname{Tr}(\tilde Q_1\tilde{H}^{*})$, and the trace pairing $\mathrm{Tr}(\tilde Q_1\tilde Q_2)$ of two states is the boundary case of this norm.

**The biquaternion norm.** The second object is
$$
\langle\tilde Q_1\rangle_{\natural} = \langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=\tilde Q_1\tilde Q_1^{\natural}=\bigl(x_t^2+x_x^2+x_y^2+x_z^2\bigr)e_t\in\mathbb{C}_{\mathbb{B}},
$$
a quadratic form with values in the **centre**, not in $\mathbb{R}$. Its coefficient is the determinant of the matrix model, $\langle\tilde Q_1\rangle_{\natural}e_t=\det M(\tilde Q_1)\,e_t$, so $\langle\cdot\rangle_{\natural}$ is multiplicative,
$$
\langle\tilde Q_1\tilde Q_1\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_1\rangle_{\natural},
$$
and it is indefinite on $\mathbb{M}_+$: for $\tilde{H}=h_te_t+i\vec h$ one has $\langle\tilde{H}\rangle_{\natural}=(h_t^2-|\vec h|^2)e_t$, of signature $(1,3)$. Its null cone is the pure-state boundary of the Bloch ball.

The two norms differ in every structural respect that matters here. The Hermitian norm is real-valued and positive definite; the biquaternion norm is centre-valued and indefinite. The Hermitian norm is preserved by the left action of the unitaries on the state module; the biquaternion norm is preserved by the left action of the unit-norm elements $SL(2,\mathbb{C})$. The Hermitian norm detects the state; the biquaternion norm detects the determinant. A reader who asks "which norm does the framework use" is asking a question with two correct answers, and the answer depends on whether the object at hand is a state overlap or a determinant.

## The Conjugation Action and Its Defect

The action studied throughout is conjugation by an invertible element,
$$
\Gamma_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*},
\qquad
\tilde Q\in\mathbb{B}^{\times}.
$$
It has the following elementary properties, each immediate from the definitions.

**It preserves Hermiticity.** Since ${}^{*}$ is an anti-automorphism,
$$
\Gamma_{\tilde Q}(\tilde Q_1)^{*}=\tilde Q\tilde Q_1^{*}\tilde Q^{*}=\Gamma_{\tilde Q}\bigl(\tilde Q_1^{*}\bigr),
$$
so Hermitian elements go to Hermitian elements and anti-Hermitian to anti-Hermitian. In particular $\Gamma_{\tilde Q}$ acts on $\mathbb{M}_+$ and on the state space, and it maps the positive cone to itself, because a congruence by an invertible element preserves the signature.

**It fixes the unit only for unitaries.** Evaluating at $e_t$,
$$
\Gamma_{\tilde Q}(e_t)=\tilde Q\tilde Q^{*} .
$$
So the action is unital, $\Gamma_{\tilde Q}(e_t)=e_t$, if and only if $\tilde Q\tilde Q^{*}=e_t$, i.e. if and only if $\tilde Q$ is $*$-unitary.

**Its defect is $\tilde Q^{*}\tilde Q$.** Compute the product of two images:
$$
\Gamma_{\tilde Q}(\tilde Q_1)\,\Gamma_{\tilde Q}(\tilde Q_1)
=\tilde Q\tilde Q_1\tilde Q^{*}\tilde Q\tilde Q_1\tilde Q^{*}
=\tilde Q\tilde Q_1\bigl(\tilde Q^{*}\tilde Q\bigr)\tilde Q_1\tilde Q^{*} .
$$
Compare with $\Gamma_{\tilde Q}(\tilde Q_1\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q_1\tilde Q^{*}$. The two agree for all $\tilde Q_1,\tilde Q_1$ if and only if
$$
\tilde Q^{*}\tilde Q\,\tilde Q_1=\tilde Q_1\qquad\text{for all }\tilde Q_1,
$$
which holds if and only if $\tilde Q^{*}\tilde Q=e_t$. This is the **defect** of the action.

**The centrality statement.** If the defect is central, $\tilde Q^{*}\tilde Q=\lambda e_t$ with $\lambda\in\mathbb{C}_{\mathbb{B}}$, then it commutes past $\tilde Q_1$ and
$$
\Gamma_{\tilde Q}(\tilde Q_1)\Gamma_{\tilde Q}(\tilde Q_1)
=\lambda\,\Gamma_{\tilde Q}(\tilde Q_1\tilde Q_1),
$$
so that $\Gamma_{\tilde Q}$ is an algebra homomorphism **up to the central scalar $\lambda$**. The failure of multiplicativity is then a scalar — the same number for every pair $\tilde Q_1,\tilde Q_1$ — rather than an operator-valued anomaly that distorts each product differently. Centrality of the defect is exactly the condition that the anomaly is scalar; and the scalar is $1$, i.e. the action is multiplicative, exactly when $\tilde Q$ is $*$-unitary:
$$
\boxed{\;\Gamma_{\tilde Q}\text{ multiplicative}
\iff \tilde Q^{*}\tilde Q=e_t
\iff \tilde Q\text{ }{}^{*}\text{-unitary}\;}.
$$
This is the first appearance of the centre in the norm-preservation problem, and it is the structural core of the article. Note that $\tilde Q^{*}\tilde Q$ is automatically **Hermitian and positive**, $(\tilde Q^{*}\tilde Q)^{*}=\tilde Q^{*}\tilde Q$, so when it is central it is $\lambda e_t$ with $\lambda\in\mathbb{R}$ and $\lambda>0$ for $\tilde Q\neq0$; the central defect is a positive real scalar multiple of the identity, and unitarity is its normalization to $1$.

## The Norm-Preservation Theorem

The two parts of the theorem are stated and proved separately, because they have different hypotheses and different content.

### Part 1: the Hermitian norm

**Theorem 1.** Let $\tilde Q\in\mathbb{B}^{\times}$. The conjugation $\Gamma_{\tilde Q}$ preserves the Hermitian norm for all $\tilde Q_1$,
$$
\boxed{\;\mathrm{Tr}\bigl(\Gamma_{\tilde Q}(\tilde Q_1)^{*}\,\Gamma_{\tilde Q}(\tilde Q_1)\bigr)=\mathrm{Tr}\bigl(\tilde Q_1^{*}\tilde Q_1\bigr)
\qquad\text{for all }\tilde Q_1\;},
$$
if and only if $\tilde Q$ is $*$-unitary, $\tilde Q^{*}\tilde Q=e_t$.

**Proof.** Write $\tilde Q_4=\tilde Q^{*}\tilde Q$, which is Hermitian and positive. Since $\Gamma_{\tilde Q}(\tilde Q_1)^{*}=\tilde Q\tilde Q_1^{*}\tilde Q^{*}$,
$$
\mathrm{Tr}\bigl(\Gamma_{\tilde Q}(\tilde Q_1)^{*}\Gamma_{\tilde Q}(\tilde Q_1)\bigr)
=\mathrm{Tr}\bigl(\tilde Q\tilde Q_1^{*}\tilde Q^{*}\tilde Q\tilde Q_1\tilde Q^{*}\bigr)
=\mathrm{Tr}\bigl(\tilde Q_1^{*}\tilde Q_4\tilde Q_1\tilde Q_4\bigr),
$$
using the cyclicity of the trace twice. If $\tilde Q_4=e_t$ this is $\mathrm{Tr}(\tilde Q_1^{*}\tilde Q_1)$, so unitarity is sufficient. Conversely, suppose the identity holds for all $\tilde Q_1$ and take $\tilde Q_1$ rank one, $\tilde Q_1=|\varphi\rangle\langle\varphi|$ in the matrix model. Then $\tilde Q_1^{*}\tilde Q_4\tilde Q_1=\langle\varphi|\tilde Q_4\varphi\rangle\,|\varphi\rangle\langle\varphi|$ and
$$
\mathrm{Tr}\bigl(\tilde Q_1^{*}\tilde Q_4\tilde Q_1\tilde Q_4\bigr)
=\langle\varphi|\tilde Q_4\varphi\rangle\,\mathrm{Tr}\bigl(|\varphi\rangle\langle\varphi|\tilde Q_4\bigr)
=\langle\varphi|\tilde Q_4\varphi\rangle^2 .
$$
The preserved value is $\mathrm{Tr}(\tilde Q_1^{*}\tilde Q_1)=1$, so $\langle\varphi|\tilde Q_4\varphi\rangle^2=1$ for every unit $\varphi$; positivity gives $\langle\varphi|\tilde Q_4\varphi\rangle=1$ for all unit $\varphi$, hence $\tilde Q_4=e_t$.

The theorem extends from the norm to the pairing by polarization, and it extends to the trace pairing $\mathrm{Tr}(\tilde Q_1\tilde Q_1^{*})$ on $\mathbb{M}_+$ by the same argument applied to Hermitian elements. The physical content is that the Born probabilities of two states are preserved under $\Gamma_{\tilde Q}$ exactly when $\tilde Q$ is $*$-unitary, which is the standard statement of unitarity in the framework's language.

### Part 2: the biquaternion norm

**Theorem 2.** Let $\tilde Q\in\mathbb{B}^{\times}$. The conjugation scales the biquaternion norm by a central scalar,
$$
\boxed{\;\langle\Gamma_{\tilde Q}(\tilde Q_1)\rangle_{\natural}=\bigl|\langle\tilde Q\rangle_{\natural}\bigr|^2\,\langle\tilde Q_1\rangle_{\natural}
\qquad
\text{for all }\tilde Q_1\;},
$$
where $|\langle\tilde Q\rangle_{\natural}|^2=\langle\tilde Q\rangle_{\natural}\,\langle\tilde Q\rangle_{\natural}^{*}$ is a non-negative real scalar, the complex conjugate being taken coefficientwise on the central element $\langle\tilde Q\rangle_{\natural}$. Consequently $\Gamma_{\tilde Q}$ preserves the biquaternion norm if and only if
$$
\bigl|\langle\tilde Q\rangle_{\natural}\bigr|=1 ,
$$
i.e. if and only if the biquaternion norm of $\tilde Q$ lies on the unit circle of the centre.

**Proof.** Under the matrix model, $M(\Gamma_{\tilde Q}\tilde Q_1)=M(\tilde Q)M(\tilde Q_1)M(\tilde Q^{*})$, and $M(\tilde Q^{*})=M(\tilde Q)^\dagger$. The determinant is multiplicative and the determinant of the adjoint is the conjugate,
$$
\det M\bigl(\Gamma_{\tilde Q}\tilde Q_1\bigr)
=\det M(\tilde Q)\,\det M(\tilde Q_1)\,\det M(\tilde Q)^{*}
=\bigl|\det M(\tilde Q)\bigr|^2\det M(\tilde Q_1).
$$
Since $\det M(\tilde Q_1)=\langle\tilde Q_1\rangle_{\natural}$ for every $\tilde Q_1$, and since $\langle\tilde Q_1\rangle_{\natural}e_t=\det M(\tilde Q_1)\,e_t$, the stated identity follows. Preservation for all $\tilde Q_1$ is equivalent to $|\langle\tilde Q\rangle_{\natural}|^2=1$, i.e. $|\langle\tilde Q\rangle_{\natural}|=1$.

Two features of the proof are worth isolating. First, the scaling factor $|\langle\tilde Q\rangle_{\natural}|^2$ is a **central** scalar: it is a real non-negative multiple of $e_t$, so it commutes with everything and multiplies the biquaternion norm uniformly. The biquaternion norm of an element is itself central-valued, and its modulus is therefore a classical number; preservation of the biquaternion norm is a condition on that number. This is the second appearance of the centre, and it is of a different kind from the first: there the centre appeared as the condition for the multiplicative anomaly to be scalar, here as the target space of the biquaternion norm itself.

Second, the hypothesis $|\langle\tilde Q\rangle_{\natural}|=1$ is genuinely weaker than unitarity. A $*$-unitary $\tilde Q$ has $|\det M(\tilde Q)|=1$, hence $|\langle\tilde Q\rangle_{\natural}|=1$, so every $*$-unitary preserves the biquaternion norm; but the converse fails, as the next section's counterexample shows. The two theorems are therefore not equivalent, and the difference between them is the difference between the quantum norm and the determinant.

### Putting the two together

The two preservation conditions can be read as statements about the same central defect. With $\tilde Q_4=\tilde Q^{*}\tilde Q$,
$$
\tilde Q_4=e_t\ \Longrightarrow\ \Gamma_{\tilde Q}\text{ is an automorphism}\ \Longrightarrow\ \text{both norms preserved},
$$
and the converse implication holds for the Hermitian norm. For the biquaternion norm the condition is weaker, and the enlargement is exactly the group of elements whose determinant has modulus one. The next section identifies the two groups and their intersection.

## The Norm-Preserving Groups

The two theorems single out two groups of invertible elements, and their structure makes the relation between the norms explicit.

**The unitaries.** Define
$$
\mathrm{U}(2)=\bigl\{\tilde Q\in\mathbb{B}:\ \tilde Q^{*}\tilde Q=e_t\bigr\}.
$$
By Theorem 1 these are exactly the elements for which $\Gamma_{\tilde Q}$ preserves the Hermitian norm, and for which $\Gamma_{\tilde Q}$ is an algebra automorphism fixing the unit. In the matrix model they are the $*$-unitary $2\times 2$ matrices; on the state module they are the norm-preserving linear maps; on the Bloch sphere their conjugation image is the rotation group $SO(3)$, with kernel $\{\pm e_t\}$, the double cover of the companion article *Angular Momentum and Spin in Biquaternionic Form*.

**The unit-norm elements.** A unit-norm biquaternion is a Lorentz rotor, written $\tilde U_{\mathrm L}$, and the group is
$$
SL(2,\mathbb{C})=\bigl\{\tilde U_{\mathrm L}\in\mathbb{B}:\ \langle\tilde U_{\mathrm L}\rangle_{\natural} = \langle\tilde U_{\mathrm L},\tilde U_{\mathrm L}\rangle_{\natural}=e_t\bigr\}=\bigl\{\tilde U_{\mathrm L}:\ \det M(\tilde U_{\mathrm L})=1\bigr\},
$$
the elements of unit norm. By Theorem 2 these preserve the biquaternion norm, with the scaling factor exactly $1$; they need not be $*$-unitary, and they need not be norm-preserving for the Hermitian norm. This is the group that acts on the biquaternion norm, and it is the group that the companion articles on the algebra's real structure identify with the determinant-preserving transformations.

**The exact biquaternion-norm group.** Theorem 2 gives preservation of the biquaternion norm under the weaker condition $|\langle\tilde Q\rangle_{\natural}|=1$, and the group is
$$
G_N=\bigl\{\tilde Q\in\mathbb{B}^{\times}:\ |\langle\tilde Q\rangle_{\natural}|=1\bigr\}.
$$
It contains $SL(2,\mathbb{C})$ as the subgroup with phase $1$, and every element factors as a central phase times a unit-norm element,
$$
G_N=\mathrm{U}(1)\cdot SL(2,\mathbb{C}),
\qquad
\tilde Q=\lambda\,\tilde U_{\mathrm L},\quad |\lambda|=1,\quad \langle\tilde U_{\mathrm L}\rangle_{\natural}=e_t ,
$$
because if $\langle\tilde Q\rangle_{\natural}=\mu e_t$ with $|\mu|=1$ then choosing $\lambda$ with $\lambda^2=\mu$ (possible since $\mu$ lies on the unit circle, which is divisible) gives $\langle\tilde Q/\lambda\rangle_{\natural}=e_t$. The decomposition is not direct. The intersection consists of the central scalars that are at once of modulus one and of unit norm; a central scalar is $\lambda e_t$, and $\langle \lambda e_t\rangle_{\natural}=\lambda^2e_t$, so $|\lambda^2|=1$ gives $|\lambda|=1$ while $\lambda^2=1$ gives $\lambda=\pm1$, so the intersection is $\{\pm e_t\}$.

The real dimensions are worth recording. Over $\mathbb{R}$, the algebra is eight-dimensional; $SL(2,\mathbb{C})$ is the six-dimensional real group with one complex equation $\langle\tilde U_{\mathrm L}\rangle_{\natural}=e_t$ (two real conditions); the phase group adds one more real dimension, so $G_N$ is seven-real-dimensional; and $\mathrm{U}(2)$ is four-real-dimensional. The inclusions are
$$
SU(2)=\mathrm{U}(2)\cap SL(2,\mathbb{C})\ \subset\ \mathrm{U}(2)\ \subset\ G_N=\mathrm{U}(1)\cdot SL(2,\mathbb{C}),
$$
with $SU(2)$ the elements that are simultaneously $*$-unitary and of unit norm — the quaternionic unit sphere. The chain records the whole norm-preservation structure: the smallest group is the one that preserves both norms **and** the algebra's multiplication; enlarging to $\mathrm{U}(2)$ keeps the Hermitian norm and the multiplication but gives up the unit-norm condition; enlarging to $G_N$ keeps only the biquaternion norm.

**The $*$-unitary group is not the unit sphere.** The unit group of a form is the set of elements on which the form takes the value $1$; the $*$-unitary group is the isometry group of the form under the conjugation action. For the general plain sesquilinear form the second is the smaller, and the difference is a difference of equations. The defect $\tilde Q\tilde Q^{*}$ is Hermitian, so writing it as $z_te_t+i\vec z$ with $z_t\in\mathbb{R}$ and $\vec z\in\mathbb{R}^3$,
$$
\tilde Q\tilde Q^{*}=e_t\iff z_t=1\ \text{and}\ \vec z=0,
\qquad
\langle\tilde Q,\tilde Q\rangle_{*}=1\iff z_t=1 ,
$$
the general plain sesquilinear algebraic norm interpretation the scalar part alone, $z_t=\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert U_\mu\rvert^2$ (*The Involutions and the Four Forms* of *Conventions of the Products and the Forms*). Unitarity is therefore the norm condition **together with** the vanishing of the vector part of the defect, and it implies the norm condition rather than following from it. The set $\{\tilde Q : \langle\tilde Q,\tilde Q\rangle_{*}=1\}$ is the unit sphere of $\mathbb{B}$ in the sesquilinear norm, of real dimension seven, and it is not a group; the $*$-unitary elements form its four-real-dimensional submanifold. The containment is the biquaternion case of the theorem of *The Unitary Slice and the Compact Real Form with Hermitian Adjoint* that a positive dagger puts the slice inside the unit sphere, and the three dimensions of the gap are exactly the vector part the norm does not see. A reader who meets the phrase "unit norm under ${}^{*}$" should read it as one of the four equations, not as the group.

**The $*$-unitary conjugation is an isometry of all four forms.** The conjugation by a $*$-unitary preserves **all four** forms of *Conventions in the Biquaternion Universe* at once — the general plain bilinear, the general quaternionic bilinear, the general plain sesquilinear and the Krein form — and not the general plain sesquilinear form alone. The computation reduces to two facts already in hand. A $*$-unitary splits as a central phase times a determinant-one part,
$$
\mathrm{U}(2)=\mathrm{U}(1)\cdot SU(2),\qquad \tilde Q=\lambda\tilde u_{\mathrm r},\quad |\lambda|=1,\quad \langle\tilde u_{\mathrm r}\rangle_{\natural}=e_t ,
$$
and the phase is invisible to conjugation, $\Gamma_{\lambda e_t}=\mathrm{id}$, so only the $SU(2)$ part acts; and that part is a **unit real quaternion**, so for it the bar is the identity and the natural sign and the star agree, $\bar{\tilde u_{\mathrm r}}=\tilde u_{\mathrm r}$, $\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{-1}$. The four forms are $\mathrm{Sc}(\tilde Q_3^{a}\tilde Q_1^{b})$ with $a$ the identity or the natural sign on the first slot and $b$ the identity or the star on the second; with the bar trivial and the natural sign equal to the star, each dressing is carried along by the automorphism $\Gamma_{\tilde u_{\mathrm r}}$, and each of the four forms is preserved by the multiplicativity of $\Gamma_{\tilde u_{\mathrm r}}$ together with $\mathrm{Sc}(\tilde u_{\mathrm r}\tilde Q_2\tilde u_{\mathrm r}^{*})=\mathrm{Sc}(\tilde Q_2)$.

**Which group preserves which pair.** The four forms are not preserved by the same larger group, and the split follows the first slot. The two forms that carry the natural sign there — the general quaternionic bilinear form and the Krein form — scale by the **central factor** $\lvert \langle\tilde Q\rangle_{\natural}\rvert^{2}$ under a conjugation,
$$
\langle\Gamma_{\tilde Q}\tilde Q_1,\Gamma_{\tilde Q}\tilde Q_2\rangle_{\natural}=\lvert \langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural},
\qquad
\langle\Gamma_{\tilde Q}\tilde Q_1,\Gamma_{\tilde Q}\tilde Q_2\rangle_{\natural*}=\lvert \langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*} ,
$$
both resting on the identity $\tilde Q^{*}\bar{\tilde Q}=\overline{\langle\tilde Q\rangle_{\natural}}e_t$, the counterpart of $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$. They are therefore preserved **exactly by $G_N$**, the larger group. The two forms without the natural sign — the general plain bilinear and the general plain sesquilinear — are preserved **exactly by $\mathrm{U}(2)$**: for the general plain sesquilinear form the diagonal of a conjugate reads
$$
\mathrm{Sc}\bigl(\tilde Q\tilde Q_1\tilde Q^{*}(\tilde Q\tilde Q_2\tilde Q^{*})^{*}\bigr)=\mathrm{Sc}\bigl(\tilde Q_1\,(\tilde Q^{*}\tilde Q)\,\tilde Q_2^{*}\,(\tilde Q^{*}\tilde Q)\bigr),
$$
which returns $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ for all $\tilde Q_1$ and $\tilde Q_2$ only when $\tilde Q^{*}\tilde Q=e_t$ — setting $\tilde Q_2=e_t$ already forces $(\tilde Q^{*}\tilde Q)^{2}=e_t$, and a Hermitian positive $\tilde Q^{*}\tilde Q$ with that square is $e_t$. The common part of the two groups is $\mathrm{U}(2)$, so the four forms are preserved together only by the smaller group, and the larger group is not a larger symmetry of them. The boosts of $G_N$ separate the two pairs and are the witness: $\tilde U_{\mathrm L}=\cosh t\,e_t+i\sinh t\,\vec e_z$ has $\langle\tilde U_{\mathrm L}\rangle_{\natural}=e_t$, preserves the general quaternionic bilinear and the Krein form, and fails the other two with no constant of proportionality at all — the failure is not a scalar multiple but a genuine change of the form.

**A caution on the word isometry.** The isometry group of a form, read in the standard linear sense as the full group of linear maps that preserve it, is far larger than the $*$-unitary group, and it is not one group but three: $O_4(\mathbb{C})$ of real dimension twelve for the two bilinear forms, $\mathrm{U}(4)$ of real dimension sixteen and compact for the general plain sesquilinear form, and $\mathrm{U}(1,3)$ of real dimension sixteen and non-compact for the Krein form. What the unitaries supply is not one of those groups but the **inner isometries**, the conjugations by an element of the algebra, and because the central phase acts trivially the acting group is $PU(2)\cong SO(3)$, of real dimension three. The two statements do not compete, and a reader should hold both: every conjugation by a $*$-unitary is an isometry of each of the four forms, and the isometry group of each form is very much larger than the image of the $*$-unitary group. The sharper form of the first statement is that these inner isometries are exactly the isometries that also preserve the algebra's multiplication — the $\mathbb{C}$-linear isometries preserving the product are the inner ones and no others. That is why the four forms survive a $*$-unitary conjugation together: the reason is not an accident of the coefficients, it is that the conjugation is an automorphism of the algebra as well as an isometry of the forms, and the four forms are four dressings of the one product that the automorphism preserves.

**A remark on the direction of the two accounts.** Theorem 1 is a statement about the algebra's own conjugation action: it says which inner maps are automorphisms. Theorem 2 is a statement about the determinant: it says that the biquaternion norm detects $\tilde Q$ only through the central number $\langle\tilde Q\rangle_{\natural}$. The two are related by the fact that the unitaries are precisely the elements with $\langle\tilde Q\rangle_{\natural}$ a unit-modulus central scalar **and** $\tilde Q^{*}\tilde Q=e_t$, the second condition being the genuinely non-abelian one. In the centre, equality cannot distinguish $\mathrm{U}(2)$ from $G_N$; the non-central defect $\tilde Q^{*}\tilde Q$ is what does.

## Worked Examples and Counterexamples

The following computations exhibit each hypothesis failing when it is dropped.

**Example 1: a non-$*$-unitary element of unit norm.** Take $\tilde U_{\mathrm L}=\mathrm{diag}(\lambda,\lambda^{-1})$ in the matrix model with $\lambda>0$, $\lambda\neq1$; equivalently $\tilde U_{\mathrm L}=\cosh t\,e_t+i\sinh t\,\vec e_z$ in the algebra, with $\lambda=\exp(t)$, which the matrix model sends to $\mathrm{diag}(\exp(t),\exp(-t))$. Its determinant is $1$, so $\langle\tilde U_{\mathrm L}\rangle_{\natural}=e_t$ and Theorem 2's hypothesis holds: the biquaternion norm is preserved. But
$$
\tilde U_{\mathrm L}^{*}\tilde U_{\mathrm L}=\mathrm{diag}(\lambda^2,\lambda^{-2}),
$$
which is not central for $\lambda\neq1$, so $\Gamma_{\tilde U_{\mathrm L}}$ is not multiplicative and does not preserve the Hermitian norm. Concretely, on the pure state $\tilde\Pi=\tfrac12(e_t+i \vec e_x)$ the trace pairing of $\tilde\Pi$ with itself is $1$ before and $\mathrm{Tr}(\Gamma_{\tilde U_{\mathrm L}}\tilde\Pi)^2=\tfrac14(\lambda^2+\lambda^{-2})^2=\cosh^2 2t$ after, while the biquaternion norm $\langle\cdot\rangle_{\natural}$ stays at $0$ on this null element. The example makes the two norms' disagreement explicit: the biquaternion norm sees only the determinant, and the determinant is blind to $\lambda$.

**Example 2: a central scaling.** Take $\tilde Q=\lambda_t e_t$ with $\lambda_t>0$, $\lambda_t\neq1$. This defect is central, $\tilde Q^{*}\tilde Q=\lambda_t^2e_t$, so $\Gamma_{\tilde Q}$ is a homomorphism up to the central scalar $\lambda_t^2$: for all $\tilde Q_1,\tilde Q_1$,
$$
\Gamma_{\tilde Q}(\tilde Q_1)\Gamma_{\tilde Q}(\tilde Q_1)=\lambda_t^2\,\Gamma_{\tilde Q}(\tilde Q_1\tilde Q_1),
\qquad
\Gamma_{\tilde Q}(\tilde Q_1)=\lambda_t^2\tilde Q_1.
$$
The biquaternion norm scales as $\langle\Gamma_{\tilde Q}\tilde Q_1\rangle_{\natural}=\lambda_t^4\langle\tilde Q_1\rangle_{\natural} = \langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=\bigl|\lambda_t^2\bigr|^2\langle\tilde Q_1\rangle_{\natural}$, in agreement with Theorem 2 with $|\langle\tilde Q\rangle_{\natural}|=|\lambda_t^2|=\lambda_t^2$. The Hermitian norm scales by $\lambda_t^4$ and is not preserved. This example shows that *centrality of the defect is not enough for unitarity*: it removes the operator-valued part of the anomaly and leaves a scalar, and the scalar must be normalized to one. It is the precise counterpart, in the multiplicative direction, of the statement that a central root of $-e_t$ must be normalized to be $\pm i$.

**Example 3: a non-central root of $-e_t$.** Take $J=\vec e_z$, so $J^2=-e_t$, and take the Hermitian generator $\tilde{H}=i \vec e_x$ (i.e. $\vec h=(1,0,0)$). Then, with the flow generator $G=-\hbar^{-1}J\tilde{H}$,
$$
G=-\hbar^{-1}\vec e_z\,i\vec e_x=-\hbar^{-1}i\,\vec e_z \vec e_x=-\hbar^{-1}i\,\vec e_y .
$$
Now $i\vec e_y$ is Hermitian, since $(i\vec e_y)^{*}=i\vec e_y$, so $G$ is Hermitian rather than anti-Hermitian, and the one-parameter group it generates is the hyperbolic element
$$
\exp(Gt')=\cosh(\hbar^{-1}t')\,e_t-\sinh(\hbar^{-1}t')\,i\vec e_y ,
$$
which is not $*$-unitary: because $G^2=\hbar^{-2}e_t$, the hyperbolic functions replace the trigonometric ones, and
$$
\exp(Gt')^\dagger\exp(Gt')=\cosh(2\hbar^{-1}t')\,e_t-\sinh(2\hbar^{-1}t')\,i\vec e_y ,
\qquad
\mathrm{Tr}\bigl(\exp(Gt')^\dagger\exp(Gt')\bigr)=2\cosh(2\hbar^{-1}t'),
$$
which grows without bound, so the Hermitian norm of a state is not preserved. Its biquaternion norm, by contrast, is $\langle \exp Gt'\rangle_{\natural}=\bigl(\cosh^2\hbar^{-1}t'-\sinh^2\hbar^{-1}t'\bigr)e_t=e_t$, so this non-$*$-unitary element has $|\langle\exp Gt'\rangle_{\natural}|=1$ and is exactly the kind of element Theorem 2 allows. The failure is exactly the non-commutation of $J=\vec e_z$ with the Hermitian element $i\vec e_x$; it is the non-centrality of the unit that breaks the norm. The computation is the flow version, developed next.

**Example 4: an accidental invariance.** If one tests norm preservation only on a single fixed element, non-$*$-unitary elements can appear to preserve it. With $\tilde Q_1=\tilde\Pi(\vec u)$ and $\tilde Q$ a rotation element of $G_N$ that happens to fix $\vec u$, the Hermitian norm of that particular $\tilde Q_1$ can be unchanged even though $\Gamma_{\tilde Q}$ is not $*$-unitary. The quantifier "for all $\tilde Q_1$" in Theorem 1 is therefore essential, and the numerical checks of this article were run on random superpositions precisely to avoid this accident.

## Unitarity from Centrality: the Flow

The norm-preservation theorem of the preceding sections is algebraic: it is about the conjugation action on the algebra. Its dynamical counterpart is the statement that the unit of the Schrödinger equation is forced to be central if the norm is to be preserved for every generator.

**The state-vector equation.** In the state module $\mathbb{B}\tilde\Pi_1$, the equation is
$$
i\hbar\,\partial/\partial t'\psi=J\tilde{H}\psi ,
\qquad
J^2=-e_t,\quad \tilde{H}\in\mathbb{M}_+,
$$
with $J$ a root of $-e_t$ and $\tilde{H}$ Hermitian. The solution, for constant $\tilde{H}$, is
$$
\psi(t')=\exp\bigl(Gt'\bigr)\psi(0),
\qquad
G=-\hbar^{-1}J\tilde{H}.
$$
The norm $\mathrm{Tr}(\psi^\dagger\psi)$ is preserved for all $t'$ and all $\psi(0)$ exactly when $G$ is anti-Hermitian,
$$
\frac{d}{dt'}\mathrm{Tr}\bigl(\psi^\dagger\psi\bigr)
=\mathrm{Tr}\bigl(\psi^\dagger(G^{*}+G)\psi\bigr)
=0\ \ \text{for all }\psi
\iff G^{*}=-G .
$$

**Theorem 3.** Let $J$ be a root of $-e_t$. The flow generated by $G=-\hbar^{-1}J\tilde{H}$ is norm-preserving for **every** Hermitian $\tilde{H}$ if and only if $J$ is central. In that case $J=\pm i$, and the flow is the standard $*$-unitary one.

**Proof.** The hypothesis is that $G^{*}=-G$ for every Hermitian $\tilde{H}$. Since $\tilde{H}^{*}=\tilde{H}$,
$$
G^{*}=-\hbar^{-1}\tilde{H}J^\dagger,
\qquad
-G=+\hbar^{-1}J\tilde{H},
$$
so the hypothesis reads $-\tilde{H}J^\dagger=J\tilde{H}$ for every Hermitian $\tilde{H}$. Evaluating it at $\tilde{H}=e_t$ gives $J^\dagger=-J$, so a root of $-e_t$ that generates a norm-preserving flow is necessarily anti-Hermitian; with that, and only with that, the condition becomes $\tilde{H}J=J\tilde{H}$. This must hold for every Hermitian $\tilde{H}$. The Hermitian elements span $\mathbb{M}_+=\mathrm{span}_\mathbb{R}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$, whose real span together with $i$ spans all of $\mathbb{B}$; since $J$ commutes with $e_t$ and with every $i\vec e_k$, it commutes with every element of $\mathbb{B}$, i.e. $J$ is central. The centre is $\mathbb{C}_{\mathbb{B}}=Z(\mathbb{B})=\mathrm{span}_\mathbb{R}\{e_t,ie_t\}$, and its elements are $\lambda e_t$ with $\lambda\in\mathbb{C}$; the condition $J^2=-e_t$ gives $\lambda^2=-1$, hence $\lambda=\pm i$. Conversely, for $J=\pm i$ the generator $G=\mp\hbar^{-1}i\tilde{H}$ is anti-Hermitian because $\tilde{H}$ Hermitian implies $i\tilde{H}$ anti-Hermitian, and the exponential $\exp(Gt')$ is $*$-unitary.

**Where the centrality is used.** The hypothesis "for every Hermitian $\tilde{H}$" is what forces $J$ into the centre, and it is not a technical convenience. Physically, a dynamics must be norm-preserving for the whole class of Hamiltonians the theory admits, not merely for one particular $\tilde{H}$; the theory admits every Hermitian element as a possible generator. Mathematically, one non-central root is enough to violate the norm, and Example 3 exhibits the violation: with $J=\vec e_z$ and $\tilde{H}=i\vec e_x$, the generator is Hermitian rather than anti-Hermitian, so the exponential is not $*$-unitary.

**The structural interpretation.** Theorem 3 says that the norm-preserving unit of the dynamics is *the* central root of $-e_t$, and the centre's role here is different from its two earlier roles. In the multiplicative theorem the centre was where the defect had to live for the anomaly to be scalar; in the biquaternion-norm theorem the centre was the target space of the biquaternion norm. Here the centre is where the *unit* must live, and it is the only place where a root of $-e_t$ is compatible with invariance under the full symmetry of the state space. The three roles are the same fact seen from three sides: the centre is the maximal commutative subalgebra, and every statement that must hold "uniformly" over a non-commutative family collapses to a statement about the centre.

**A corollary on the field.** The theorem also shows what fixes the scalar field at $\mathbb{C}$: a norm-preserving unit is forced into the centre whenever the Hermitian generators are rich enough to generate the algebra, which is the case here, since $\mathbb{M}_+$ together with $i$ spans $\mathbb{B}$. The hypothesis is not idle. Over the real quaternions the conjugation-Hermitian elements are only the reals, too few to generate the algebra, and a non-central root of $-e_t$ — $\vec e_x$, say — generates a norm-preserving flow for the central generators $a e_t$; the same happens within $\mathbb{B}$ itself whenever the Hamiltonian is restricted to the central directions, since $G=-\hbar^{-1}\vec e_x a=-\hbar^{-1}a\,\vec e_x$ is anti-Hermitian and its exponential is $*$-unitary. What a non-central unit cannot do is preserve the norm for **every** Hermitian generator, and that too is visible at once: with $J=\vec e_z$ and $\tilde{H}=i\vec e_x$ the generator is $-i\vec e_y$, Hermitian rather than anti-Hermitian, and the norm grows as in Example 3. Given the full set of generators the unit is central, and a central unit with $J^2=-1$ exists precisely when the centre contains a square root of $-1$. In $\mathbb{B}$ the centre is $\mathbb{C}$, whose two roots are $\pm i$; this is the algebraic content of the standard statement that the complex numbers are sufficient for quantum theory.

## What Is Standard and What Is the Algebra's

The results above divide into a standard linear-algebra part and an algebraic part, and the division should be stated rather than left implicit.

**Standard.** The identification of the Hilbert–Schmidt isometries of a matrix algebra under congruence with the $*$-unitary group is standard; the multiplicativity of the determinant and the behaviour of the determinant under the adjoint, $\det(A^\dagger)=\det(A)^{*}$, are standard; the isomorphism of the unit-norm group $SL(2,\mathbb{C})$ with the double cover of the Lorentz group is standard, and so is the fact that the $*$-unitary group is the norm-preserving group of quantum physics. The companion articles on the Schrödinger equation and on angular momentum already use these facts, and nothing here re-derives them.

**The algebra's.** Three statements are genuinely about $\mathbb{B}$ and its structure, and they are the content the framework adds.

First, the **coexistence of the two norms on the same eight-real-dimensional algebra** is specific to the biquaternion setting: the Hermitian norm is the Hilbert–Schmidt form of the matrix model, while the biquaternion norm is its determinant, and the two live on the same elements with different target spaces ($\mathbb{R}$ and $\mathbb{C}_{\mathbb{B}}$). A purely complex matrix algebra has the first as its operator norm source and the second as its determinant, but it does not have the second as a *norm on the algebra* in the sense used here, because the determinant of a complex matrix is not a positive form; the biquaternion realization makes the determinant into a Hermitian-valued quadratic form whose scalar part is the Minkowski form.

Second, the **centrality criterion for multiplicativity** is the framework's own statement: an inner map of $\mathbb{B}$ given by conjugation is multiplicative exactly when its defect $\tilde Q^{*}\tilde Q$ is the unit, and multiplicative up to a scalar exactly when that defect is central. This is the precise algebraic form of the familiar fact that a non-$*$-unitary conjugation is not an automorphism, and it is what makes the word *centrality* the right one for the phenomenon: the obstruction to multiplicativity is measured by an element of the algebra, and it is scalar exactly when that element lies in the centre.

Third, the **forced centrality of the unit in the dynamics** is algebraic in a way that its complex counterpart is not. In the complex theory one simply postulates $i$ and checks that $i\tilde{H}$ is anti-Hermitian; because there is only one imaginary unit available, the question of centrality does not arise. In $\mathbb{B}$ the anti-Hermitian roots of $-e_t$ — the roots that can serve as the unit of a norm-preserving dynamics — are the two central ones $\pm i$ together with the infinitely many unit pure real quaternions, and the requirement of norm preservation for all generators selects the centre. The selection is a theorem in this framework, and it is what connects the norm-preservation theorem to the identification of the centre as the classical sector.

**A limit.** Theorems 1 and 3 are, at bottom, standard facts about the $*$-unitary group, dressed in the algebra's coordinates. Their value is not that they produce a new group but that they locate the framework's unitarity precisely: it is the unitarity of the matrix model, its group is $\mathrm{U}(2)$ acting by conjugation, and the extra group $G_N=\mathrm{U}(1)\cdot SL(2,\mathbb{C})$ that preserves the biquaternion norm is the group of elements whose determinant has modulus one — which is not a group of quantum symmetries but a statement about the determinant. A reader should not read the larger group as a larger class of allowed quantum evolutions; the companion article *What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions* is concerned to prevent exactly that interpretation.

## Summary

The biquaternion algebra carries two quadratic forms, and unambiguity about which one is being preserved is the whole content of the norm-preservation theorem. The Hermitian norm $\mathrm{Tr}(\tilde Q_1^{*}\tilde Q_1)$ is real, positive definite, and preserved by the conjugation action $\Gamma_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$ exactly when $\tilde Q$ is $*$-unitary; that is Theorem 1, and it is the framework's statement of unitarity. The biquaternion norm $\langle\tilde Q_1\rangle_{\natural} = \langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=\tilde Q_1\tilde Q_1^{\natural}$ is central-valued and indefinite, and under the same action it scales by a **central** scalar,

$$
\langle\Gamma_{\tilde Q}\tilde Q_1\rangle_{\natural}=\bigl|\langle\tilde Q\rangle_{\natural}\bigr|^2\langle\tilde Q_1\rangle_{\natural},
$$

so it is preserved exactly when $|\langle\tilde Q\rangle_{\natural}|=1$; that is Theorem 2, and its group is the seven-real-dimensional $G_N=\mathrm{U}(1)\cdot SL(2,\mathbb{C})$, which contains $\mathrm{U}(2)$; the intersection is $\mathrm{U}(2)$ itself, while $\mathrm{U}(2)\cap SL(2,\mathbb{C})=SU(2)$.

The centrality theme is carried by the defect $\tilde Q_4=\tilde Q^{*}\tilde Q$. The action is multiplicative exactly when $\tilde Q_4=e_t$, i.e. exactly when $\tilde Q$ is $*$-unitary and $\Gamma_{\tilde Q}$ is an automorphism; when $\tilde Q_4$ is central the multiplicative anomaly collapses to the scalar $\tilde Q_4$, and the centre is precisely the locus where that collapse occurs. The same collapse governs the dynamics: the generator $G=-\hbar^{-1}J\tilde{H}$ is anti-Hermitian for every Hermitian $\tilde{H}$ if and only if the root $J$ of $-e_t$ is central, and the only central roots are $\pm i$, so the unit of the Schrödinger equation is forced into the centre of the algebra. Unitarity, in this framework, is a centrality statement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| ${}^{*}={}^{\natural}\circ\bar{\cdot}$ | Hermitian conjugation |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $\mathbb{C}_{\mathbb{B}}=Z(\mathbb{B})=\mathrm{span}_\mathbb{R}\{e_t,ie_t\}$ | Centre of $\mathbb{B}$; the series symbol is $\mathbb{C}_{\mathbb{B}}$ |
| $\mathrm{Tr}(\tilde Q_1)=2\,\mathrm{Sc}(\tilde Q_1)$ | Trace, $\mathrm{Tr}(e_t)=2$ |
| $\langle\tilde Q_1\rangle_{\natural} = \langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=\tilde Q_1\tilde Q_1^{\natural}$ | Biquaternion norm, centre-valued |
| $\langle\tilde Q_1,\tilde Q_1\rangle_{*}=\mathrm{Tr}(\tilde Q_1^{*}\tilde Q_1)$ | Hermitian (Hilbert–Schmidt) pairing |
| $\Gamma_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$ | Conjugation action |
| $\tilde Q_4=\tilde Q^{*}\tilde Q$ | Defect of the action |
| $\mathrm{U}(2)=\{\tilde Q:\tilde Q^{*}\tilde Q=e_t\}$ | $*$-Unitary group; preserves the Hermitian norm |
| $SL(2,\mathbb{C})=\{\tilde U_{\mathrm L}:\langle\tilde U_{\mathrm L}\rangle_{\natural}=e_t\}$ | Unit-norm group; the Lorentz rotor |
| $G_N=\{\tilde Q:|\langle\tilde Q\rangle_{\natural}|=1\}=\mathrm{U}(1)\cdot SL(2,\mathbb{C})$ | Exact biquaternion-norm-preserving group |
| $J$ | Root of $-e_t$, $J^2=-e_t$ |
| $G=-\hbar^{-1}J\tilde{H}$ | Generator of the state-vector flow |
| $M(\tilde Q_1)$ | $2\times2$ matrix model, $\mathsf{M}_2(e_t)=I_2$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\mathbb{C}$-linear |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$; on the diagonal $\langle\tilde Q_2,\tilde Q_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ |

## Further Reading

- S. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford University Press, 1995), for the quaternionic formulation of quantum physics, its unitarity conditions, and the role of the norm.
- D. Finkelstein, J. M. Jauch, S. Schiminovich, and D. Speiser, "Foundations of quaternion quantum mechanics", *Journal of Mathematical Physics* **3**, 207 (1962), for the original algebraic treatment of quaternionic quantum theory and its scalar field.
- G. Birkhoff and J. von Neumann, "The logic of quantum mechanics", *Annals of Mathematics* **37**, 823 (1936), for the argument that the complex field is the appropriate scalar field and the role of a central imaginary unit.
- A. Sudbery, "Quaternionic analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85**, 199 (1979), for the analysis of quaternionic and biquaternionic linear algebra, determinants, and the unimodular group.
- E. Artin, *Geometric Algebra* (Interscience, 1957), for the biquaternion norm, its multiplicativity, and the identification of the unit-norm group with the double cover of the Lorentz group.
- K. Hoffman and R. Kunze, *Linear Algebra* (Prentice-Hall, 2nd ed., 1971), for the multiplicativity of the determinant and the determinant of the adjoint.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 2000), for $*$-unitary evolution, norm preservation, and the Hilbert–Schmidt inner product.
- A. W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2nd ed., 2002), for the structure of $\mathrm{U}(2)$, $SU(2)$, and $SL(2,\mathbb{C})$ and their real dimensions.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed., 2001), for the matrix representation of the quaternion and biquaternion algebras and the identification $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$.
