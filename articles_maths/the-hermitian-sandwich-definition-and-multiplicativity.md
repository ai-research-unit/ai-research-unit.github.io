# __The Hermitian Sandwich: Definition and Multiplicativity__

## Introduction: The Real Cone

**The operator.** For $\tilde Q\in\mathbb{B}$, the **Hermitian sandwich** is

$$
\Theta_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*}.
$$

It is the two-sided operator $T_{\tilde Q,\tilde Q^{*}}$: the second slot is tied to the first by the involution. The two-sided family is a complex cone of complex dimension seven; the sandwich is the graph of the involution inside it, a **real** cone of real dimension seven. The phase of the parameter cancels, $\Theta_{\omega\tilde Q}=\Theta_{\tilde Q}$ for $|\omega|=1$, and the square of the modulus is the only scale. The image is not a complex subspace: the sandwich is quadratic in $\tilde Q$, and a complex rescaling of $\tilde Q$ rescales the operator by the square of the modulus, a positive real number.

**The results.** The article states five things. The sandwich is multiplicative up to the order of the factors, $\Theta_{\tilde Q}\Theta_{\tilde P}=\Theta_{\tilde Q\tilde P}$, and its defect from an algebra automorphism is the operator $e_t-\tilde Q^{*}\tilde Q$. It preserves the Hermitian and anti-Hermitian halves for every parameter, and it preserves the finer subspace structure exactly when the parameter is a central multiple of a real unit quaternion. It scales the norm by $|\langle\tilde Q\rangle_{\natural}|^{2}$. Its parameter is defined modulo the central phase, which gives the real dimension seven. It meets each one-sided family in the closed ray of nonnegative multiples of the identity, and its spectrum is the four products of the eigenvalues of the $2\times2$ model with their conjugates. On the unit-norm slice the parameter map is the twofold cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$; on the full unit group it has kernel $U(1)$ and image $CO^{+}(1,3)$.

**Verification.** The matrix verification of the spectrum and of the Lorentz action is in *$M_2(\mathbb{C})$ Model : The Sandwich* and *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Sandwich*. The present article states the operator results and sketches the proofs; no case study is cited as proof. The notation of the families is that of *Conventions of the Operator Families*: $\Theta_{\tilde Q}$ is the sandwich, $T_{\tilde Q,\tilde P}$ the two-sided operator, $L(\mathbb{B})$ and $R(\mathbb{B})$ the two regular families, $\mathbb{M}_+$ and $\mathbb{M}_-$ the Hermitian and anti-Hermitian halves, $\langle\tilde Q\rangle_{\natural}$ the quaternionic norm, and $\operatorname{End}_{LR\ast}(\mathbb{B})$ the set of sandwiches. The involution is the algebra's conjugation, the one whose matrix is the dagger in the matrix models.

**The real cone.** The set $\operatorname{End}_{LR\ast}(\mathbb{B})=\{\Theta_{\tilde Q}:\tilde Q\in\mathbb{B}\}$ is a cone: it is closed under multiplication by nonnegative real numbers, and it is not closed under addition. It is a real cone of real dimension seven, not a complex cone. The two-sided cone $\operatorname{End}_{LR}(\mathbb{B})$ is complex of complex dimension seven, and the sandwich is a real slice of it, a proper subset, the slice on which the two parameters are conjugate.

## The Operator $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$

### The Definition

**Definition.** For $\tilde Q\in\mathbb{B}$, $\Theta_{\tilde Q}$ is the map

$$
\Theta_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},\qquad
\Theta_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*}.
$$

It is the composite $L_{\tilde Q}R_{\tilde Q^{*}}$ of a left multiplication and a right multiplication. It is $\mathbb{C}$-linear in $\tilde X$, because $L_{\tilde Q}$ and $R_{\tilde Q^{*}}$ are $\mathbb{C}$-linear. It is invertible exactly when $\tilde Q$ is a unit, and then

$$
\Theta_{\tilde Q}^{-1}=\Theta_{\tilde Q^{-1}}.
$$

If $\tilde Q$ is not a unit, the map has a nonzero kernel: a nonzero $\tilde X$ with $\tilde Q\tilde X=0$ or $\tilde X\tilde Q^{*}=0$ is sent to zero.

