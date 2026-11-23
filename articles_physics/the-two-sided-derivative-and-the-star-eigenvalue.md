# __The Two-Sided Derivative and the Star Eigenvalue__

## Introduction

A frame field that carries a curved metric needs a derivative before anything can be computed with it, and the derivative the framework uses is two-sided:

$$
D_{\imath}\tilde Q=\partial_{\imath}\tilde Q+\vec\Gamma_{\imath}\tilde Q+\tilde Q\vec\Gamma_{\imath}^{*}.
$$

Two products instead of one. This article explains why there are two, and what the two-sided form buys that a one-sided or commutator form does not. It is the article a reader needs before any calculation with a curved connection, and it exists because that explanation is scattered across the gravitational articles of the series and is nowhere stated once.

The reason is not a convention. $SU(2)$ acts on the material sector by **conjugation**,

$$
\tilde Q\longmapsto\tilde U\tilde Q\tilde U^{*},
$$

so a derivative that is to be covariant under that action must compensate on both sides. That much is forced by the action and is not in dispute. What is worth isolating is the finer structure: the two-side prescription splits, by a single eigenvalue, into a commutator part and an anticommutator part, and the split is the reason the naive one-sided forms fail in different ways.

**The claim of the article.** The scalar-free subspace that houses a Lorentz connection carries an involution, the star, and star acts on it with two eigenvalues. On the three-dimensional eigenspace with eigenvalue $-1$ — the rotation generators — the two-sided derivative is the **commutator** with the connection; on the three-dimensional eigenspace with eigenvalue $+1$ — the boost generators — it is the **anticommutator**. So a commutator prescription is not wrong by a factor: it is the exact derivative of a different action, the adjoint action, which agrees with conjugation on the rotation subgroup and only there. That is the precise sense in which the commutator form "drops the boosts".

Two boundary remarks belong in the introduction, because they are what keeps the article honest. The two-sided derivative is corpus content and it is not a flaw; the recurring external summary that calls it an unnecessary complication is a misreading, and the calculation here is what answers it. And the derivative, once written, is still only a derivative: it does not produce a connection, and it does not produce curvature. Choosing one is a further condition, stated at the end.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^{2}=-e_t$, $\vec e_x\vec e_y=\vec e_z$. The subspaces $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ are the anti-Hermitian and Hermitian parts under the star $^{*}$, which conjugates the coefficients and negates the three vectors, so that $(i\tilde Q)^{*}=-i\tilde Q^{*}$ and $^{*}$ is conjugate-linear. Quaternionic conjugation ${}^{\natural}$ keeps the scalar and negates the vectors and is complex-linear, so $\tilde Q^{*}=\overline{\tilde Q}^{\natural}$; the two agree on $\mathbb{B}_{H}$. The norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$, the bilinear form on the material sector is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})$, and $SU(2)$ is $\{\tilde U:\tilde U\tilde U^{\natural}=e_t\}$, so that $\tilde U^{-1}=\tilde U^{\natural}$.

## The Lie Algebra of the Frame

The frame's local freedom is a copy of $SL(2,\mathbb{C})$ at each point, and its Lie algebra is a subspace of $\mathbb{B}$, not an abstract Lie algebra attached from outside. The subspace is

$$
\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}=\{\vec G:\mathrm{Sc}(\vec G)=0\},
$$

the six-real-dimensional scalar-free subspace, with basis

$$
\vec e_x,\ \vec e_y,\ \vec e_z,\qquad i\vec e_x,\ i\vec e_y,\ i\vec e_z .
$$

The first three are the **rotation generators** and the last three the **boost generators**, and the names are exact rather than decorative: the first three are anti-Hermitian and close among themselves on $\mathfrak{su}(2)$, the last three are Hermitian and do not close among themselves, and a single generator of the mixed form produces a null rotation.

Two facts about this subspace are used repeatedly below and are worth recording as computations rather than as slogans. It is closed under multiplication modulo the scalar: the product of two scalar-free elements is scalar-free. And every element of it is invertible unless its norm vanishes, because $\vec G\vec G^{\natural}=\langle \vec G\rangle_{\natural}e_t$ is a scalar, so $\vec G^{-1}=\vec G^{\natural}/\langle\vec G\rangle_{\natural}$.

