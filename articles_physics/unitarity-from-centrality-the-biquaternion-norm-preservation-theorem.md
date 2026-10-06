# __Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem__

## Introduction

Unitarity is the statement that the norm of a state does not change in time. In the biquaternion framework there are two norms on the algebra, and they behave differently: the **Hermitian norm** $\mathrm{Tr}(\tilde{Q}^{*}\tilde{Q})$, which is positive definite and is the norm that Born probabilities are built from, and the **biquaternion norm** $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}$, which is central-valued and indefinite. This article asks, for each of them, under exactly which elements of $\mathbb{B}$ the conjugation action
$$
\Gamma_{\tilde{U}}(\tilde{Q})=\tilde{U}\tilde{Q}\tilde{U}^{*}
$$
preserves it. The answer is a norm-preservation theorem with a single organising theme: **the conditions are conditions on the centre of the algebra.**

Three statements are proved. The first is that $\Gamma_{\tilde{U}}$ preserves the Hermitian norm if and only if $\tilde{U}$ is unitary, $\tilde{U}\tilde{U}^{*}=e_0$. The second is that $\Gamma_{\tilde{U}}$ scales the biquaternion norm by a **central scalar**,
$$
N\bigl(\Gamma_{\tilde{U}}\tilde{Q}\bigr)=\bigl|N(\tilde{U})\bigr|^2\,N(\tilde{Q}),
$$
so that it preserves the biquaternion norm exactly when $|N(\tilde{U})|=1$, i.e. when $N(\tilde{U})$ lies on the unit circle of the centre $\mathbb{C}_{\mathbb{B}}$. The third is the structural reason behind the word *centrality* in the title: the product $\tilde{U}^{*}\tilde{U}$, which measures the failure of $\Gamma_{\tilde{U}}$ to be multiplicative, is central if and only if that failure is a scalar rather than an operator-valued anomaly; and it equals $e_0$ — the case of a genuine algebra automorphism — if and only if $\tilde{U}$ is unitary. Thus

$$
\Gamma_{\tilde{U}}\ \text{is multiplicative} \iff \tilde{U}^{*}\tilde{U}=e_0 \iff \tilde{U}\ \text{unitary},
$$

and the intermediate case $\tilde{U}^{*}\tilde{U}=\lambda e_0$ with central $\lambda$ is a homomorphism up to the central scalar $\lambda$.

The same theme governs the dynamics. The state-vector equation requires a unit $J$ with $J^2=-e_0$ and a Hermitian generator $\tilde{H}$; the flow it generates preserves the Hermitian norm **for every Hermitian $\tilde{H}$** if and only if $J$ commutes with every Hermitian element, i.e. if and only if $J$ is central. The centre contains exactly the two roots $\pm i$, so the norm-preserving unit of the Schrödinger equation is forced to be the scalar imaginary. This is the precise sense of the title: unitarity follows from centrality.

The article is organised as follows. The two norms are written down and their natures contrasted; the conjugation action and its defect are introduced; the two norm-preservation theorems are proved; the norm-preserving groups are identified as $U(2)$ for the Hermitian norm and $U(1)\cdot SL(2,\mathbb{C})$ for the biquaternion norm, the second containing the first, so that the intersection of the two is $U(2)$ itself while $U(2)\cap SL(2,\mathbb{C})=SU(2)$; the flow version and the forced centrality of the unit are proved; and the standard and algebraic parts of the result are separated. Worked counterexamples show what fails when the centrality hypothesis is dropped.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=\epsilon_{jkl}e_l$ for $j\neq k$, and central $i$ with $i^2=-1$. Conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (complex), ${}^{*}={}^{\natural}\circ\bar{\cdot}$ (Hermitian), and $\flat=-{}^{*}$. The Hermitian and anti-Hermitian subspaces are
$$
\mathbb{M}_+=\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\},
\qquad
\mathbb{M}_-=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\},
\qquad
\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_- .
$$
The centre is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}\cong\mathbb{C}$. The trace is $\mathrm{Tr}(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})$ with $\mathrm{Tr}(e_0)=2$, the biquaternion norm is $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}$, and on $\mathbb{M}_+$ with $\tilde{H}=h_0e_0+i\mathbf{h}$ one has $N(\tilde{H})=(h_0^2-|\mathbf{h}|^2)e_0$. The matrix model is the $\mathbb{C}$-linear representation $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, under which $\Phi(\mathbb{B})=M_2(\mathbb{C})$ and $\det M(\tilde{Q})=N(\tilde{Q})$. A root of $-e_0$ is an element $\xi$ with $\xi^2=-e_0$. The roots that can serve as the unit of a norm-preserving dynamics are the **anti-Hermitian** ones, $\xi^{*}=-\xi$; among these the central roots are $\pm i$ and the rest are the unit pure real quaternions. A general root of $-e_0$ need not be anti-Hermitian, as $\xi=e_1+ie_2-e_3$ shows, and the condition of norm preservation at $\tilde{H}=e_0$ is what forces $\xi^{*}=-\xi$. A state is $\tilde{\rho}=\tfrac12(e_0+i\mathbf{r})$ and a pure state is $\tilde\Pi(\hat{\mu})=\tfrac12(e_0+i\hat{\mu})$.

## The Two Norms

The word "norm" carries two distinct objects in this framework, and the whole article turns on not confusing them.

**The Hermitian norm.** For $\tilde{Q},\tilde{Y}\in\mathbb{B}$ define
$$
\langle\tilde{Q},\tilde{Y}\rangle_{\dagger}=\mathrm{Tr}\bigl(\tilde{Q}^{*}\tilde{Y}\bigr),
\qquad
\|\tilde{Q}\|_{\dagger}^2=\mathrm{Tr}\bigl(\tilde{Q}^{*}\tilde{Q}\bigr).
$$
Writing $\tilde{Q}=x_0e_0+x_1e_1+x_2e_2+x_3e_3$ with $x_\mu\in\mathbb{C}$ and using $\tilde{Q}^{*}=x_0^{*}e_0-x_1^{*}e_1-x_2^{*}e_2-x_3^{*}e_3$, one finds
$$
\|\tilde{Q}\|_{\dagger}^2
=2\bigl(|x_0|^2+|x_1|^2+|x_2|^2+|x_3|^2\bigr)>0\quad(\tilde{Q}\neq0).
$$
This form is positive definite of signature $(8,0)$ on the real eight-dimensional algebra. It is the Hilbert–Schmidt form of the matrix model, $\langle \tilde{Q},\tilde{Y}\rangle_{}^{*}=\mathrm{tr}(M(\tilde{Q})^\dagger M(\tilde{Y}))$ with $\mathrm{tr}$ the ordinary $2\times2$ matrix trace, and its restriction to the state module is the quantity $\mathrm{Tr}(\psi^\dagger\psi)$ that normalizes spinors. This is the norm whose preservation is the unitarity statement of quantum physics: the Born probability $\mathrm{Tr}(\tilde{P}\tilde{H})$ is written with the trace, and the trace pairing $\mathrm{Tr}(\tilde{P}\tilde{Q})$ of two states is the boundary case of this norm.