**The zero and the identity.** $\Theta_0=0$, and $\Theta_{e_t}=\mathrm{id}$. The identity is the sandwich of the unit, and the identity operator is also $\Theta_{\omega e_t}$ for every central phase $\omega$ of modulus one. The map $\tilde Q\mapsto\Theta_{\tilde Q}$ is not linear: it is quadratic, with the cross terms $\tilde Q\tilde X\tilde P^{*}+\tilde P\tilde X\tilde Q^{*}$ in $\Theta_{\tilde Q+\tilde P}$.

**The scaling.** For $\lambda\in\mathbb{C}$,

$$
\Theta_{\lambda\tilde Q}=|\lambda|^{2}\,\Theta_{\tilde Q},
$$

because $(\lambda\tilde Q)^{*}=\bar\lambda\tilde Q^{*}$. The phase of $\lambda$ cancels and the modulus squared remains. In particular $\Theta_{\omega\tilde Q}=\Theta_{\tilde Q}$ for every $\omega$ with $|\omega|=1$.

### The Member $T_{\tilde Q,\tilde Q^{*}}$

**The two-sided family.** The sandwich is the member of the two-sided family whose parameters are tied:

$$
\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}.
$$

The two-sided family is the set of decomposable tensors $\tilde Q\otimes\tilde P^{\mathrm{opp}}$, a complex cone of complex dimension seven in the complex sixteen-dimensional algebra. The sandwich is the graph of the involution $\tilde P=\tilde Q^{*}$ inside that cone.

**The graph is real, not complex.** For $\lambda\in\mathbb{C}^{\times}$ the pair $(\lambda\tilde Q,(\lambda\tilde Q)^{*})=(\lambda\tilde Q,\bar\lambda\tilde Q^{*})$ is not $\lambda(\tilde Q,\tilde Q^{*})$ unless $\lambda$ is real. The graph is therefore not a complex subcone: a complex rescaling of the pair leaves the graph, while the sandwich itself rescales by $|\lambda|^{2}$. The image is a real cone of real dimension seven. Its complex span is the whole endomorphism algebra: the graph is a real form of $\mathbb{B}\times\mathbb{B}$, and the bilinear map $T$ is surjective by the generation theorem of *Two-Sided Operators on the Biquaternion Algebra*; the complex cone generated by a single sandwich is only a complex line, so the real cone is not the complex cone. Over $\mathbb{R}$ the sandwich cone is a proper subset of the ambient space: it is a real cone of real dimension seven, not a real vector space, and its complex span is the whole algebra.

**The member.** The set is named in *Conventions of the Operator Families*; this article proves the row: $\operatorname{End}_{LR\ast}(\mathbb{B})=\{\Theta_{\tilde Q}\}$ is a real cone of real dimension seven, contained in $\operatorname{End}_{LR}(\mathbb{B})$ and meeting each one-sided family in the closed ray of the identity. The sections below give the proofs.

## Multiplicativity

### $\Theta_{\tilde Q}\Theta_{\tilde P}=\Theta_{\tilde Q\tilde P}$

**Proposition (multiplicativity).** For all $\tilde Q,\tilde P\in\mathbb{B}$,

$$
\Theta_{\tilde Q}\,\Theta_{\tilde P}=\Theta_{\tilde Q\tilde P}.
$$

*Proof.* For every $\tilde X$,

$$
\Theta_{\tilde Q}\bigl(\Theta_{\tilde P}(\tilde X)\bigr)
=\tilde Q\,\tilde P\,\tilde X\,\tilde P^{*}\,\tilde Q^{*}
=(\tilde Q\tilde P)\,\tilde X\,(\tilde Q\tilde P)^{*},
$$

because $(\tilde Q\tilde P)^{*}=\tilde P^{*}\tilde Q^{*}$. The right-hand side is $\Theta_{\tilde Q\tilde P}(\tilde X)$.

**The order.** The composition is $\Theta_{\tilde Q}\Theta_{\tilde P}=\Theta_{\tilde Q\tilde P}$; the map $\tilde Q\mapsto\Theta_{\tilde Q}$ is therefore a homomorphism from the opposite algebra $\mathbb{B}^{\mathrm{opp}}$ to $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, not from $\mathbb{B}$. The reversal is the involution: the star reverses the order of the factors. In particular the image is a group anti-isomorphic to the unit group, and $\Theta_{\tilde Q}^{-1}=\Theta_{\tilde Q^{-1}}$ is the inverse in the image.