**The counting.** Six real dimensions of generator, four coordinate directions in a frame's index, twenty-four real connection components, which is twelve complex: the spin coefficients of the Newman–Penrose article. The arithmetic is the same arithmetic, and it is the reason the connection can be called $\mathbb{B}$-valued without qualification.

## The Action, and the Derivative That Matches It

Rotor conjugation is the action of the frame's freedom on the material sector, and its infinitesimal form is what a covariant derivative has to compensate. Write $\tilde U=e_t+\epsilon\vec G$ to first order in a small parameter, with $\vec G$ scalar-free. Then $\tilde U^{*}=e_t+\epsilon\vec G^{*}$, and since $\epsilon$ is real, $\tilde U^{-1}=\tilde U^{\natural}=e_t+\epsilon\vec G^{\natural}$. Rotor conjugation gives

$$
(e_t+\epsilon\vec G)\tilde Q(e_t+\epsilon\vec G^{*})=\tilde Q+\epsilon\left(\vec G\tilde Q+\tilde Q\vec G^{*}\right),
$$

so the infinitesimal generator acting on $\tilde Q$ is

$$
\tilde Q\longmapsto \vec G\tilde Q+\tilde Q\vec G^{*}.
$$

**The derivative's shape is now forced.** A connection with values $\vec\Gamma_{\imath}$ in the same subspace must subtract this generator, and it must subtract it **on both sides**, because the generator has two products. A prescription that compensates only on the left cannot be covariant: the right product $\tilde Q\vec\Gamma^{*}$ is not a left multiplication by any algebra element, so no choice of a left connection removes it. This is the entire content of the "two-sided" in the derivative's name, and it is a consequence of the action rather than a design choice.

**The test case that separates the candidates.** Take $\vec G=i\vec e_x$, a boost, and $\tilde Q=i q'_t e_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ a general material element. Then

$$
\vec G\tilde Q+\tilde Q\vec G^{*}=(-2q_x)\,i e_t+(-2q'_t)\,\vec e_x ,
$$

that is, $\delta q'_t=-2q_x$ and $\delta q_x=-2q'_t$: the infinitesimal boost in its standard form, with both coordinates moving. The number two is not decoration; it is the factor by which a bivector acts twice on a vector, once through each of its two vector legs. A one-sided prescription produces one of the two lines and not the other, and the component it misses is the one that makes the transformation a boost rather than a shear.

## The Star Eigenvalue Splits the Connection

The six generators split into two triples, and the split is an eigenvalue statement about the star. Applying $^{*}$ to the basis,

$$
\vec e_k^{*}=-\vec e_k,\qquad (i\vec e_k)^{*}=+i\vec e_k ,
$$

because $^{*}$ conjugates the coefficient — which reverses the sign of $i$ — and negates the vector, and the two signs cancel on $i\vec e_k$. So the scalar-free subspace is the direct sum of two three-dimensional eigenspaces,

$$
\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}=\underbrace{\mathrm{span}\{\vec e_x,\vec e_y,\vec e_z\}}_{\sigma=-1}\ \oplus\ \underbrace{\mathrm{span}\{i\vec e_x,i\vec e_y,i\vec e_z\}}_{\sigma=+1},
$$

and every connection value decomposes accordingly:

$$
\vec\Gamma_{\imath}=\vec\omega_{\imath}+\vec\beta_{\imath},\qquad \vec\omega_{\imath}^{*}=-\vec\omega_{\imath},\qquad \vec\beta_{\imath}^{*}=+\vec\beta_{\imath}.
$$

The names are the physical ones: $\vec\omega_{\imath}$ is the **rotation part** of the connection and $\vec\beta_{\imath}$ the **boost part**. The eigenvalues are real and the decomposition is canonical — it is not a choice of basis, since an eigenspace decomposition of a linear map is invariant — so the split of a connection into its rotation and boost halves is well defined for every connection and no convention enters.

**The identity.** Let $\vec G$ be scalar-free with $\vec G^{*}=\sigma\vec G$, $\sigma=\pm1$. Then