**The biquaternion norm.** The second object is
$$
N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\bigl(x_0^2+x_1^2+x_2^2+x_3^2\bigr)e_0\in\mathbb{C}_{\mathbb{B}},
$$
a quadratic form with values in the **centre**, not in $\mathbb{R}$. Its coefficient is the determinant of the matrix model, $N(\tilde{Q})e_0=\det M(\tilde{Q})\,e_0$, so $N$ is multiplicative,
$$
N(\tilde{Q}\tilde{Y})=N(\tilde{Q})N(\tilde{Y}),
$$
and it is indefinite on $\mathbb{M}_+$: for $\tilde{H}=h_0e_0+i\mathbf{h}$ one has $N(\tilde{H})=(h_0^2-|\mathbf{h}|^2)e_0$, of signature $(1,3)$. Its null cone is the pure-state boundary of the Bloch ball.

The two norms differ in every structural respect that matters here. The Hermitian norm is real-valued and positive definite; the biquaternion norm is centre-valued and indefinite. The Hermitian norm is preserved by the left action of the unitaries on the state module; the biquaternion norm is preserved by the left action of the unit-norm elements $SL(2,\mathbb{C})$. The Hermitian norm detects the state; the biquaternion norm detects the determinant. A reader who asks "which norm does the framework use" is asking a question with two correct answers, and the answer depends on whether the object at hand is a state overlap or a determinant.

## The Conjugation Action and Its Defect

The action studied throughout is conjugation by an invertible element,
$$
\Gamma_{\tilde{U}}(\tilde{Q})=\tilde{U}\tilde{Q}\tilde{U}^{*},
\qquad
\tilde{U}\in\mathbb{B}^{\times}.
$$
It has the following elementary properties, each immediate from the definitions.

**It preserves Hermiticity.** Since ${}^{*}$ is an anti-automorphism,
$$
\Gamma_{\tilde{U}}(\tilde{Q})^{*}=\tilde{U}\tilde{Q}^{*}\tilde{U}^{*}=\Gamma_{\tilde{U}}\bigl(\tilde{Q}^{*}\bigr),
$$
so Hermitian elements go to Hermitian elements and anti-Hermitian to anti-Hermitian. In particular $\Gamma_{\tilde{U}}$ acts on $\mathbb{M}_+$ and on the state space, and it maps the positive cone to itself, because a congruence by an invertible element preserves the signature.

**It fixes the unit only for unitaries.** Evaluating at $e_0$,
$$
\Gamma_{\tilde{U}}(e_0)=\tilde{U}\tilde{U}^{*} .
$$
So the action is unital, $\Gamma_{\tilde{U}}(e_0)=e_0$, if and only if $\tilde{U}\tilde{U}^{*}=e_0$, i.e. if and only if $\tilde{U}$ is unitary.

**Its defect is $\tilde{U}^{*}\tilde{U}$.** Compute the product of two images:
$$
\Gamma_{\tilde{U}}(\tilde{Q})\,\Gamma_{\tilde{U}}(\tilde{Y})
=\tilde{U}\tilde{Q}\tilde{U}^{*}\tilde{U}\tilde{Y}\tilde{U}^{*}
=\tilde{U}\tilde{Q}\bigl(\tilde{U}^{*}\tilde{U}\bigr)\tilde{Y}\tilde{U}^{*} .
$$
Compare with $\Gamma_{\tilde{U}}(\tilde{Q}\tilde{Y})=\tilde{U}\tilde{Q}\tilde{Y}\tilde{U}^{*}$. The two agree for all $\tilde{Q},\tilde{Y}$ if and only if
$$
\tilde{U}^{*}\tilde{U}\,\tilde{Y}=\tilde{Y}\qquad\text{for all }\tilde{Y},
$$
which holds if and only if $\tilde{U}^{*}\tilde{U}=e_0$. This is the **defect** of the action.

**The centrality statement.** If the defect is central, $\tilde{U}^{*}\tilde{U}=\lambda e_0$ with $\lambda\in\mathbb{C}_{\mathbb{B}}$, then it commutes past $\tilde{Y}$ and
$$
\Gamma_{\tilde{U}}(\tilde{Q})\Gamma_{\tilde{U}}(\tilde{Y})
=\lambda\,\Gamma_{\tilde{U}}(\tilde{Q}\tilde{Y}),
$$
so that $\Gamma_{\tilde{U}}$ is an algebra homomorphism **up to the central scalar $\lambda$**. The failure of multiplicativity is then a scalar — the same number for every pair $\tilde{Q},\tilde{Y}$ — rather than an operator-valued anomaly that distorts each product differently. Centrality of the defect is exactly the condition that the anomaly is scalar; and the scalar is $1$, i.e. the action is multiplicative, exactly when $\tilde{U}$ is unitary:
$$
\Gamma_{\tilde{U}}\text{ multiplicative}
\iff \tilde{U}^{*}\tilde{U}=e_0
\iff \tilde{U}\text{ unitary}.
$$
This is the first appearance of the centre in the norm-preservation problem, and it is the structural core of the article. Note that $\tilde{U}^{*}\tilde{U}$ is automatically **Hermitian and positive**, $(\tilde{U}^{*}\tilde{U})^{*}=\tilde{U}^{*}\tilde{U}$, so when it is central it is $\lambda e_0$ with $\lambda\in\mathbb{R}$ and $\lambda>0$ for $\tilde{U}\neq0$; the central defect is a positive real scalar multiple of the identity, and unitarity is its normalization to $1$.