**The kernel of the parameter map.** If $\Theta_{\tilde Q}=\mathrm{id}$, then $\tilde Q\tilde X\tilde Q^{*}=\tilde X$ for all $\tilde X$. At $\tilde X=e_t$ this gives $\tilde Q\tilde Q^{*}=e_t$; the parameter is a unit of norm one. The identity sandwich is $\Theta_{\omega e_t}$ for every central phase $\omega$ with $|\omega|=1$, and these are all: the kernel of the parameter map on the unit group is the central $U(1)$. The proof of the exact kernel is in §*The Parameter Modulo $\mathrm{U}(1)$*.

### The Defect of an Automorphism

**The defect.** The sandwich is not an algebra automorphism in general. For all $\tilde X,\tilde Y$,

$$
\Theta_{\tilde Q}(\tilde X\tilde Y)-\Theta_{\tilde Q}(\tilde X)\,\Theta_{\tilde Q}(\tilde Y)
=\tilde Q\,\tilde X\,\bigl(e_t-\tilde Q^{*}\tilde Q\bigr)\,\tilde Y\,\tilde Q^{*}.
$$

The **defect** is the element $e_t-\tilde Q^{*}\tilde Q$, placed between the two arguments. The sandwich is an algebra automorphism exactly when the defect vanishes, that is, when $\tilde Q^{*}\tilde Q=e_t$. For an invertible $\tilde Q$ this is the $*$-unitary group.

**The scaled case.** If $\tilde Q^{*}\tilde Q=\lambda e_t$ with $\lambda>0$, then

$$
\Theta_{\tilde Q}(\tilde X)\,\Theta_{\tilde Q}(\tilde Y)
=\lambda\,\Theta_{\tilde Q}(\tilde X\tilde Y),
$$

so the sandwich is a scalar multiple of an algebra automorphism; it is an automorphism exactly when $\lambda=1$. The central multiples of real unit quaternions with a nontrivial scale preserve the subspace structure of §*The Two Halves* but are not algebra automorphisms. The defect $e_t-\tilde Q^{*}\tilde Q=(1-\lambda)e_t$ measures the scale.

**The two laws.** The composition law $\Theta_{\tilde Q}\Theta_{\tilde P}=\Theta_{\tilde Q\tilde P}$ holds for every pair, and it concerns the composition of two sandwiches. The automorphism law $\Theta_{\tilde Q}(\tilde X\tilde Y)=\Theta_{\tilde Q}(\tilde X)\Theta_{\tilde Q}(\tilde Y)$ holds only under the defect criterion $\tilde Q^{*}\tilde Q=e_t$, not under the weaker subspace criterion. The two laws are different; the first is the multiplication of the parameter, the second is the preservation of the algebra's product.

## The Two Halves

### Preservation of $\mathbb{M}_+$ and $\mathbb{M}_-$

**The halves.** The Hermitian half and the anti-Hermitian half are

$$
\mathbb{M}_+=\{\tilde X:\tilde X^{*}=\tilde X\},\qquad
\mathbb{M}_-=\{\tilde X:\tilde X^{*}=-\tilde X\}.
$$

They are the real eigenspaces of the involution. Each is a real subspace of real dimension four; they are exchanged by multiplication by the central $i$, and their sum is the real algebra of real dimension eight. They are not complex subspaces: multiplication by $i$ moves one to the other.

**Preservation.** If $\tilde X^{*}=\pm\tilde X$, then

$$
\bigl(\tilde Q\tilde X\tilde Q^{*}\bigr)^{*}
=\tilde Q\tilde X^{*}\tilde Q^{*}
=\pm\tilde Q\tilde X\tilde Q^{*}.
$$

So $\Theta_{\tilde Q}$ preserves each half for every $\tilde Q$, without a unit or norm-one hypothesis. The two statements are consequences of the involution, not of the norm.

**The exchange.** Multiplication by the central $i$ exchanges the halves: $\tilde X\in\mathbb{M}_+$ iff $i\tilde X\in\mathbb{M}_-$. The sandwich commutes with the exchange, because $i$ is central:
$$
\Theta_{\tilde Q}(i\tilde X)=i\,\Theta_{\tilde Q}(\tilde X).
$$
The two halves are one action read in two real forms; the Lorentz transformation on $\mathbb{M}_-$ is the congruence on $\mathbb{M}_+$ composed with the exchange.