$$
\vec G\tilde Q+\tilde Q\vec G^{*}=\vec G\tilde Q+\sigma\,\tilde Q\vec G=
\begin{cases}
[\vec G,\tilde Q], & \sigma=-1,\\[2pt]
\{\vec G,\tilde Q\}, & \sigma=+1 .
\end{cases}
$$

This is the whole of the article's technical content, and it is one line: the two-sided prescription is a commutator on one eigenspace and an anticommutator on the other. Applying the identity component by component gives the decomposition of the derivative itself,

$$
\boxed{\;D_{\imath}\tilde Q=\partial_{\imath}\tilde Q+[\vec\omega_{\imath},\tilde Q]+\{\vec\beta_{\imath},\tilde Q\}\;},
$$

which was checked on a hundred random connections and material elements with no residual. The two-sided derivative is a **commutator plus an anticommutator**, and the two terms are the two halves of the local Lorentz group.

**Why the anticommutator is not optional, stated as an identity rather than a warning.** A commutator-only derivative preserves the scalar part of $\tilde Q$ identically, since $\mathrm{Sc}([\vec G,\tilde Q])=0$ for every $\vec G$. But a boost does not preserve the scalar part: the test case above sends $i q'_t$ into $-2q_x i e_t$, changing the time coefficient. So a commutator-only derivative cannot generate a boost on the material sector, and its covariance group is the rotation subgroup $\mathfrak{su}(2)$ rather than the Lorentz algebra. The anticommutator is exactly the part that moves the scalar part, and the boost half of the connection is exactly what supplies it.

## The Rotor-Level Twin

The same split appears at the level of finite transformations, and in a form that is easier to remember than the infinitesimal one.

**A rotation rotor is unitary in the algebra's sense.** For $\tilde U=\cos(\phi/2)e_t+\sin(\phi/2)\vec u$ with $\vec u$ a unit spatial vector, $\tilde U^{*}=\cos(\phi/2)e_t-\sin(\phi/2)\vec u=\tilde U^{-1}$, and $\tilde U\tilde U^{\natural}=e_t$ because $\vec u^{2}=-e_t$. So $\tilde U^{*}=\tilde U^{-1}$.

**A boost rotor is Hermitian.** For $\tilde U=\cosh(\theta/2)e_t+i\sinh(\theta/2)\vec u$, the star leaves the coefficient of $i\vec u$ alone, so $\tilde U^{*}=\tilde U$, and $\tilde U\tilde U^{\natural}=\cosh^{2}(\theta/2)-\sinh^{2}(\theta/2)\cdot(i\vec u)^{2}=e_t$ because $(i\vec u)^{2}=+\vec u^{2}\cdot i^{2}=+e_t$. So $\tilde U^{*}=\tilde U\neq\tilde U^{-1}$.

Both were checked on explicit rotors, and the two statements are the rotor-level twin of the eigenvalue split: the compact half of the group satisfies $\tilde U^{*}=\tilde U^{-1}$, the noncompact half satisfies $\tilde U^{*}=\tilde U$, and no element of the group satisfies both unless it is $\pm e_t$. The boost rotor's Hermiticity is the finite form of "the boost generators are Hermitian", and it is the reason a boost is a Hermitian operation while a rotation is a unitary one.

**What that means for an action written with $\tilde U^{-1}$.** Since $\tilde U^{*}=\tilde U^{-1}$ only on the compact half, an action written as $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{-1}$ agrees with rotor conjugation on rotations and disagrees on boosts. That action is the adjoint action, its derivative is the commutator, and its covariance group is the complexification of $\mathfrak{su}(2)$ read as a Lie algebra rather than the Lorentz algebra acting on the vector. The finite statement and the infinitesimal one are the same statement.

## Why the Commutator Prescription Fails, and What It Would Be Right For

The commutator prescription is a real prescription: it is the covariant derivative of the adjoint action. It is correct, and it is the right derivative, for a field that transforms in the adjoint representation — for a bivector, for a connection, for anything whose transformation law is $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{-1}$. The frame field does not transform that way. It transforms by conjugation, $\tilde E_{\Phi,\imath}\mapsto\tilde U\tilde E_{\Phi,\imath}\tilde U^{*}$, and the two agree only when $\tilde U^{*}=\tilde U^{-1}$, that is, only on the rotation subgroup.