## The Norm-Preservation Theorem

The two parts of the theorem are stated and proved separately, because they have different hypotheses and different content.

### Part 1: the Hermitian norm

**Theorem 1.** Let $\tilde{U}\in\mathbb{B}^{\times}$. The conjugation $\Gamma_{\tilde{U}}$ preserves the Hermitian norm for all $\tilde{Q}$,
$$
\mathrm{Tr}\bigl(\Gamma_{\tilde{U}}(\tilde{Q})^{*}\,\Gamma_{\tilde{U}}(\tilde{Q})\bigr)=\mathrm{Tr}\bigl(\tilde{Q}^{*}\tilde{Q}\bigr)
\qquad\text{for all }\tilde{Q},
$$
if and only if $\tilde{U}$ is unitary, $\tilde{U}^{*}\tilde{U}=e_0$.

**Proof.** Write $\tilde{Z}=\tilde{U}^{*}\tilde{U}$, which is Hermitian and positive. Since $\Gamma_{\tilde{U}}(\tilde{Q})^{*}=\tilde{U}\tilde{Q}^{*}\tilde{U}^{*}$,
$$
\mathrm{Tr}\bigl(\Gamma_{\tilde{U}}(\tilde{Q})^{*}\Gamma_{\tilde{U}}(\tilde{Q})\bigr)
=\mathrm{Tr}\bigl(\tilde{U}\tilde{Q}^{*}\tilde{U}^{*}\tilde{U}\tilde{Q}\tilde{U}^{*}\bigr)
=\mathrm{Tr}\bigl(\tilde{Q}^{*}\tilde{Z}\tilde{Q}\tilde{Z}\bigr),
$$
using the cyclicity of the trace twice. If $\tilde{Z}=e_0$ this is $\mathrm{Tr}(\tilde{Q}^{*}\tilde{Q})$, so unitarity is sufficient. Conversely, suppose the identity holds for all $\tilde{Q}$ and take $\tilde{Q}$ rank one, $\tilde{Q}=|\varphi\rangle\langle\varphi|$ in the matrix model. Then $\tilde{Q}^{*}\tilde{Z}\tilde{Q}=\langle\varphi|\tilde{Z}\varphi\rangle\,|\varphi\rangle\langle\varphi|$ and
$$
\mathrm{Tr}\bigl(\tilde{Q}^{*}\tilde{Z}\tilde{Q}\tilde{Z}\bigr)
=\langle\varphi|\tilde{Z}\varphi\rangle\,\mathrm{Tr}\bigl(|\varphi\rangle\langle\varphi|\tilde{Z}\bigr)
=\langle\varphi|\tilde{Z}\varphi\rangle^2 .
$$
The preserved value is $\mathrm{Tr}(\tilde{Q}^{*}\tilde{Q})=1$, so $\langle\varphi|\tilde{Z}\varphi\rangle^2=1$ for every unit $\varphi$; positivity gives $\langle\varphi|\tilde{Z}\varphi\rangle=1$ for all unit $\varphi$, hence $\tilde{Z}=e_0$.

The theorem extends from the norm to the pairing by polarization, and it extends to the trace pairing $\mathrm{Tr}(\tilde{Q}\tilde{Y})$ on $\mathbb{M}_+$ by the same argument applied to Hermitian elements. The physical content is that the Born probabilities of two states are preserved under $\Gamma_{\tilde{U}}$ exactly when $\tilde{U}$ is unitary, which is the standard statement of unitarity in the framework's language.

### Part 2: the biquaternion norm

**Theorem 2.** Let $\tilde{U}\in\mathbb{B}^{\times}$. The conjugation scales the biquaternion norm by a central scalar,
$$
N\bigl(\Gamma_{\tilde{U}}(\tilde{Q})\bigr)=\bigl|N(\tilde{U})\bigr|^2\,N(\tilde{Q})
\qquad
\text{for all }\tilde{Q},
$$
where $|N(\tilde{U})|^2=N(\tilde{U})\,N(\tilde{U})^{*}$ is a non-negative real scalar, the complex conjugate being taken coefficientwise on the central element $N(\tilde{U})$. Consequently $\Gamma_{\tilde{U}}$ preserves the biquaternion norm if and only if
$$
\bigl|N(\tilde{U})\bigr|=1 ,
$$
i.e. if and only if the biquaternion norm of $\tilde{U}$ lies on the unit circle of the centre.

**Proof.** Under the matrix model, $M(\Gamma_{\tilde{U}}\tilde{Q})=M(\tilde{U})M(\tilde{Q})M(\tilde{U}^{*})$, and $M(\tilde{U}^{*})=M(\tilde{U})^\dagger$. The determinant is multiplicative and the determinant of the adjoint is the conjugate,
$$
\det M\bigl(\Gamma_{\tilde{U}}\tilde{Q}\bigr)
=\det M(\tilde{U})\,\det M(\tilde{Q})\,\det M(\tilde{U})^{*}
=\bigl|\det M(\tilde{U})\bigr|^2\det M(\tilde{Q}).
$$
Since $\det M(\tilde{Q})=N(\tilde{Q})$ for every $\tilde{Q}$, and since $N(\tilde{Q})e_0=\det M(\tilde{Q})\,e_0$, the stated identity follows. Preservation for all $\tilde{Q}$ is equivalent to $|N(\tilde{U})|^2=1$, i.e. $|N(\tilde{U})|=1$.

Two features of the proof are worth isolating. First, the scaling factor $|N(\tilde{U})|^2$ is a **central** scalar: it is a real non-negative multiple of $e_0$, so it commutes with everything and multiplies the biquaternion norm uniformly. The biquaternion norm of an element is itself central-valued, and its modulus is therefore a classical number; preservation of the biquaternion norm is a condition on that number. This is the second appearance of the centre, and it is of a different kind from the first: there the centre appeared as the condition for the multiplicative anomaly to be scalar, here as the target space of the biquaternion norm itself.

Second, the hypothesis $|N(\tilde{U})|=1$ is genuinely weaker than unitarity. A unitary $\tilde{U}$ has $|\det M(\tilde{U})|=1$, hence $|N(\tilde{U})|=1$, so every unitary preserves the biquaternion norm; but the converse fails, as the next section's counterexample shows. The two theorems are therefore not equivalent, and the difference between them is the difference between the quantum norm and the determinant.

