# __The Modular Theory of Tomita–Takesaki under the Biquaternion Framework__

## Introduction

The **Tomita–Takesaki theory** attaches to a state on a von Neumann algebra a canonical one-parameter group of automorphisms. Let $M$ be a von Neumann algebra acting on a Hilbert space $\mathcal{H}$, and let $\Omega\in\mathcal{H}$ be **cyclic** and **separating** for $M$. On the dense domain $M\Omega$ define the anti-linear map
$$
S_0(A\Omega) := A^*\Omega .
$$
It is closable, and its closure $S$ has the polar decomposition
$$
S = J\,\Delta^{1/2},
$$
with $\Delta=S^*S\geq 0$ self-adjoint and $J$ anti-unitary. The theory then delivers the structural facts
$$
J M J = M', \qquad \Delta^{it}M\Delta^{-it}=M, \qquad \sigma_t(A):=\Delta^{it}A\Delta^{-it},
$$
so that $J$ identifies $M$ with its commutant and $t\mapsto\sigma_t$ is a one-parameter group of automorphisms of $M$, the **modular automorphism group** of the pair $(M,\Omega)$.

This article is the companion of *The KMS Condition and the Biquaternion Framework*. That article stated the KMS condition and located the modular Hamiltonian $K=-\log\rho$ in the informational sector $\mathbb{M}_+$. It used, but did not construct, the operator $S$ whose polar decomposition produces the modular flow. The present article constructs $S$ explicitly in the finite-dimensional biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$, takes its polar decomposition in closed form, and verifies the resulting identities by recomputation. The KMS condition is the parent's subject and is not restated here; the one thing imported from it is the result that the modular flow is the flow for which the thermal state satisfies the KMS boundary relation.

Three features of the construction are easy to get wrong, and they organize what follows.

- **$S$ and $J$ are anti-linear.** $S$ satisfies $S(z\xi)=\bar z\,S(\xi)$, so $J$ is anti-unitary and
$$
J\,i\,J = -i .
$$
The modular conjugation **conjugates the scalar imaginary** $i$. Every sign in the flow depends on this.
- **Cyclic and separating is a genuine hypothesis.** Cyclicity makes $S$ densely defined; separation makes it well defined. Neither implies the other, and the construction collapses without both.
- **The character of the modular flow is fixed by the type of the algebra.** For a semifinite factor it is inner for every $t$; for a type III$_1$ factor it is outer for every $t\neq0$. The direction of this statement is frequently reversed in casual retellings, and the reversal matters.

The article proceeds as follows. The construction and its structural identities come first. Then the two hypotheses, with an explicit failure when separation is dropped. Then the modular flow and its identification with the KMS flow of the parent article. Then the finite-dimensional realization in $\mathbb{B}$ and the closed-form polar decomposition. Then the biquaternion candidate for $S$ and what the framework does and does not supply. Then the type of $\mathbb{B}$ and the inner/outer classification. It closes with the boundary between what is established and what is a gap.

**Conventions.** Those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$, scalar imaginary $i$ with $i^2=-1$, and the isomorphism $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, so that $\mathbb{B}\cong M_2(\mathbb{C})$. The Hermitian (informational) subspace is $\mathbb{M}_+$ and the anti-Hermitian (material) subspace is $\mathbb{M}_-$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$. Hermitian conjugation is $\dagger$, and it is the algebra involution $A\mapsto A^*$ of the Tomita construction. The trace is normalized by the matrix representation, $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, so that $\mathrm{Tr}(e_0)=2$.

## The Tomita–Takesaki Construction

### Cyclic and Separating Vectors

Let $M$ be a von Neumann algebra on a Hilbert space $\mathcal{H}$, and let $\Omega\in\mathcal{H}$. The vector is

- **cyclic** for $M$ if the set $M\Omega=\{A\Omega:A\in M\}$ is dense in $\mathcal{H}$;
- **separating** for $M$ if $A\Omega=0$ with $A\in M$ forces $A=0$.