So the failure is not an algebraic slip that a factor could repair. It is a representation-theoretic mismatch: the commutator derivative is the derivative for the adjoint representation and the frame is in the vector representation. Written as a table,

| Field | Transformation | Correct derivative |
|---|---|---|
| frame $\tilde E_{\Phi,\imath}$, four-vector | $\tilde U\tilde E\tilde U^{*}$ | $\partial_{\imath}\tilde E+\vec\Gamma_{\imath}\tilde E+\tilde E\vec\Gamma_{\imath}^{*}$ |
| bivector, connection | $\tilde U\tilde Q\tilde U^{-1}$ | $\partial_{\imath}\tilde Q+[\vec\Gamma_{\imath},\tilde Q]$ |
| rotation-only field | $\tilde U\tilde Q\tilde U^{-1}$, $\tilde U$ compact | $\partial_{\imath}\tilde Q+[\vec\omega_{\imath},\tilde Q]$ |

The third line is a special case of the second and is not available for a boost. This is the table that the recurring external summary should have had.

**A second, independent check that a one-sided derivative cannot work.** Count the connection components needed to make each prescription covariant on the material sector. Under a position-dependent rotor the derivative must transform as $\tilde U(D_{\imath}\tilde Q)\tilde U^{*}$, which requires six real compensatory parameters per direction. The left connection $\vec\Gamma_{\imath}$ supplies six; the right connection $\vec\Gamma_{\imath}^{*}$ supplies the same six again, since $\vec\Gamma\mapsto\vec\Gamma^{*}$ is a linear isomorphism of the six-dimensional subspace onto itself. So the two-sided form has exactly the twelve real parameters per direction that a covariant derivative on the vector representation needs, and the one-sided form has six. The count is not a coincidence and it is not an argument by analogy: it is the dimension of the representation.

## The Logarithmic Derivative Is Scalar-Free

A frame built from a rotor field, $\tilde E_{\Phi,\imath}=\tilde U\vec e_{\imath}\tilde U^{*}$ with $\vec e_0=ie_t$, needs a connection that makes it constant. The candidate is the rotor's logarithmic derivative, and it has the property that makes the construction work.

**Claim.** If $\tilde U$ is a unit-norm biquaternion field, then $\tilde U^{\natural}\partial_{\imath}\tilde U$ is scalar-free.

**Proof.** Differentiate $\tilde U^{\natural}\tilde U=e_t$: $(\partial_{\imath}\tilde U^{\natural})\tilde U+\tilde U^{\natural}\partial_{\imath}\tilde U=0$. Let $\vec A=\tilde U^{\natural}\partial_{\imath}\tilde U$. Then $\vec A^{\natural}=(\partial_{\imath}\tilde U^{\natural})\tilde U=-\vec A$, and $\mathrm{Sc}$ is invariant under ${}^{\natural}$, so $\mathrm{Sc}(\vec A)=\mathrm{Sc}(\vec A^{\natural})=-\mathrm{Sc}(\vec A)$, hence $\mathrm{Sc}(\vec A)=0$.

The same argument gives $\partial_{\imath}\tilde U\,\tilde U^{\natural}$ scalar-free, and the two are related by conjugation. So both natural one-sided logarithmic derivatives live in the six-dimensional Lie subspace, which is exactly what a connection needs, and the derivative's value is $\mathbb{B}$-valued with no scalar leakage.

This was checked numerically along an explicit one-parameter rotation rotor with a finite-difference derivative: the scalar part of $\tilde U^{\natural}\partial_{\imath}\tilde U$ came out at the $10^{-11}$ level, which is the finite-difference noise floor, while the vector part was $\tfrac12\vec e_x$ as expected for a rotor of angle $t$ about $x$.

**What the logarithmic derivative is not.** It is not a connection for an arbitrary frame, only for a frame that is pure rotor gauge of the rigid frame. For a general frame the logarithmic derivative of the frame does not exist as a single biquaternion, because the frame is four elements rather than one, and the connection must be supplied by a separate field. This is the precise content of the statement, repeated in the companion articles, that **the algebra supplies the home of the connection and not the connection**.