### Putting the two together

The two preservation conditions can be read as statements about the same central defect. With $\tilde{Z}=\tilde{U}^{*}\tilde{U}$,
$$
\tilde{Z}=e_0\ \Longrightarrow\ \Gamma_{\tilde{U}}\text{ is an automorphism}\ \Longrightarrow\ \text{both norms preserved},
$$
and the converse implication holds for the Hermitian norm. For the biquaternion norm the condition is weaker, and the enlargement is exactly the group of elements whose determinant has modulus one. The next section identifies the two groups and their intersection.

## The Norm-Preserving Groups

The two theorems single out two groups of invertible elements, and their structure makes the relation between the norms explicit.

**The unitaries.** Define
$$
U(2)=\bigl\{\tilde{U}\in\mathbb{B}:\ \tilde{U}^{*}\tilde{U}=e_0\bigr\}.
$$
By Theorem 1 these are exactly the elements for which $\Gamma_{\tilde{U}}$ preserves the Hermitian norm, and for which $\Gamma_{\tilde{U}}$ is an algebra automorphism fixing the unit. In the matrix model they are the unitary $2\times 2$ matrices; on the state module they are the norm-preserving linear maps; on the Bloch sphere their conjugation image is the rotation group $SO(3)$, with kernel $\{\pm e_0\}$, the double cover of the companion article *Angular Momentum and Spin in Biquaternionic Form*.

**The unit-norm elements.** Define
$$
SL(2,\mathbb{C})=\bigl\{\tilde{U}\in\mathbb{B}:\ N(\tilde{U}) = \langle\tilde{U},\tilde{U}\rangle_{\natural}=e_0\bigr\}=\bigl\{\tilde{U}:\ \det M(\tilde{U})=1\bigr\},
$$
the elements of unit norm. By Theorem 2 these preserve the biquaternion norm, with the scaling factor exactly $1$; they need not be unitary, and they need not be norm-preserving for the Hermitian norm. This is the group that acts on the biquaternion norm, and it is the group that the companion articles on the algebra's real structure identify with the determinant-preserving transformations.

**The exact biquaternion-norm group.** Theorem 2 gives preservation of the biquaternion norm under the weaker condition $|N(\tilde{U})|=1$, and the group is
$$
G_N=\bigl\{\tilde{U}\in\mathbb{B}^{\times}:\ |N(\tilde{U})|=1\bigr\}.
$$
It contains $SL(2,\mathbb{C})$ as the subgroup with phase $1$, and every element factors as a central phase times a unit-norm element,
$$
G_N=U(1)\cdot SL(2,\mathbb{C}),
\qquad
\tilde{U}=\lambda\,\tilde{U}_0,\quad |\lambda|=1,\quad N(\tilde{U}_0)=e_0 ,
$$
because if $N(\tilde{U})=\mu e_0$ with $|\mu|=1$ then choosing $\lambda$ with $\lambda^2=\mu$ (possible since $\mu$ lies on the unit circle, which is divisible) gives $N(\tilde{U}/\lambda)=e_0$. The decomposition is not direct. The intersection consists of the central scalars that are at once of modulus one and of unit norm; a central scalar is $\lambda e_0$, and $N(\lambda e_0)=\lambda^2e_0$, so $|N|=1$ gives $|\lambda|=1$ while $N=e_0$ gives $\lambda=\pm1$, so the intersection is $\{\pm e_0\}$.

The real dimensions are worth recording. Over $\mathbb{R}$, the algebra is eight-dimensional; $SL(2,\mathbb{C})$ is the six-dimensional real group with one complex equation $N(\tilde{U})=e_0$ (two real conditions); the phase group adds one more real dimension, so $G_N$ is seven-real-dimensional; and $U(2)$ is four-real-dimensional. The inclusions are
$$
SU(2)=U(2)\cap SL(2,\mathbb{C})\ \subset\ U(2)\ \subset\ G_N=U(1)\cdot SL(2,\mathbb{C}),
$$
with $SU(2)$ the elements that are simultaneously unitary and of unit norm — the quaternionic unit sphere. The chain records the whole norm-preservation structure: the smallest group is the one that preserves both norms **and** the algebra's multiplication; enlarging to $U(2)$ keeps the Hermitian norm and the multiplication but gives up the unit-norm condition; enlarging to $G_N$ keeps only the biquaternion norm.

**The unitary group is not the unit sphere.** The unit group of a form is the set of elements on which the form takes the value $1$; the unitary group is the isometry group of the form under the conjugation action. For the sesquilinear form the second is the smaller, and the difference is a difference of equations. The defect $\tilde{U}\tilde{U}^{*}$ is Hermitian, so writing it as $z_0e_0+i\mathbf{z}$ with $z_0\in\mathbb{R}$ and $\mathbf{z}\in\mathbb{R}^3$,
$$
\tilde{U}\tilde{U}^{*}=e_0\iff z_0=1\ \text{and}\ \mathbf{z}=0,
\qquad
\langle\tilde{U},\tilde{U}\rangle_{*}=1\iff z_0=1 ,
$$
the sesquilinear norm reading the scalar part alone, $z_0=\mathrm{Sc}(\tilde{U}\tilde{U}^{*})=\sum_\mu\lvert U_\mu\rvert^2$ (*The Involutions and the Four Forms* of *Conventions in the Biquaternion Universe*). Unitarity is therefore the norm condition **together with** the vanishing of the vector part of the defect, and it implies the norm condition rather than following from it. The set $\{\tilde{U} : \langle\tilde{U},\tilde{U}\rangle_{*}=1\}$ is the unit sphere of $\mathbb{B}$ in the sesquilinear norm, of real dimension seven, and it is not a group; the unitary elements form its four-real-dimensional submanifold. The containment is the biquaternion case of the theorem of *The Unitary Slice and the Compact Real Form with Hermitian Adjoint* that a positive dagger puts the slice inside the unit sphere, and the three dimensions of the gap are exactly the vector part the norm does not see. A reader who meets the phrase "unit norm under ${}^{*}$" should read it as one of the four equations, not as the group.