Both are properties of the pair $(M,\Omega)$, not of $M$ alone: an algebra can have cyclic vectors that are not separating, and separating vectors that are not cyclic.

### The Tomita Operator and Its Polar Decomposition

On the dense domain $M\Omega$ define
$$
S_0(A\Omega) := A^*\Omega .
$$
This is well defined precisely when $\Omega$ is separating: if $A\Omega=0$ then $A=0$, hence $A^*\Omega=0$, so the image does not depend on the representative $A$. The map is **anti-linear**,
$$
S_0\big((zA)\Omega\big)= (zA)^*\Omega = \bar z\,A^*\Omega = \bar z\,S_0(A\Omega),
$$
and it is closable. Its closure is the **Tomita operator**
$$
S := \overline{S_0},
$$
and its polar decomposition is written
$$
S = J\,\Delta^{1/2}, \qquad \Delta := S^*S \geq 0 .
$$
Here $\Delta$ is the **modular operator** and $J$ the **modular conjugation**. The structural identities are
$$
S^2 = 1, \qquad J^2 = 1, \qquad J\Delta J = \Delta^{-1}, \qquad \Delta^{it}M\Delta^{-it}=M \quad (t\in\mathbb{R}).
$$
The last of these is Tomita's theorem. Define
$$
\sigma_t(A) := \Delta^{it}A\Delta^{-it}, \qquad t\in\mathbb{R}.
$$
Then $\sigma_t$ is an automorphism of $M$, and
$$
\sigma_0=\mathrm{id}, \qquad \sigma_t\circ\sigma_s=\sigma_{t+s},
$$
so $t\mapsto\sigma_t$ is a one-parameter group: the **modular automorphism group** of $(M,\Omega)$. The remaining structural identity,
$$
J M J = M',
$$
says that the modular conjugation identifies the algebra with its commutant. The content of the theory is that $S$ — hence $\Delta$ and $J$ — is constructed from the pair $(M,\Omega)$, and that from the state it recovers both a canonical flow and a canonical anti-isomorphism $M\cong M'$.

### Anti-Linearity and the Conjugation of the Scalar Imaginary

The defining anti-linearity of $S_0$ is inherited by $S$ and, through $S=J\Delta^{1/2}$, by $J$, which is anti-unitary:
$$
J(z\xi) = \bar z\,J(\xi), \qquad z\in\mathbb{C},\ \xi\in\mathcal{H}.
$$
The operator form of this statement is
$$
J\,i\,J = -i,
$$
with $i$ the scalar imaginary. The modular conjugation does not commute with $i$; it **inverts** it. Every modular quantity that carries a factor of $i$ — the generator of the flow, the imaginary-time displacement of the KMS condition, the imaginary vector part of a density matrix — is conjugated by $J$. This is the first trap: treating $J$ as a unitary (linear) involution loses the conjugation and reverses the resulting flow.

## Why the Hypotheses Are Load-Bearing

**Cyclicity** is what gives $S_0$ a dense domain. If $M\Omega$ were not dense in $\mathcal{H}$, the polar decomposition of the (then not densely defined) operator would not be available.

**Separation** is what makes $S_0$ single-valued. Without it there are $A\in M$ with $A\Omega=0$ but $A^*\Omega\neq0$, and the rule $A\Omega\mapsto A^*\Omega$ has no content.

Both failures are visible in the defining representation of $M_2(\mathbb{C})$ on $\mathbb{C}^2$. Let $\Omega=e_1$. The vector is cyclic, since $M_2(\mathbb{C})e_1=\mathbb{C}^2$, but it is not separating, since $E_{22}\Omega=0$ with $E_{22}\neq0$. The Tomita operator is not merely unproven — it is ill-defined: for $A=E_{12}$,
$$
A\Omega=E_{12}e_1=0, \qquad A^*\Omega=E_{12}^\dagger e_1=E_{21}e_1=e_2\neq0 .
$$
The same vector $0$ has the two images $0$ and $e_2$, so no polar decomposition follows. Equivalently, the vector state $\omega(A)=\langle e_1,Ae_1\rangle$ is not faithful, since $\omega(E_{22})=0$ while $E_{22}>0$.