### The Criterion on $\tilde Q$

**The two halves are always preserved.** The criterion is not for the halves; it is for the finer subspace structure. The centre, the vector subspace, the real quaternion subspace and the anti-quaternion subspace are preserved exactly when $\tilde Q$ is a central multiple of a real unit quaternion.

**Theorem (the criterion).** For a unit $\tilde Q$, the following are equivalent:

1. $\Theta_{\tilde Q}$ maps each of the six remarkable subspaces to itself;
2. $\tilde Q=\tilde A\,\tilde u$ with $\tilde A$ central and $\tilde u$ a real unit quaternion;
3. $\tilde Q\tilde Q^{*}$ is a positive real multiple of $e_t$;
4. $\tilde Q^{*}\tilde Q$ is a positive real multiple of $e_t$.

For a general element the same equivalences hold with $\tilde Q$ replaced by its unit part; the scale is central and preserves every subspace.

*Sketch.* $(2)\Rightarrow(3)$: a real unit quaternion satisfies $\tilde u\tilde u^{*}=e_t$, so $\tilde Q\tilde Q^{*}=|\tilde A|^{2}e_t$. $(3)\Rightarrow(2)$: if $\tilde Q\tilde Q^{*}=\lambda e_t$ with $\lambda>0$, the principal square root of $\lambda$ normalises $\tilde Q$ to a unit element with $\tilde U\tilde U^{*}=e_t$; a unit element with $\tilde U\tilde U^{*}=e_t$ is a central phase times a real unit quaternion, by the polar decomposition. $(2)\Rightarrow(1)$: the central factor is a dilation, the real unit quaternion is a rotation of the vector space, and both preserve the six subspaces. $(1)\Rightarrow(3)$: if the centre is preserved, $\tilde Q\tilde Q^{*}$ is central; it is Hermitian positive, and a central Hermitian positive element of the algebra is a positive real multiple of $e_t$. The full proof is *The Polar Decomposition and Remarkable Subspaces*, §*Which Subspaces the Sandwich Preserves*.

**The group.** On the unit-norm slice the parameters are the real unit quaternions modulo sign, and they form $SO(3)$, of real dimension three. With the central dilations admitted they form $\mathbb{R}_{>0}\times SO(3)$, of real dimension four. The rotation group sits inside the six-dimensional operator group as the rotations sit inside the Lorentz group; the remaining three dimensions are the boosts, which move the centre and the vector subspace. The criterion is weaker than the vanishing of the defect: it allows a central scale, and the defect vanishes exactly on the unit-norm part of the set, the $*$-unitary group. The central multiples of real unit quaternions with a nontrivial scale are dilations composed with rotations; they preserve the subspaces but are not algebra automorphisms.

**The matrix check.** The matrix verification is in *$M_2(\mathbb{C})$ Model : The Sandwich*, §*The Congruence*, and in *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Sandwich*, §*Which Subspaces the Sandwich Preserves*.

## The Norm

### $\langle\Theta_{\tilde Q}(\tilde X)\rangle_{\natural}=|\langle\tilde Q\rangle_{\natural}|^{2}\langle\tilde X\rangle_{\natural}$

**Proposition (the norm scaling).** For all $\tilde Q,\tilde X\in\mathbb{B}$,

$$
\langle\Theta_{\tilde Q}(\tilde X)\rangle_{\natural}
=|\langle\tilde Q\rangle_{\natural}|^{2}\,\langle\tilde X\rangle_{\natural}.
$$

*Proof.* The quaternionic norm is multiplicative, $\langle AB\rangle_{\natural}=\langle A\rangle_{\natural}\langle B\rangle_{\natural}$, and $\langle\tilde Q^{*}\rangle_{\natural}=\overline{\langle\tilde Q\rangle_{\natural}}$. Hence
$$
\langle\tilde Q\tilde X\tilde Q^{*}\rangle_{\natural}
=\langle\tilde Q\rangle_{\natural}\langle\tilde X\rangle_{\natural}\overline{\langle\tilde Q\rangle_{\natural}}
=|\langle\tilde Q\rangle_{\natural}|^{2}\langle\tilde X\rangle_{\natural}.
$$