**The unitary conjugation is an isometry of all four forms.** The conjugation by a unitary preserves **all four** forms of *Conventions in the Biquaternion Universe* at once — the bilinear, the quaternionic bilinear, the sesquilinear and the Krein form — and not the sesquilinear form alone. The computation reduces to two facts already in hand. A unitary splits as a central phase times a determinant-one part,
$$
U(2)=U(1)\cdot SU(2),\qquad \tilde{U}=\lambda\tilde{U}_0,\quad |\lambda|=1,\quad N(\tilde{U}_0)=e_0 ,
$$
and the phase is invisible to conjugation, $\Gamma_{\lambda e_0}=\mathrm{id}$, so only the $SU(2)$ part acts; and that part is a **unit real quaternion**, so for it the bar is the identity and the natural sign and the star agree, $\bar{\tilde{U}}_0=\tilde{U}_0$, $\tilde{U}_0^{\natural}=\tilde{U}_0^{*}=\tilde{U}_0^{-1}$. The four forms are $\mathrm{Sc}(\tilde{Z}^{a}\tilde{Y}^{b})$ with $a$ the identity or the natural sign on the first slot and $b$ the identity or the star on the second; with the bar trivial and the natural sign equal to the star, each dressing is carried along by the automorphism $\Gamma_{\tilde{U}_0}$, and each of the four forms is preserved by the multiplicativity of $\Gamma_{\tilde{U}_0}$ together with $\mathrm{Sc}(\tilde{U}_0\tilde{X}\tilde{U}_0^{*})=\mathrm{Sc}(\tilde{X})$.

**Which group preserves which pair.** The four forms are not preserved by the same larger group, and the split follows the first slot. The two forms that carry the natural sign there — the quaternionic bilinear form and the Krein form — scale by the **central factor** $\lvert N(\tilde{U})\rvert^{2}$ under a conjugation,
$$
\langle\Gamma_{\tilde{U}}\tilde{P},\Gamma_{\tilde{U}}\tilde{Q}\rangle_{\natural}=\lvert N(\tilde{U})\rvert^{2}\langle\tilde{P},\tilde{Q}\rangle_{\natural},
\qquad
\langle\Gamma_{\tilde{U}}\tilde{P},\Gamma_{\tilde{U}}\tilde{Q}\rangle_{\natural*}=\lvert N(\tilde{U})\rvert^{2}\langle\tilde{P},\tilde{Q}\rangle_{\natural*} ,
$$
both resting on the identity $\tilde{U}^{*}\bar{\tilde{U}}=\overline{N(\tilde{U})}e_0$, the counterpart of $\tilde{U}\tilde{U}^{\natural}=N(\tilde{U})e_0$. They are therefore preserved **exactly by $G_N$**, the larger group. The two forms without the natural sign — the complex bilinear and the complex sesquilinear — are preserved **exactly by $U(2)$**: for the sesquilinear form the diagonal of a conjugate reads
$$
\mathrm{Sc}\bigl(\tilde{U}\tilde{P}\tilde{U}^{*}(\tilde{U}\tilde{Q}\tilde{U}^{*})^{*}\bigr)=\mathrm{Sc}\bigl(\tilde{P}\tilde{D}\tilde{Q}^{*}\tilde{D}\bigr),\qquad \tilde{D}=\tilde{U}^{*}\tilde{U},
$$
which returns $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$ for all $\tilde{P}$ and $\tilde{Q}$ only when $\tilde{D}=e_0$ — setting $\tilde{Q}=e_0$ already forces $\tilde{D}^{2}=e_0$, and a Hermitian positive $\tilde{D}$ with that square is $e_0$. The common part of the two groups is $U(2)$, so the four forms are preserved together only by the smaller group, and the larger group is not a larger symmetry of them. The boosts of $G_N$ separate the two pairs and are the witness: $\tilde{U}=\cosh t\,e_0+i\sinh t\,e_3$ has $N(\tilde{U})=e_0$, preserves the quaternionic bilinear and the Krein form, and fails the other two with no constant of proportionality at all — the failure is not a scalar multiple but a genuine change of the form.

**A caution on the word isometry.** The isometry group of a form, read in the standard linear sense as the full group of linear maps that preserve it, is far larger than the unitary group, and it is not one group but three: $O_4(\mathbb{C})$ of real dimension twelve for the two bilinear forms, $U(4)$ of real dimension sixteen and compact for the complex sesquilinear form, and $U(1,3)$ of real dimension sixteen and non-compact for the Krein form. What the unitaries supply is not one of those groups but the **inner isometries**, the conjugations by an element of the algebra, and because the central phase acts trivially the acting group is $PU(2)\cong SO(3)$, of real dimension three. The two statements do not compete, and a reader should hold both: every conjugation by a unitary is an isometry of each of the four forms, and the isometry group of each form is very much larger than the image of the unitary group. The sharper form of the first statement is that these inner isometries are exactly the isometries that also preserve the algebra's multiplication — the $\mathbb{C}$-linear isometries preserving the product are the inner ones and no others. That is why the four forms survive a unitary conjugation together: the reason is not an accident of the coefficients, it is that the conjugation is an automorphism of the algebra as well as an isometry of the forms, and the four forms are four dressings of the one product that the automorphism preserves.

**A remark on the direction of the two accounts.** Theorem 1 is a statement about the algebra's own conjugation action: it says which inner maps are automorphisms. Theorem 2 is a statement about the determinant: it says that the biquaternion norm detects $\tilde{U}$ only through the central number $N(\tilde{U})$. The two are related by the fact that the unitaries are precisely the elements with $N(\tilde{U})$ a unit-modulus central scalar **and** $\tilde{U}^{*}\tilde{U}=e_0$, the second condition being the genuinely non-abelian one. In the centre, equality cannot distinguish $U(2)$ from $G_N$; the non-central defect $\tilde{U}^{*}\tilde{U}$ is what does.

## Worked Examples and Counterexamples

The following computations exhibit each hypothesis failing when it is dropped. Every one has been recomputed symbolically and confirmed numerically on superpositions, not on a single basis element.