**Faithfulness is the invariant form of the hypothesis.** In the GNS representation of a normal state $\omega$, the GNS vector $\Omega$ is cyclic and separating for $M$ if and only if $\omega$ is faithful. So "cyclic and separating" is not a technicality about a vector; it is the statement that the state assigns a nonzero expectation to every nonzero positive element. A pure state on $M_2(\mathbb{C})$ fails it; a faithful state, with positive-definite density, passes it.

## The Modular Flow Is the KMS Flow

The modular flow is not an auxiliary construction: it is exactly the flow for which the state satisfies the KMS condition. The precise statement, due to Takesaki and Winnink, is the following.

**Theorem.** Let $\omega$ be a faithful normal state on $M$ with modular group $\sigma_t$ constructed as above, and normalize the inverse temperature to $\beta=1$. Then $\omega$ satisfies the KMS condition with respect to the flow $t\mapsto\sigma_{-t}$: for all $A,B\in M$ the function
$$
F_{AB}(t) := \omega\big(A\,\sigma_{-t}(B)\big)
$$
extends analytically to the strip $0<\mathrm{Im}\,t<1$ and satisfies, on its boundary,
$$
F_{AB}(t+i) = \omega\big(\sigma_{-t}(B)\,A\big) = F_{BA}(-t),
$$
the last equality by the invariance of $\omega$ under the modular flow.

The normalization $\beta=1$ is a choice of scale for the modular parameter. The parent article's inverse temperature is recovered by rescaling, $t\mapsto t/\beta$ in the flow, and its boundary relation $F_{AB}(t+i\beta)=F_{BA}(-t)$ is the same statement at width $\beta$ rather than width $1$. The parent's **modular Hamiltonian** is the generator of this flow: writing $K=-\log\rho$, the finite-dimensional flow below is $\sigma_t(A)=e^{-itK}Ae^{itK}$, so that
$$
\frac{d}{dt}\sigma_t(A)\Big|_{t=0} = -i[K,A],
$$
and the parent article's algebraic fact that $K$ is a Hermitian element of the algebra, hence lies in $\mathbb{M}_+$, is the statement that the flow has an $\mathbb{M}_+$-valued generator. What the present article adds to the parent is the operator $S$: the parent stated the KMS relation, and $S$ is the object whose polar decomposition produces the flow for which that relation holds.

## The Finite-Dimensional Realization in the Biquaternion Algebra

Now build $S$ and its polar decomposition explicitly.

### The GNS Hilbert Space

Take $M=\mathbb{B}\cong M_2(\mathbb{C})$, and let $\tilde\rho\in\mathbb{M}_+$ be positive definite with $\mathrm{Tr}(\tilde\rho)=1$. On the vector space $\mathbb{B}$ put the inner product
$$
\langle \tilde{A},\tilde{B}\rangle_{\tilde\rho} := \mathrm{Tr}\big(\tilde\rho\,\tilde{A}^\dagger\tilde{B}\big),
$$
let $M$ act by left multiplication, $\pi(\tilde{A})\tilde{B}=\tilde{A}\tilde{B}$, and take the vector
$$
\Omega := e_0 .
$$
This is the GNS construction of the state
$$
\omega(\tilde{A}) = \langle\Omega,\pi(\tilde{A})\Omega\rangle_{\tilde\rho} = \mathrm{Tr}(\tilde\rho\,\tilde{A}).
$$
Because $\tilde\rho$ is positive definite the form is nondegenerate and the state is faithful, and $\Omega=e_0$ is cyclic and separating: cyclic because $\pi(\tilde{A})e_0=\tilde{A}$ runs over all of $\mathbb{B}$, and separating because $\tilde{A}e_0=\tilde{A}=0$ forces $\tilde{A}=0$. The hypothesis of the Tomita construction is thus, in this model, exactly the positivity of the density.