**The consequences.** The scaling factor is a nonnegative real number. The sign of the norm is preserved, so the positive and negative cones of the norm are each preserved; the null cone $\langle\tilde X\rangle_{\natural}=0$ is preserved, and the zero divisors map to zero divisors. The norm itself is preserved exactly when $|\langle\tilde Q\rangle_{\natural}|=1$, that is, on the unit-norm slice. The determinant in the $2\times2$ model is the norm and scales by $|\langle\tilde Q\rangle_{\natural}|^{2}$; in the $4\times4$ model the determinant is the square of the norm and scales by $|\langle\tilde Q\rangle_{\natural}|^{4}$, the eighth power of the modulus $r=|\langle\tilde Q\rangle_{\natural}|^{1/2}$.

### The Cancellation of the Phase

**The phase of the parameter.** For $\omega\in\mathrm{U}(1)$,

$$
\Theta_{\omega\tilde Q}=\Theta_{\tilde Q},\qquad
\langle\omega\tilde Q\rangle_{\natural}=\omega^{2}\langle\tilde Q\rangle_{\natural}.
$$

The phase of $\tilde Q$ cancels in the operator, and the phase of the norm cancels in the modulus: $|\langle\omega\tilde Q\rangle_{\natural}|=|\langle\tilde Q\rangle_{\natural}|$. The norm formula therefore depends only on the modulus of the norm, not on its argument.

**What the operator sees.** The sandwich sees the orbit $\mathrm{U}(1)\cdot\tilde Q$ and the modulus $|\langle\tilde Q\rangle_{\natural}|$. It does not see the phase of $\tilde Q$ or the phase of the norm. The parameter of the sandwich is a point of $\mathbb{B}/\mathrm{U}(1)$; the positive real scale is its modulus, and the phase is the kernel of the parameter map.

**The real form.** The norm is a complex quadratic form on the complex algebra; on the Hermitian half it is real, and on the anti-Hermitian half it is real with the opposite sign. The sandwich scales it by the nonnegative factor $|\langle\tilde Q\rangle_{\natural}|^{2}$, so it preserves the common zero set and the sign of the norm on each half. The two halves are the two real readings of the same complex form.

## The Parameter Modulo $\mathrm{U}(1)$

### The Real Dimension Seven

**The action.** The group $\mathrm{U}(1)=\{\omega e_t:|\omega|=1\}$ acts on the parameter by $\tilde Q\mapsto\omega\tilde Q$. The sandwich is invariant, by §*The Cancellation of the Phase*. The map $\tilde Q\mapsto\Theta_{\tilde Q}$ factors through the quotient $\mathbb{B}/\mathrm{U}(1)$.

**The fibre.** Suppose $\Theta_{\tilde Q}=\Theta_{\tilde P}$ with $\tilde Q,\tilde P\neq0$. Then $T_{\tilde Q,\tilde Q^{*}}=T_{\tilde P,\tilde P^{*}}$. By the fibre theorem of *Two-Sided Operators on the Biquaternion Algebra*, §*The Scaling Orbit*, the two pairs are proportional:

$$
\tilde P=\lambda\tilde Q,\qquad \tilde P^{*}=\lambda^{-1}\tilde Q^{*}
$$

for some $\lambda\in\mathbb{C}^{\times}$. Conjugating the first equation gives $\tilde P^{*}=\bar\lambda\tilde Q^{*}$; comparing with the second gives $\lambda^{-1}=\bar\lambda$, hence $|\lambda|=1$. Therefore $\tilde P=\lambda\tilde Q$ with $|\lambda|=1$, and the fibre is exactly the $\mathrm{U}(1)$ orbit. The zero operator is the image of $\tilde Q=0$ alone.

**The dimension.** The parameter space $\mathbb{B}$ has complex dimension four, real dimension eight. The $\mathrm{U}(1)$ orbit is one real dimension, and it acts freely on $\mathbb{B}\setminus\{0\}$. The quotient has real dimension $8-1=7$, and the cone has real dimension seven. The dimension is real, not complex: the quotient $\mathbb{B}/\mathrm{U}(1)$ is the real cone over $\mathbb{CP}^{3}$, not a complex vector space, and the parameter map is quadratic. This is the row of the table: $\operatorname{End}_{LR\ast}(\mathbb{B})$ has real dimension seven, while $\operatorname{End}_{LR}(\mathbb{B})$ has complex dimension seven.