**Example 1: a non-unitary element of unit norm.** Take $\tilde{U}=\mathrm{diag}(\lambda,\lambda^{-1})$ in the matrix model with $\lambda>0$, $\lambda\neq1$; equivalently $\tilde{U}=\cosh t\,e_0+i\sinh t\,e_3$ in the algebra, with $\lambda=e^{t}$, which the matrix model sends to $\mathrm{diag}(e^{t},e^{-t})$. Its determinant is $1$, so $N(\tilde{U})=e_0$ and Theorem 2's hypothesis holds: the biquaternion norm is preserved. But
$$
\tilde{U}^{*}\tilde{U}=\mathrm{diag}(\lambda^2,\lambda^{-2}),
$$
which is not central for $\lambda\neq1$, so $\Gamma_{\tilde{U}}$ is not multiplicative and does not preserve the Hermitian norm. Concretely, on the pure state $\tilde{P}=\tfrac12(e_0+i e_1)$ the trace pairing of $\tilde{P}$ with itself is $1$ before and $\mathrm{Tr}(\Gamma_{\tilde{U}}\tilde{P})^2=\tfrac14(\lambda^2+\lambda^{-2})^2=\cosh^2 2t$ after, while the biquaternion norm $N$ stays at $0$ on this null element. The example makes the two norms' disagreement explicit: the biquaternion norm sees only the determinant, and the determinant is blind to $\lambda$.

**Example 2: a central scaling.** Take $\tilde{U}=\lambda_0 e_0$ with $\lambda_0>0$, $\lambda_0\neq1$. This defect is central, $\tilde{U}^{*}\tilde{U}=\lambda_0^2e_0$, so $\Gamma_{\tilde{U}}$ is a homomorphism up to the central scalar $\lambda_0^2$: for all $\tilde{Q},\tilde{Y}$,
$$
\Gamma_{\tilde{U}}(\tilde{Q})\Gamma_{\tilde{U}}(\tilde{Y})=\lambda_0^2\,\Gamma_{\tilde{U}}(\tilde{Q}\tilde{Y}),
\qquad
\Gamma_{\tilde{U}}(\tilde{Q})=\lambda_0^2\tilde{Q}.
$$
The biquaternion norm scales as $N(\Gamma_{\tilde{U}}\tilde{Q})=\lambda_0^4N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\bigl|\lambda_0^2\bigr|^2N(\tilde{Q})$, in agreement with Theorem 2 with $|N(\tilde{U})|=|\lambda_0^2|=\lambda_0^2$. The Hermitian norm scales by $\lambda_0^4$ and is not preserved. This example shows that *centrality of the defect is not enough for unitarity*: it removes the operator-valued part of the anomaly and leaves a scalar, and the scalar must be normalized to one. It is the precise counterpart, in the multiplicative direction, of the statement that a central root of $-e_0$ must be normalized to be $\pm i$.

**Example 3: a non-central root of $-e_0$.** Take $J=e_3$, so $J^2=-e_0$, and take the Hermitian generator $\tilde{H}=i e_1$ (i.e. $\mathbf{h}=(1,0,0)$). Then, with the flow generator $G=-\hbar^{-1}J\tilde{H}$,
$$
G=-\hbar^{-1}e_3\,ie_1=-\hbar^{-1}i\,e_3e_1=-\hbar^{-1}i\,e_2 .
$$
Now $ie_2$ is Hermitian, since $(ie_2)^{*}=ie_2$, so $G$ is Hermitian rather than anti-Hermitian, and the one-parameter group it generates is the hyperbolic element
$$
\exp(Gt)=\cosh(\hbar^{-1}t)\,e_0-\sinh(\hbar^{-1}t)\,ie_2 ,
$$
which is not unitary: because $G^2=\hbar^{-2}e_0$, the hyperbolic functions replace the trigonometric ones, and
$$
\exp(Gt)^\dagger\exp(Gt)=\cosh(2\hbar^{-1}t)\,e_0-\sinh(2\hbar^{-1}t)\,ie_2 ,
\qquad
\mathrm{Tr}\bigl(\exp(Gt)^\dagger\exp(Gt)\bigr)=2\cosh(2\hbar^{-1}t),
$$
which grows without bound, so the Hermitian norm of a state is not preserved. Its biquaternion norm, by contrast, is $N(\exp Gt)=\bigl(\cosh^2\hbar^{-1}t-\sinh^2\hbar^{-1}t\bigr)e_0=e_0$, so this non-unitary element has $|N|=1$ and is exactly the kind of element Theorem 2 allows. The failure is exactly the non-commutation of $J=e_3$ with the Hermitian element $ie_1$; it is the non-centrality of the unit that breaks the norm. The computation is the flow version, developed next.

**Example 4: an accidental invariance.** If one tests norm preservation only on a single fixed element, non-unitary elements can appear to preserve it. With $\tilde{Q}=\tilde\Pi(\hat{\mu})$ and $\tilde{U}$ a rotation element of $G_N$ that happens to fix $\hat{\mu}$, the Hermitian norm of that particular $\tilde{Q}$ can be unchanged even though $\Gamma_{\tilde{U}}$ is not unitary. The quantifier "for all $\tilde{Q}$" in Theorem 1 is therefore essential, and the numerical checks of this article were run on random superpositions precisely to avoid this accident.

## Unitarity from Centrality: the Flow

The norm-preservation theorem of the preceding sections is algebraic: it is about the conjugation action on the algebra. Its dynamical counterpart is the statement that the unit of the Schrödinger equation is forced to be central if the norm is to be preserved for every generator.

**The state-vector equation.** In the state module $\mathbb{B}p$, the equation is
$$
i\hbar\,\partial_t\psi=J\tilde{H}\psi ,
\qquad
J^2=-e_0,\quad \tilde{H}\in\mathbb{M}_+,
$$
with $J$ a root of $-e_0$ and $\tilde{H}$ Hermitian. The solution, for constant $\tilde{H}$, is
$$
\psi(t)=\exp\bigl(Gt\bigr)\psi(0),
\qquad
G=-\hbar^{-1}J\tilde{H}.
$$
The norm $\mathrm{Tr}(\psi^\dagger\psi)$ is preserved for all $t$ and all $\psi(0)$ exactly when $G$ is anti-Hermitian,
$$
\frac{d}{dt}\mathrm{Tr}\bigl(\psi^\dagger\psi\bigr)
=\mathrm{Tr}\bigl(\psi^\dagger(G^{*}+G)\psi\bigr)
=0\ \ \text{for all }\psi
\iff G^{*}=-G .
$$

**Theorem 3.** Let $J$ be a root of $-e_0$. The flow generated by $G=-\hbar^{-1}J\tilde{H}$ is norm-preserving for **every** Hermitian $\tilde{H}$ if and only if $J$ is central. In that case $J=\pm i$, and the flow is the standard unitary one.