### The Tomita Operator, the Modular Operator, and the Modular Conjugation

Identifying the vector $\pi(\tilde{A})\Omega=\tilde{A}e_0$ with the algebra element $\tilde{A}$ (the Hilbert space is $\mathbb{B}$ itself), the Tomita operator is
$$
S_0(\tilde{A}) = \tilde{A}^\dagger .
$$
**The Tomita operator of the biquaternion algebra is its Hermitian conjugation.** It is anti-linear because $\dagger$ conjugates the coefficients: for $\tilde{A}=\sum_\mu Q_\mu e_\mu$ one has $\tilde{A}^\dagger=\bar Q_0e_0-\sum_{k=1}^{3}\bar Q_ke_k$, using $e_0^\dagger=e_0$ and $e_k^\dagger=-e_k$. The same conjugation of coefficients is what conjugates $i$, so the anti-linearity of $S_0$ and the conjugation of the scalar imaginary are one and the same operation in this framework.

The Hilbert-space adjoint of the anti-linear $S_0$, defined by
$$
\langle S_0\tilde{A},\tilde{B}\rangle_{\tilde\rho}=\overline{\langle\tilde{A},S_0^*\tilde{B}\rangle_{\tilde\rho}},
$$
is
$$
S_0^*(\tilde{B}) = \tilde\rho\,\tilde{B}^\dagger\tilde\rho^{-1},
$$
whence
$$
\Delta(\tilde{A}) = S_0^*S_0(\tilde{A}) = \tilde\rho\,\tilde{A}\,\tilde\rho^{-1}, \qquad
\Delta^{1/2}(\tilde{A})=\tilde\rho^{1/2}\tilde{A}\tilde\rho^{-1/2}.
$$
The polar decomposition $S_0=J\Delta^{1/2}$ then gives
$$
J(\tilde{A}) = \tilde\rho^{1/2}\tilde{A}^\dagger\tilde\rho^{-1/2}.
$$
The **modular flow** is
$$
\sigma_t(\tilde{A}) = \Delta^{it}\tilde{A}\Delta^{-it} = \tilde\rho^{it}\tilde{A}\tilde\rho^{-it},
$$
which is an **inner** automorphism of $\mathbb{B}$, implemented by the unitary $\tilde\rho^{it}\in\mathbb{B}$. It preserves Hermitian conjugation, $\sigma_t(\tilde{A}^\dagger)=\sigma_t(\tilde{A})^\dagger$, and hence acts on $\mathbb{M}_+$ and $\mathbb{M}_-$ separately. With
$$
\tilde K := -\log\tilde\rho \ \in\mathbb{M}_+,
$$
one has $\tilde\rho^{it}=e^{-it\tilde K}$ and
$$
\sigma_t(\tilde{A})=e^{-it\tilde K}\tilde{A}\,e^{it\tilde K}, \qquad \frac{d}{dt}\sigma_t(\tilde{A})\Big|_{t=0}=-i[\tilde K,\tilde{A}].
$$

### The Identities, Verified

The identities $S_0=J\Delta^{1/2}$, $J^2=1$, $J\Delta J=\Delta^{-1}$, $J\,i\,J=-i$, the group law $\sigma_t\circ\sigma_s=\sigma_{t+s}$, the generator relation, and $JMJ=M'$ — with $M'$ the right multiplications $\tilde{B}\mapsto\tilde{B}\tilde{C}$ — were each verified in two independent ways: symbolically, and numerically to machine precision at a density chosen after the formulas rather than before them. They are recorded in the companion `.thinking` file. The finite-dimensional realization is therefore not an analogy: it is the theory, instantiated in the algebra the framework already uses.

### An Explicit Case