**The cone.** The image is a cone over the complex projective space $\mathbb{CP}^{3}$: the parameter modulo the positive real scale and the phase. The quotient of $\mathbb{B}\setminus\{0\}$ by $\mathrm{U}(1)$ and $\mathbb{R}_{>0}$ is $\mathbb{CP}^{3}$, of real dimension six, and the cone has real dimension seven. The image is the set of sandwiches, a real cone of dimension seven. It is not a subspace: the sum of two sandwiches is not a sandwich in general, and the cone is not closed under multiplication by $i$ unless the parameter is scaled by a real number.

## The Intersections with $L(\mathbb{B})$ and $R(\mathbb{B})$

### The Closed Ray of the Identity

**The statement.** The sandwich cone meets each one-sided family in the same closed ray:

$$
\operatorname{End}_{LR\ast}(\mathbb{B})\cap L(\mathbb{B})
=\operatorname{End}_{LR\ast}(\mathbb{B})\cap R(\mathbb{B})
=\{t\,\mathrm{I}:t\ge0\}.
$$

The ray is the closed ray of nonnegative multiples of the identity; the identity is the point $t=1$, and the zero operator is the point $t=0$.

**The proof.** Write $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$. If $\Theta_{\tilde Q}=L_{\tilde A}$, then $R_{\tilde Q^{*}}=L_{\tilde A}L_{\tilde Q}^{-1}$ when $\tilde Q$ is a unit, so $R_{\tilde Q^{*}}$ lies in $L(\mathbb{B})\cap R(\mathbb{B})$. The intersection of the two one-sided families is the scalars, by *The Commutant of the Two Regular Families*, so $R_{\tilde Q^{*}}$ is a scalar; hence $\tilde Q^{*}$ is central and $\tilde Q$ is central. If $\tilde Q$ is not a unit and $\Theta_{\tilde Q}=L_{\tilde A}$, evaluating at $e_t$ gives $\tilde A=\tilde Q\tilde Q^{*}=\langle\tilde Q\rangle_{\natural}e_t$; if $\tilde Q$ is a null element this is zero, and then $\Theta_{\tilde Q}=0$, which forces $\tilde Q=0$. In every case $\tilde Q=\lambda e_t$, and $\Theta_{\tilde Q}=|\lambda|^{2}\mathrm{I}$ is a nonnegative multiple of the identity. The same argument with the roles exchanged gives the intersection with $R(\mathbb{B})$.

**The ray is not a subspace.** The ray is a half-line, not a line: the negative multiples of the identity are not in the cone, because they would require $|\lambda|^{2}<0$. The ray is a boundary face of the cone along the central direction; it is the only part of the sandwich cone that is one-sided. The two intersections are the same ray.

**The contrast.** The full product set of the two-sided family meets $L(\mathbb{B})$ in all of $L(\mathbb{B})$ and $R(\mathbb{B})$ in all of $R(\mathbb{B})$, because $T_{\tilde Q,e_t}=L_{\tilde Q}$ and $T_{e_t,\tilde P}=R_{\tilde P}$. The sandwich is the graph $\tilde P=\tilde Q^{*}$, and the graph meets the two axes only at the central ray. The two intersections of the product set are distinct; the two intersections of the sandwich are the same ray.

## The Spectrum

### The Four Products $\lambda_i\bar\lambda_j$

**The statement.** Let $\lambda_1,\lambda_2$ be the eigenvalues of the $2\times2$ matrix $\mathsf M_2(\tilde Q)$. The eigenvalues of $\Theta_{\tilde Q}$ on $\mathbb{B}$ are the four products

$$
\lambda_i\bar\lambda_j,\qquad i,j\in\{1,2\}.
$$

The trace and the determinant follow:

$$
\operatorname{Tr}\Theta_{\tilde Q}=|\lambda_1+\lambda_2|^{2}=4|Q_t|^{2},\qquad
\det\Theta_{\tilde Q}=|\lambda_1\lambda_2|^{4}=|\langle\tilde Q\rangle_{\natural}|^{4}.
$$

**The reading.** The diagonal products $\lambda_i\bar\lambda_i=|\lambda_i|^{2}$ are nonnegative real; the two off-diagonal products are conjugate to each other. The spectrum is invariant under the phase of $\tilde Q$, and it depends only on the eigenvalues of the $2\times2$ model. If $\tilde Q$ is a unit, all four products are nonzero; if $\tilde Q$ is a null element, at least one eigenvalue is zero, and at least two products vanish. If $\tilde Q$ is central, $\lambda_1=\lambda_2=\lambda$, and all four products are $|\lambda|^{2}$; the sandwich is the scalar $|\lambda|^{2}\mathrm{I}$.