## Conditions, Consequences, and Where the Framework Stops

The derivative's shape is not a choice, but everything else about a connection is. Four statements belong in sequence, because they are frequently merged.

**The shape is a consequence.** Two-sidedness follows from the conjugacy of the action. Nothing is assumed, and no alternative is available for a four-vector.

**The values are not determined.** $\vec\Gamma_{\imath}$ is an independent field with six real components per direction. The algebra supplies the six-dimensional space it lives in and does not choose a point of it: there is no algebraic condition that a connection must satisfy.

**Metric compatibility is a condition on the values.** Requiring $D_{\imath} g_{\jmath\rho}=0$ for the Gram metric forces the connection coefficients to be antisymmetric in the frame's own index pair, which is what reduces the sixty-four components of a general linear connection to the twenty-four of a Lorentz connection. It is imposed rather than derived: the algebra does not prefer an antisymmetric pair to any other, it supplies the six-dimensional space in which the antisymmetry lives.

**Torsion-freedom is a second, separate condition.** A connection can be metric-compatible and carry torsion, and the framework has no preference between those cases, because it has no action that would break the tie. Torsion is a frame-index object with twenty-four components, so imposing its vanishing fixes the remaining twenty-four parameters and leaves the unique Levi-Civita connection; the framework inherits that solution and not the reason for it.

**The curvature is the ordinary one.** With the connection valued in $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}$, the curvature is a $\mathbb{B}$-valued two-form with the usual expression $\vec F_{\imath\jmath}=\partial_{\imath}\vec\Gamma_{\jmath}-\partial_{\jmath}\vec\Gamma_{\imath}+[\vec\Gamma_{\imath},\vec\Gamma_{\jmath}]$, and its action on a material element is by the two-sided prescription with $\vec F_{\imath\jmath}$ in place of $\vec\Gamma_{\imath}$. The commutator appears here for the connection and the two-sided form appears for the field, and there is no inconsistency: the connection transforms in the adjoint representation and the frame in the vector representation, which is the table above read at the level of curvature.

**Where the framework stops.** The path-ordered exponential is the single operation in the chain connection–curvature–holonomy that $\mathbb{B}$ does not generate. A holonomy is an element of $SL(2,\mathbb{C})$ obtained by integrating a connection along a curve, and the integral is not an algebra operation. Everything up to the curvature is pointwise and therefore native; the holonomy is not, and the programme's accounting says so.

## The One-Sided Alternative, Stated Fairly

The alternative proposal that a commutative connection suffices has a defensible core and an indefensible extension, and separating them is what makes this article useful to a reader who has met the proposal elsewhere.

**The defensible core.** On the rotation subgroup the two-sided derivative and the commutator derivative coincide, because $\vec U^{*}=\vec U^{-1}$ for compact $\vec U$. So for a field whose covariance is restricted to rotations — a spatial triad carried along by a rotation-only frame — the commutator form is exactly right, and nothing is lost. A reader who meets the commutator prescription in a context where only rotations act has met a correct formula.

**The indefensible extension.** A boost is a Lorentz transformation and the frame's covariance group contains it. If the derivative is required to be covariant under the full local Lorentz group, the commutator form fails on the boost half, and the failure is visible in one component: the time coefficient of a material element does not transform. There is no repair by choosing a different connection, because the missing term is not a connection term — it is the difference between two actions.

**Why the proposal keeps recurring.** The commutator form is shorter to write, it is the standard expression in the gauge-theory literature for a field in the adjoint representation, and it agrees with the two-sided form on every example in which only rotations are varied. A summary written from the compact case generalises it, and the generalisation is wrong by exactly the boost half. That is the diagnosis, and it is a diagnosis of a generalisation and not of an arithmetic slip.

## Summary

The two-sided derivative is forced by the conjugacy of the rotor action: the infinitesimal generator is $\vec G\tilde Q+\tilde Q\vec G^{*}$, so a connection must compensate on both sides, and no left connection can absorb the right product.