Take the faithful state with Bloch vector
$$
\tilde\rho=\tfrac12\big(e_0+i\mathbf{r}\cdot\mathbf{e}\big),\qquad \mathbf{r}=\big(\tfrac{3}{10},\tfrac{2}{5},-\tfrac15\big),\qquad |\mathbf{r}|^2=\tfrac{29}{100}<1 .
$$
Its eigenvalues are $\lambda_\pm=\tfrac12\pm\tfrac{\sqrt{29}}{20}$, and
$$
\tilde K=-\log\tilde\rho=a_0e_0+i\mathbf{a}\cdot\mathbf{e},\qquad
a_0=-\tfrac12\log\det\tilde\rho=-\tfrac12\log\tfrac{71}{400}=0.864392\ldots,\qquad
\mathbf{a}=-\tfrac12\log\frac{\lambda_+}{\lambda_-}\,\hat{\mathbf{r}},
$$
with $\mathbf{a}=(-0.335401,-0.447202,0.223601)$. The direction $\mathbf{r}$ is deliberately neither an axis of the basis nor the thermal direction. For this state the KMS relation was evaluated at several real $t$ with generic $\tilde{A},\tilde{B}$: $F_{AB}(t+i)$ agrees with $\omega(\sigma_{-t}(B)A)$ and with $F_{BA}(-t)$ to machine precision, and the flow identities hold to the same order.

A second, physical case ties the construction to the parent article and to *The Partition Function in Biquaternionic Form*. For the single fermionic mode of the Fock-space article, with $\tilde H=\omega\tilde N_{\mathrm{tr}}$ and $\tilde N_{\mathrm{tr}}=\tfrac12(e_0-ie_3)$, the thermal state at $\beta=1.2$, $\omega=0.9$ is $\tilde\rho=\mathrm{diag}(0.746494,0.253506)$ in the $e_3$ basis (the occupied mode second, so that $\tilde N_{\mathrm{tr}}\mapsto\mathrm{diag}(0,1)$), and
$$
\tilde K=-\log\tilde\rho=\mathrm{diag}(0.292368,1.372368)=\beta\tilde H+(\log Z)e_0,
$$
with $Z=1+e^{-\beta\omega}=1.339596$, in agreement with the partition-function article's $K=\beta H+\log Z\,e_0$ and with that article's partition function.

## The Biquaternion Candidate for $S$

The framework supplies a natural candidate for $S$, and it is the Hermitian conjugation $\dagger$ itself:
$$
S_0:\ \tilde{A}\mapsto\tilde{A}^\dagger .
$$
This is not a choice made to fit the theory; it is the involution that defines the framework's two sectors, $\mathbb{M}_+$ being the $+1$ eigenspace of $\dagger$ and $\mathbb{M}_-$ the $-1$ eigenspace. Two remarks.

**The candidate satisfies the hypotheses.** With $\Omega=e_0$, cyclicity and separation hold automatically, and the state is faithful exactly when $\tilde\rho>0$. So the pair $(\mathbb{B},\Omega)$ with $\dagger$ as the involution is a genuine instance of the construction, not a formal resemblance. It also explains the anti-linearity: the Hermitian conjugation of $\mathbb{B}$ conjugates the coefficients, which is the same operation that conjugates $i$, so the anti-unitary character of $J$ is inherited from the framework's own conjugation rather than imported.

**The state is not supplied.** $S_0$ as a map is state-independent — $\tilde{A}\mapsto\tilde{A}^\dagger$ for every $\tilde\rho$ — but the polar decomposition is not: $\Delta$ and $J$ depend on $\tilde\rho$, through the inner product. And the framework's most distinguished state is the tracial one,
$$
\tilde\rho=\tfrac12 e_0 \qquad(\mathbf{r}=0),
$$
for which
$$
\Delta=1, \qquad J=S_0=\dagger, \qquad \sigma_t=\mathrm{id} :
$$
the modular flow is trivial. A nontrivial modular flow requires a nontracial state. The natural family is the thermal states $\tilde\rho=e^{-\beta\tilde H}/\mathrm{Tr}(e^{-\beta\tilde H})$ with $\tilde H\in\mathbb{M}_+$, and for those $\tilde K=-\log\tilde\rho$ generates the flow; but the algebra itself does not select one. **This is a gap, and it is left visible:** the framework supplies $S$, supplies a family of states, and supplies no dynamics that chooses among them.