**The verification.** The matrix verification is in *$M_2(\mathbb{C})$ Model : The Sandwich*, §*The Anti-Hermitian Half as Four-Vectors*, and in *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Sandwich*, §*The Two Halves Are One Action*. In the $2\times2$ model the sandwich is the congruence $X\mapsto MXM^{\dagger}$; its eigenvalues are the products of an eigenvalue of $M$ with the conjugate of an eigenvalue of $M$, which is the display. The abstract statement is the same computation read in the $2\times2$ model of the algebra; the spectrum is a similarity invariant, so the choice of model does not change it.

**The trace.** The trace is $|\operatorname{Tr}\mathsf M_2(\tilde Q)|^{2}=4|Q_t|^{2}$, the squared modulus of the trace of the model matrix. The determinant is the fourth power of the modulus of the norm, $|\langle\tilde Q\rangle_{\natural}|^{4}$, which is also the determinant of the sandwich as a linear operator on the complex four-dimensional algebra. The two invariants are real and nonnegative; the spectrum carries the phase information in its off-diagonal pair.

## The Image and the Kernel

### $\mathrm{U}(1)$ and $CO^{+}(1,3)$

**The parameter map on the unit group.** The map

$$
\Theta:\mathbb{B}^{\times}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\tilde Q\longmapsto\Theta_{\tilde Q}
$$

is a group anti-homomorphism. Its kernel is the central $\mathrm{U}(1)=\{\omega e_t:|\omega|=1\}$, by §*The Parameter Modulo $\mathrm{U}(1)$*. Its image, read on the anti-Hermitian half, is the conformal group

$$
CO^{+}(1,3)=\mathbb{R}_{>0}\cdot SO^{+}(1,3),
$$

of real dimension seven. The general element $\tilde Q=r\zeta\tilde U$ with $r>0$, $|\zeta|=1$ and $|\langle\tilde U\rangle_{\natural}|=1$ gives $\Theta_{\tilde Q}=r^{2}\Theta_{\tilde U}$: the phase cancels, the modulus squared is the dilation, and the unit part is the Lorentz transformation.

**The kernel of the linear map.** The kernel of the linear map $\Theta_{\tilde Q}$ for a fixed $\tilde Q$ is a different object. It is $\{0\}$ exactly when $\tilde Q$ is a unit; if $\tilde Q$ is a null element, the kernel is nonzero. The kernel of the parameter map is the $\mathrm{U}(1)$ orbit; the kernel of the linear map is $\{\tilde X:\tilde Q\tilde X\tilde Q^{*}=0\}$. The two kernels are stated separately, and neither is the other.

**The image of the linear map.** For a unit $\tilde Q$, $\Theta_{\tilde Q}$ is a linear isomorphism of $\mathbb{B}$; for a null element it has a nonzero kernel and a proper image. The image of the parameter map is the cone of §*The Real Cone*; the image of the linear map is the whole algebra or a proper subspace, according to the rank of $\tilde Q$. The rank of $\Theta_{\tilde Q}$ is the square of the rank of $\tilde Q$: the image is $\tilde Q\mathbb{B}\tilde Q^{*}$, of complex dimension $\operatorname{rank}(\tilde Q)^{2}$.

### $SL_2(\mathbb{C})\to SO^{+}(1,3)$ on the Norm-One Slice

**The slice.** On the norm-one slice $\mathbb{B}_1^{\times}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=1\}$, the group is $SL_2(\mathbb{C})$, of real dimension six. The parameter map restricts to

$$
SL_2(\mathbb{C})\longrightarrow SO^{+}(1,3),\qquad
\tilde Q\longmapsto\Theta_{\tilde Q},
$$

a twofold cover. The kernel is $\{\pm e_t\}$; the image is the identity component of the Lorentz group; both groups have real dimension six. The kernel and the image are stated per slice: on $\mathbb{B}^{\times}$ the kernel is $\mathrm{U}(1)$ and the image is $CO^{+}(1,3)$; on $\mathbb{B}_1^{\times}$ the kernel is $\{\pm e_t\}$ and the image is $SO^{+}(1,3)$.