**Proof.** The hypothesis is that $G^{*}=-G$ for every Hermitian $\tilde{H}$. Since $\tilde{H}^{*}=\tilde{H}$,
$$
G^{*}=-\hbar^{-1}\tilde{H}J^\dagger,
\qquad
-G=+\hbar^{-1}J\tilde{H},
$$
so the hypothesis reads $-\tilde{H}J^\dagger=J\tilde{H}$ for every Hermitian $\tilde{H}$. Evaluating it at $\tilde{H}=e_0$ gives $J^\dagger=-J$, so a root of $-e_0$ that generates a norm-preserving flow is necessarily anti-Hermitian; with that, and only with that, the condition becomes $\tilde{H}J=J\tilde{H}$. This must hold for every Hermitian $\tilde{H}$. The Hermitian elements span $\mathbb{M}_+=\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$, whose real span together with $i$ spans all of $\mathbb{B}$; since $J$ commutes with $e_0$ and with every $ie_k$, it commutes with every element of $\mathbb{B}$, i.e. $J$ is central. The centre is $\mathbb{C}_{\mathbb{B}}=Z(\mathbb{B})=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$, and its elements are $\lambda e_0$ with $\lambda\in\mathbb{C}$; the condition $J^2=-e_0$ gives $\lambda^2=-1$, hence $\lambda=\pm i$. Conversely, for $J=\pm i$ the generator $G=\mp\hbar^{-1}i\tilde{H}$ is anti-Hermitian because $\tilde{H}$ Hermitian implies $i\tilde{H}$ anti-Hermitian, and the exponential $\exp(Gt)$ is unitary.

**Where the centrality is used.** The hypothesis "for every Hermitian $\tilde{H}$" is what forces $J$ into the centre, and it is not a technical convenience. Physically, a dynamics must be norm-preserving for the whole class of Hamiltonians the theory admits, not merely for one particular $\tilde{H}$; the theory admits every Hermitian element as a possible generator. Mathematically, one non-central root is enough to violate the norm, and Example 3 exhibits the violation: with $J=e_3$ and $\tilde{H}=ie_1$, the generator is Hermitian rather than anti-Hermitian, so the exponential is not unitary.

**The structural reading.** Theorem 3 says that the norm-preserving unit of the dynamics is *the* central root of $-e_0$, and the centre's role here is different from its two earlier roles. In the multiplicative theorem the centre was where the defect had to live for the anomaly to be scalar; in the biquaternion-norm theorem the centre was the target space of the biquaternion norm. Here the centre is where the *unit* must live, and it is the only place where a root of $-e_0$ is compatible with invariance under the full symmetry of the state space. The three roles are the same fact seen from three sides: the centre is the maximal commutative subalgebra, and every statement that must hold "uniformly" over a non-commutative family collapses to a statement about the centre.

**A corollary on the field.** The theorem also shows what fixes the scalar field at $\mathbb{C}$: a norm-preserving unit is forced into the centre whenever the Hermitian generators are rich enough to generate the algebra, which is the case here, since $\mathbb{M}_+$ together with $i$ spans $\mathbb{B}$. The hypothesis is not idle. Over the real quaternions the conjugation-Hermitian elements are only the reals, too few to generate the algebra, and a non-central root of $-e_0$ — $e_1$, say — generates a norm-preserving flow for the central generators $a e_0$; the same happens within $\mathbb{B}$ itself whenever the Hamiltonian is restricted to the central directions, since $G=-\hbar^{-1}e_1a=-\hbar^{-1}a\,e_1$ is anti-Hermitian and its exponential is unitary. What a non-central unit cannot do is preserve the norm for **every** Hermitian generator, and that too is visible at once: with $J=e_3$ and $\tilde{H}=ie_1$ the generator is $-ie_2$, Hermitian rather than anti-Hermitian, and the norm grows as in Example 3. Given the full set of generators the unit is central, and a central unit with $J^2=-1$ exists precisely when the centre contains a square root of $-1$. In $\mathbb{B}$ the centre is $\mathbb{C}$, whose two roots are $\pm i$; this is the algebraic content of the standard statement that the complex numbers are sufficient for quantum theory.

## What Is Standard and What Is the Algebra's

The results above divide into a standard linear-algebra part and an algebraic part, and the division should be stated rather than left implicit.

**Standard.** The identification of the Hilbert–Schmidt isometries of a matrix algebra under congruence with the unitary group is standard; the multiplicativity of the determinant and the behaviour of the determinant under the adjoint, $\det(A^\dagger)=\det(A)^{*}$, are standard; the isomorphism of the unit-norm group $SL(2,\mathbb{C})$ with the double cover of the Lorentz group is standard, and so is the fact that the unitary group is the norm-preserving group of quantum physics. The companion articles on the Schrödinger equation and on angular momentum already use these facts, and nothing here re-derives them.

**The algebra's.** Three statements are genuinely about $\mathbb{B}$ and its structure, and they are the content the framework adds.

First, the **coexistence of the two norms on the same eight-real-dimensional algebra** is specific to the biquaternion setting: the Hermitian norm is the Hilbert–Schmidt form of the matrix model, while the biquaternion norm is its determinant, and the two live on the same elements with different target spaces ($\mathbb{R}$ and $\mathbb{C}_{\mathbb{B}}$). A purely complex matrix algebra has the first as its operator norm source and the second as its determinant, but it does not have the second as a *norm on the algebra* in the sense used here, because the determinant of a complex matrix is not a positive form; the biquaternion realization makes the determinant into a Hermitian-valued quadratic form whose scalar part is the Minkowski form.

Second, the **centrality criterion for multiplicativity** is the framework's own statement: an inner map of $\mathbb{B}$ given by conjugation is multiplicative exactly when its defect $\tilde{U}^{*}\tilde{U}$ is the unit, and multiplicative up to a scalar exactly when that defect is central. This is the precise algebraic form of the familiar fact that a non-unitary conjugation is not an automorphism, and it is what makes the word *centrality* the right one for the phenomenon: the obstruction to multiplicativity is measured by an element of the algebra, and it is scalar exactly when that element lies in the centre.