## The Type of the Algebra and Inner Versus Outer Modular Flow

The finite-dimensional algebra is a factor of **type I$_2$**: a finite factor is I$_n$ exactly when it is $M_n(\mathbb{C})$, and $\mathbb{B}\cong M_2(\mathbb{C})$, and it is semifinite: it carries a trace, and in the model above its modular flow is inner, implemented by the unitary $\tilde\rho^{it}$ inside $\mathbb{B}$,
$$
\sigma_t(\tilde{A})=\tilde\rho^{it}\tilde{A}\tilde\rho^{-it},\qquad \tilde\rho^{it}\in\mathbb{B}.
$$
No object outside the algebra is needed to implement it. This is the generic behavior of a semifinite factor: **for a semifinite factor the modular flow of any faithful normal state is inner for every $t$.**

To describe the non-semifinite cases one uses the Connes invariant. For a factor $M$ the map
$$
\delta:\mathbb{R}\longrightarrow\operatorname{Out}(M),\qquad t\longmapsto[\sigma_t],
$$
assigning to $t$ the class of the modular automorphism in the outer automorphism group, is a homomorphism, and its kernel determines the type:

| Kernel of $\delta$ | Type of $M$ | Modular flow |
|---|---|---|
| all of $\mathbb{R}$ | I, II (semifinite) | inner for every $t$ |
| discrete subgroup generated by $x>0$ | III$_\lambda$, $\lambda=e^{-2\pi/x}$ | inner exactly on the subgroup |
| dense proper subgroup | III$_0$ | inner on a dense set, outer elsewhere |
| trivial, $\{0\}$ | III$_1$ | outer for every $t\neq0$ |

Read off the last two rows: for a type III$_1$ factor the kernel is trivial, so the modular flow is **outer at every nonzero time**, and for type III$_\lambda$ it is inner only at the discrete times in the kernel. The statement that the modular flow is inner *only* for type III$_1$ is therefore the reverse of the classification: III$_1$ is the case that is outer at every nonzero $t$, and it is the **semifinite** factors — type I, including the finite-dimensional $\mathbb{B}$, and type II — for which the modular flow is everywhere inner. The inner/outer behavior is not a marker of III$_1$ but its opposite.

The KMS connection does not depend on this. The theorem of the earlier section — that a faithful normal state is a KMS state for its modular flow — holds for every type. What the type controls is whether that flow can be absorbed into the algebra as an inner dynamics (semifinite, where it is conjugation by $\tilde\rho^{it}$) or is a genuinely new flow that no element of the algebra implements (type III). Because $\mathbb{B}$ is finite-dimensional it is on the semifinite side, and the outer-flow phenomenon — the reason Tomita–Takesaki theory is indispensable for type III factors — **cannot occur inside $\mathbb{B}$**. An outer modular flow would have to live in an infinite-dimensional algebra, for instance a field algebra built on a $\mathbb{B}$-module as in the Fock-space companion article. This is a second gap, and it is structural: the framework's finite-dimensional algebra admits the construction and lies entirely on the semifinite side of the inner/outer distinction.

## What Is Established and What Is a Gap

**Established (theorem).**

- The Tomita–Takesaki construction: $S$, $\Delta$, $J$, the identities $S^2=1$, $J^2=1$, $J\Delta J=\Delta^{-1}$, $JMJ=M'$, and the modular group $\sigma_t$.
- The equivalence, in a GNS representation, of "cyclic and separating" with "faithful".
- The Takesaki–Winnink theorem: the modular flow is the KMS flow, normalized to $\beta=1$, which is the link to the parent article.
- Connes' classification of factors by the kernel of $\delta$, and the inner/outer behavior of the modular flow.

**Established (recomputed here).**