Star acts on the six-dimensional scalar-free subspace with eigenvalues $-1$ on the rotation generators $\vec e_k$ and $+1$ on the boost generators $i\vec e_k$. Consequently the two-sided derivative is a commutator on the rotation half and an anticommutator on the boost half, $D_{\imath}\tilde Q=\partial_{\imath}\tilde Q+[\vec\omega_{\imath},\tilde Q]+\{\vec\beta_{\imath},\tilde Q\}$, and this was checked on a hundred random cases with no residual.

The rotor-level twin states the same thing: a rotation rotor satisfies $\tilde U^{*}=\tilde U^{-1}$ and a boost rotor satisfies $\tilde U^{*}=\tilde U$. The commutator prescription is therefore the derivative of the adjoint action, correct for bivectors and for connections, and correct for the frame only on the compact subgroup, where the two actions coincide.

What the derivative does not supply is the connection. Metric compatibility and torsion freedom are conditions imposed on independent values, and the curvature is the ordinary Lie-algebra curvature. The holonomy is where the chain leaves the algebra, because the path-ordered exponential is an integral and the framework is pointwise.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $^{*}$ | star: conjugates the coefficients and negates the three vectors; conjugate-linear; $\tilde Q^{*}=\overline{\tilde Q}^{\natural}$ |
| ${}^{\natural}$ | quaternionic conjugation: keeps the scalar, negates the vectors; complex-linear |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | anti-Hermitian and Hermitian subspaces under $^{*}$; material and informational sectors |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | the biquaternion norm |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})$ | the bilinear form on $\mathbb{B}_{\Phi}$ |
| $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}=\{\vec G:\mathrm{Sc}(\vec G)=0\}$ | the six-real-dimensional Lie subspace of $SU(2)$ |
| $\vec e_x,\vec e_y,\vec e_z$ | rotation generators; $^{*}$-eigenvalue $\sigma=-1$ |
| $i\vec e_x,i\vec e_y,i\vec e_z$ | boost generators; $^{*}$-eigenvalue $\sigma=+1$ |
| $\vec\Gamma_{\imath}=\vec\omega_{\imath}+\vec\beta_{\imath}$ | connection; rotation part plus boost part |
| $D_{\imath}\tilde Q=\partial_{\imath}\tilde Q+\vec\Gamma_{\imath}\tilde Q+\tilde Q\vec\Gamma_{\imath}^{*}$ | the two-sided covariant derivative |
| $[\vec G,\tilde Q]=\vec G\tilde Q-\tilde Q\vec G$ | commutator; the $\sigma=-1$ form |
| $\{\vec G,\tilde Q\}=\vec G\tilde Q+\tilde Q\vec G$ | anticommutator; the $\sigma=+1$ form |
| $\sigma$ | star eigenvalue of a generator; $-1$ rotation, $+1$ boost |
| $\vec F_{\imath\jmath}=\partial_{\imath}\vec\Gamma_{\jmath}-\partial_{\jmath}\vec\Gamma_{\imath}+[\vec\Gamma_{\imath},\vec\Gamma_{\jmath}]$ | curvature two-form |
| $\tilde U^{\natural}\partial_{\imath}\tilde U$ | logarithmic derivative of a rotor field; scalar-free |

## Further Reading

- [The Gram Matrix as the Only Metric](the-gram-matrix-as-the-only-metric.html), for the frame whose covariance forces the two-sided form.
- [The Curved Dirac Operator and Its Square](the-curved-dirac-operator-and-its-square.html), the only place in the series where the two-sided derivative enters a calculation with an answer.
- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for the frame route and the programme's accounting of connections, curvature and holonomy.
- [The Newman–Penrose Formalism in Biquaternionic Form](the-newman-penrose-formalism-in-biquaternionic-form.html), for the twelve complex spin coefficients that are the components of this connection in a null basis.
- [Expressing Lie Algebras via Biquaternions](../articles_internal/expressing-lie-algebras-via-biquaternions.html), for the identification of the scalar-free subspace with the Lorentz algebra.
- [Conceptual Conventions](../articles_internal/conceptual-conventions.html), for the rule that an unpreferred concept stays unprivileged and for the status of a connection the algebra hosts but does not choose.
- Robert M. Wald, *General Relativity* (Chicago, 1984), for the tetrad connection, metric compatibility, torsion, and the curvature two-form.