Third, the **forced centrality of the unit in the dynamics** is algebraic in a way that its complex counterpart is not. In the complex theory one simply postulates $i$ and checks that $i\tilde{H}$ is anti-Hermitian; because there is only one imaginary unit available, the question of centrality does not arise. In $\mathbb{B}$ the anti-Hermitian roots of $-e_0$ — the roots that can serve as the unit of a norm-preserving dynamics — are the two central ones $\pm i$ together with the infinitely many unit pure real quaternions, and the requirement of norm preservation for all generators selects the centre. The selection is a theorem in this framework, and it is what connects the norm-preservation theorem to the identification of the centre as the classical sector.

**A limit.** Theorems 1 and 3 are, at bottom, standard facts about the unitary group, dressed in the algebra's coordinates. Their value is not that they produce a new group but that they locate the framework's unitarity precisely: it is the unitarity of the matrix model, its group is $U(2)$ acting by conjugation, and the extra group $G_N=U(1)\cdot SL(2,\mathbb{C})$ that preserves the biquaternion norm is the group of elements whose determinant has modulus one — which is not a group of quantum symmetries but a statement about the determinant. A reader should not read the larger group as a larger class of allowed quantum evolutions; the companion article *What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions* is concerned to prevent exactly that reading.

## Summary

The biquaternion algebra carries two quadratic forms, and unambiguity about which one is being preserved is the whole content of the norm-preservation theorem. The Hermitian norm $\mathrm{Tr}(\tilde{Q}^{*}\tilde{Q})$ is real, positive definite, and preserved by the conjugation action $\Gamma_{\tilde{U}}(\tilde{Q})=\tilde{U}\tilde{Q}\tilde{U}^{*}$ exactly when $\tilde{U}$ is unitary; that is Theorem 1, and it is the framework's statement of unitarity. The biquaternion norm $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}$ is central-valued and indefinite, and under the same action it scales by a **central** scalar,

$$
N\bigl(\Gamma_{\tilde{U}}\tilde{Q}\bigr)=\bigl|N(\tilde{U})\bigr|^2N(\tilde{Q}),
$$

so it is preserved exactly when $|N(\tilde{U})|=1$; that is Theorem 2, and its group is the seven-real-dimensional $G_N=U(1)\cdot SL(2,\mathbb{C})$, which contains $U(2)$; the intersection is $U(2)$ itself, while $U(2)\cap SL(2,\mathbb{C})=SU(2)$.

The centrality theme is carried by the defect $\tilde{Z}=\tilde{U}^{*}\tilde{U}$. The action is multiplicative exactly when $\tilde{Z}=e_0$, i.e. exactly when $\tilde{U}$ is unitary and $\Gamma_{\tilde{U}}$ is an automorphism; when $\tilde{Z}$ is central the multiplicative anomaly collapses to the scalar $\tilde{Z}$, and the centre is precisely the locus where that collapse occurs. The same collapse governs the dynamics: the generator $G=-\hbar^{-1}J\tilde{H}$ is anti-Hermitian for every Hermitian $\tilde{H}$ if and only if the root $J$ of $-e_0$ is central, and the only central roots are $\pm i$, so the unit of the Schrödinger equation is forced into the centre of the algebra. Unitarity, in this framework, is a centrality statement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| ${}^{*}={}^{\natural}\circ\bar{\cdot}$ | Hermitian conjugation |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $\mathbb{C}_{\mathbb{B}}=Z(\mathbb{B})=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$ | Centre of $\mathbb{B}$; the series symbol is $\mathbb{C}_{\mathbb{B}}$ |
| $\mathrm{Tr}(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})$ | Trace, $\mathrm{Tr}(e_0)=2$ |
| $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm, centre-valued |
| $\langle\tilde{Q},\tilde{Y}\rangle_{}^{*}=\mathrm{Tr}(\tilde{Q}^{*}\tilde{Y})$ | Hermitian (Hilbert–Schmidt) pairing |
| $\Gamma_{\tilde{U}}(\tilde{Q})=\tilde{U}\tilde{Q}\tilde{U}^{*}$ | Conjugation action |
| $\tilde{Z}=\tilde{U}^{*}\tilde{U}$ | Defect of the action |
| $U(2)=\{\tilde{U}:\tilde{U}^{*}\tilde{U}=e_0\}$ | Unitary group; preserves the Hermitian norm |
| $SL(2,\mathbb{C})=\{\tilde{U}:N(\tilde{U})=e_0\}$ | Unit-norm group |
| $G_N=\{\tilde{U}:|N(\tilde{U})|=1\}=U(1)\cdot SL(2,\mathbb{C})$ | Exact biquaternion-norm-preserving group |
| $J$ | Root of $-e_0$, $J^2=-e_0$ |
| $G=-\hbar^{-1}J\tilde{H}$ | Generator of the state-vector flow |
| $M(\tilde{Q})$ | $2\times2$ matrix model, $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, $\mathbb{C}$-linear |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the complex sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the complex bilinear form, the scalar part of the complex bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- S. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford University Press, 1995), for the quaternionic formulation of quantum physics, its unitarity conditions, and the role of the norm.
- D. Finkelstein, J. M. Jauch, S. Schiminovich, and D. Speiser, "Foundations of quaternion quantum mechanics", *Journal of Mathematical Physics* **3**, 207 (1962), for the original algebraic treatment of quaternionic quantum theory and its scalar field.
- G. Birkhoff and J. von Neumann, "The logic of quantum mechanics", *Annals of Mathematics* **37**, 823 (1936), for the argument that the complex field is the appropriate scalar field and the role of a central imaginary unit.
- A. Sudbery, "Quaternionic analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85**, 199 (1979), for the analysis of quaternionic and biquaternionic linear algebra, determinants, and the unimodular group.
- E. Artin, *Geometric Algebra* (Interscience, 1957), for the biquaternion norm, its multiplicativity, and the identification of the unit-norm group with the double cover of the Lorentz group.
- K. Hoffman and R. Kunze, *Linear Algebra* (Prentice-Hall, 2nd ed., 1971), for the multiplicativity of the determinant and the determinant of the adjoint.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 2000), for unitary evolution, norm preservation, and the Hilbert–Schmidt inner product.
- A. W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2nd ed., 2002), for the structure of $U(2)$, $SU(2)$, and $SL(2,\mathbb{C})$ and their real dimensions.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed., 2001), for the matrix representation of the quaternion and biquaternion algebras and the identification $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$.