- $M=\mathbb{B}$, with the GNS inner product $\langle\tilde{A},\tilde{B}\rangle_{\tilde\rho}=\mathrm{Tr}(\tilde\rho\tilde{A}^\dagger\tilde{B})$ and $\Omega=e_0$, is an instance; $S_0=\dagger$.
- $\Delta(\tilde{A})=\tilde\rho\tilde{A}\tilde\rho^{-1}$, $\Delta^{1/2}(\tilde{A})=\tilde\rho^{1/2}\tilde{A}\tilde\rho^{-1/2}$, $J(\tilde{A})=\tilde\rho^{1/2}\tilde{A}^\dagger\tilde\rho^{-1/2}$, $\sigma_t(\tilde{A})=\tilde\rho^{it}\tilde{A}\tilde\rho^{-it}$.
- $J^2=1$, $J\Delta J=\Delta^{-1}$, $J\,i\,J=-i$, $\sigma_t\circ\sigma_s=\sigma_{t+s}$, $d\sigma_t/dt|_{t=0}=-i[\tilde{K},\tilde{A}]$, and $JMJ=M'$.
- $\tilde{K}=-\log\tilde\rho\in\mathbb{M}_+$, and for the thermal single mode $\tilde{K}=\beta\tilde{H}+(\log Z)e_0$, matching the parent and partition-function articles.
- $\mathbb{B}\cong M_2(\mathbb{C})$ is type I$_2$; its modular flow is inner, implemented by $\tilde\rho^{it}\in\mathbb{B}$.

**Interpretation.**

- That the framework's Hermitian conjugation $\dagger$ is the natural Tomita operator, and that its coefficient-conjugation is the origin of the anti-unitarity of $J$ and of the conjugation of $i$.

**Gap.**

- The framework admits a modular flow but does not select a state; the distinguished tracial state gives the trivial flow $\sigma_t=\mathrm{id}$.
- $\mathbb{B}$ is type I$_2$ and semifinite, so the genuinely type-III, outer modular flow lies outside it; realizing it requires an infinite-dimensional algebra built on $\mathbb{B}$-modules.
- The action of $J$ on the sector decomposition and on the fermionic one-mode structure, in particular the parity $(-1)^F=ie_3$, has not been worked out.
- No empirical consequence is derived.

## Summary

The Tomita–Takesaki construction turns a cyclic and separating vector on a von Neumann algebra into an anti-linear involution $S$, and its polar decomposition $S=J\Delta^{1/2}$ into a positive modular operator $\Delta$, an anti-unitary modular conjugation $J$ with $J^2=1$ and $JMJ=M'$, and a modular automorphism group $\sigma_t(A)=\Delta^{it}A\Delta^{-it}$.

In the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$, with the GNS inner product $\langle\tilde{A},\tilde{B}\rangle_{\tilde\rho}=\mathrm{Tr}(\tilde\rho\tilde{A}^\dagger\tilde{B})$ and the cyclic separating vector $\Omega=e_0$, the Tomita operator is the Hermitian conjugation,
$$
S_0:\tilde{A}\mapsto\tilde{A}^\dagger,
$$
and the polar decomposition is
$$
\Delta(\tilde{A})=\tilde\rho\tilde{A}\tilde\rho^{-1},\qquad
J(\tilde{A})=\tilde\rho^{1/2}\tilde{A}^\dagger\tilde\rho^{-1/2},\qquad
\sigma_t(\tilde{A})=\tilde\rho^{it}\tilde{A}\tilde\rho^{-it}.
$$
The identities $J^2=1$, $J\Delta J=\Delta^{-1}$ and $J\,i\,J=-i$ — the modular conjugation conjugates the scalar imaginary — together with the group law of the flow, were verified symbolically and numerically on an explicit faithful state whose Bloch vector was chosen independently of the derivation.