**The Lorentz action.** The anti-Hermitian half is a real four-dimensional space with the Minkowski form of signature $(3,1)$. A unit-norm sandwich preserves the form, because the norm scales by $|\langle\tilde Q\rangle_{\natural}|^{2}=1$. The map is continuous, $SL_2(\mathbb{C})$ is connected, and the kernel is $\{\pm e_t\}$; hence the image is the identity component $SO^{+}(1,3)$. The Hermitian half carries the same action composed with the exchange by $i$, with the opposite sign of the form. The matrix verification is in the two model articles cited in §*The Spectrum*.

**The conformal extension.** For a general unit $\tilde Q=r\zeta\tilde U$, the sandwich is $r^{2}\Theta_{\tilde U}$: a Lorentz transformation composed with the dilation of ratio $r^{2}$ on the algebra, $r^{4}$ on the norm and $r^{8}$ on the $4\times4$ determinant. The image is the conformal group $CO^{+}(1,3)$; the kernel remains the central $\mathrm{U}(1)$, and the scale is the positive real factor. The unit-norm slice is the subgroup on which the dilation is one; the general unit group adds the dilation and the phase, and the phase is the kernel.

## Summary

The Hermitian sandwich is $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$, the member $T_{\tilde Q,\tilde Q^{*}}$ of the two-sided family. It is a real cone of real dimension seven, the graph of the involution inside the complex two-sided cone; the phase of the parameter cancels, and complex rescaling acts by the square of the modulus. It is multiplicative up to the order of the factors, $\Theta_{\tilde Q}\Theta_{\tilde P}=\Theta_{\tilde Q\tilde P}$, and its defect from an algebra automorphism is $e_t-\tilde Q^{*}\tilde Q$; the defect vanishes exactly on the central multiples of real unit quaternions. It preserves the Hermitian and anti-Hermitian halves for every parameter, and the finer subspace structure exactly on that same set. It scales the norm by $|\langle\tilde Q\rangle_{\natural}|^{2}$, preserves the null cone and the sign of the norm, and sees only the modulus of the norm. The parameter is defined modulo the central $\mathrm{U}(1)$, which gives the real dimension seven. The sandwich meets each one-sided family in the closed ray of nonnegative multiples of the identity. Its spectrum is the four products $\lambda_i\bar\lambda_j$ of the eigenvalues of the $2\times2$ model with their conjugates; the trace is $4|Q_t|^{2}$ and the determinant is $|\langle\tilde Q\rangle_{\natural}|^{4}$. On the unit group the parameter map has kernel $\mathrm{U}(1)$ and image $CO^{+}(1,3)$; on the norm-one slice it is the twofold cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$ with kernel $\{\pm e_t\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the Hermitian sandwich |
| $T_{\tilde Q,\tilde P}$ | the two-sided operator; $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | the Hermitian and anti-Hermitian halves, real dimension four each |
| $\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm; $\langle\Theta_{\tilde Q}(\tilde X)\rangle_{\natural}=|\langle\tilde Q\rangle_{\natural}|^{2}\langle\tilde X\rangle_{\natural}$ |
| $\mathrm{U}(1)$ | the central phase $\{\omega e_t:|\omega|=1\}$ |
| $\operatorname{End}_{LR\ast}(\mathbb{B})$ | the real cone of sandwiches, real dimension seven |
| $L(\mathbb{B}),R(\mathbb{B})$ | the left and right regular families |
| $\lambda_1,\lambda_2$ | the eigenvalues of the $2\times2$ model $\mathsf M_2(\tilde Q)$ |
| $CO^{+}(1,3)$ | the conformal proper orthochronous Lorentz group |
| $SO^{+}(1,3)$ | the proper orthochronous Lorentz group |
| $SL_2(\mathbb{C})$ | the norm-one slice $\mathbb{B}_1^{\times}$ |

## Further Reading

- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the two-sided family, the scaling orbit and the composition.
- [$M_2(\mathbb{C})$ Model : The Sandwich](the-sandwich-in-the-m2c-model.html), for the matrix verification in the $2\times2$ model.
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Sandwich](the-sandwich-in-the-m4c-l-model.html), for the matrix verification in the regular model.
- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the adjoints of the sandwich.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the criterion on the parameter and the action on the six subspaces.
- [Conventions of the Operator Families](conventions-of-the-operator-families.html), for the names of the families and the sets.