The modular flow is the KMS flow: normalized to $\beta=1$, a faithful normal state satisfies the KMS boundary relation with respect to $\sigma_{-t}$, and the parent article's modular Hamiltonian $K=-\log\tilde\rho\in\mathbb{M}_+$ generates it, $d\sigma_t/dt|_{t=0}=-i[K,A]$. The parent stated the condition; this article has constructed the operator whose polar decomposition produces the flow for which it holds.

Two honest limitations. The framework supplies $S$ and a family of faithful states, but no dynamics that selects a state, and the distinguished tracial state gives the trivial flow. And $\mathbb{B}$ is a type I$_2$ factor, hence semifinite, so its modular flow is inner — implemented by $\tilde\rho^{it}\in\mathbb{B}$ — while the outer modular flow of type III factors, the case in which the theory is indispensable, cannot occur inside the finite-dimensional algebra. The modular flow is inner for the semifinite factors and outer for III$_1$; the reverse reading is a common error. Whether an infinite-dimensional algebra built on $\mathbb{B}$-modules realizes the type III case is open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\dagger$ | Hermitian conjugation; the Tomita involution $A^*$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) subspaces |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula; $\mathrm{Tr}(e_0)=2$ |
| $\mathcal{H},M,\Omega$ | Hilbert space, von Neumann algebra, cyclic separating vector |
| $S_0,S$ | Tomita operator $A\Omega\mapsto A^*\Omega$ and its closure |
| $\Delta=S^*S$ | Modular operator |
| $J$ | Modular conjugation, anti-unitary, $J^2=1$ |
| $\sigma_t(A)=\Delta^{it}A\Delta^{-it}$ | Modular automorphism group |
| $\tilde\rho\in\mathbb{M}_+$ | Faithful state (positive definite, trace one) |
| $\langle\tilde{A},\tilde{B}\rangle_{\tilde\rho}=\mathrm{Tr}(\tilde\rho\tilde{A}^\dagger\tilde{B})$ | GNS inner product on $\mathbb{B}$ |
| $\tilde{K}=-\log\tilde\rho$ | Modular Hamiltonian, in $\mathbb{M}_+$ |
| $F_{AB}(t+i)=F_{BA}(-t)$ | KMS boundary relation (parent article) |
| $\delta:\mathbb{R}\to\operatorname{Out}(M)$ | Connes invariant, $t\mapsto[\sigma_t]$ |

## Further Reading

- Companion article *The KMS Condition and the Biquaternion Framework*, for the KMS condition, the imaginary-time strip, and the modular Hamiltonian $K=-\log\rho$.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the Hermitian subspace, the trace formula, and states as elements of $\mathbb{M}_+$.
- Companion article *The Partition Function in Biquaternionic Form*, for the Gibbs state and $K=\beta H+\log Z\,e_0$.
- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the single fermionic mode, $\tilde{N}_{\mathrm{tr}}$, and the parity $(-1)^F$.
- Companion article *Introduction to the Biquaternion Universe*, for the algebra and its two sectors.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material sector and the four-vectors.
- Companion article *The Wick Rotation in the Biquaternion Universe*, for the $i$-exchange between the sectors.
- Companion article *Quantum Mechanics in Biquaternionic Form*, for the operator algebra of the informational sector.
- M. Takesaki, *Tomita's Theory of Modular Hilbert Algebras and Its Applications* (Springer, 1970), for the original development of the modular theory.
- M. Takesaki, *Theory of Operator Algebras II* (Springer, 2003), for the modular automorphism group and its properties.
- O. Bratteli and D. W. Robinson, *Operator Algebras and Quantum Statistical Mechanics* 1–2 (Springer, 1987/1997), for the Tomita–Takesaki theorem and the KMS condition.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic formulation and the modular structure.
- A. Connes, "Une classification des facteurs de type III," *Annales Scientifiques de l'École Normale Supérieure* **6** (1973) 133–252, for the kernel of $\delta$ and the classification used above.
- Ş. Strătilă, *Modular Theory in Operator Algebras* (Abacus Press, 1981), for a systematic treatment of modular theory.
