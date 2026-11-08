# __The Transposition of the Two Sides__

## Introduction

**The two identities.** Both are exact for every element of the algebra, and neither chooses a frame:

$$
\natural\,L_{\tilde Q}\,\natural=R_{\tilde Q^{\natural}},
\qquad\qquad
\natural\,L_{\tilde Q^{\natural}}\,\natural=R_{\tilde Q}.
$$

The first is what conjugation by $\natural$ does to a left multiplication: it turns it into a right multiplication and carries the parameter into its image. The second is the first with the element renamed from $\tilde Q$ to $\natural(\tilde Q)$; it is the same theorem, not a convention. The second reads better as a statement about the right family, and it is the one this article is named after.

**The equation that is false.** It is **not** true that $R_{\tilde Q}=\natural L_{\tilde Q}\natural$ with the same element on both sides. That equation holds exactly when $\tilde Q$ is central, and it fails on every parameter with a nonzero vector part. The proof is one line, and it is the reason this article exists: the two sides agree on $e_t$ only if $\tilde Q=\tilde Q^{\natural}$.

**Why the confusion is easy.** Three different operations act on the two one-sided families, and two of them swap the sides. They are the crossing of the comma, the conjugation by $\natural$, and the composite of the two:

| the operation | $L_{\tilde Q}$ becomes | $R_{\tilde Q}$ becomes | the side | the parameter |
|---|---|---|---|---|
| cross the comma, the **transpose** | $R_{\tilde Q}$ | $L_{\tilde Q}$ | exchanged | **kept** |
| conjugate by $\natural$ | $R_{\tilde Q^{\natural}}$ | $L_{\tilde Q^{\natural}}$ | exchanged | **carried through $\natural$** |
| the two composed | $L_{\tilde Q^{\natural}}$ | $R_{\tilde Q^{\natural}}$ | kept | carried through $\natural$ |

So an exchanged side is either free of conjugation or paid for by the conjugation of the parameter, and there is no third possibility. The first row is exact for every element, $R_{\tilde Q}=L_{\tilde Q}^{\mathsf T}$. The fourth display of line two is the first row written with the notation of the second: it keeps the transpose's parameter and applies the conjugation's map, and it is exact only on the centre. Writing the parameter of the conjugation repairs it, $R_{\tilde Q}=\natural L_{\tilde Q^{\natural}}\natural$.

**The mechanism, in one sentence.** An anti-automorphism reverses the order of every product, so a left multiplication by $\tilde Q$ becomes a right multiplication in which $\tilde Q$ has moved to the right and the map has been applied to it.

**Scope.** The two families and their laws are *Operators Acting on One Side*; their products, *Operators Acting on Two Sides*; the conjugation belongs to *The Group of Involutions*; the transpose of the plain form is the associate of *Adjoint Pair of $L$ and $R$ Operators*. No step below uses a topology, a distance or a limit, and no step chooses a basis.

## The Two Families

**Definition.** For $\tilde Q\in\mathbb{B}$ the **left** and **right multiplications** are the operators

$$
L_{\tilde Q}(X)=\tilde Q X,
\qquad
R_{\tilde Q}(X)=X\tilde Q .
$$

**Proposition (the three laws).** For all elements,

$$
L_{\tilde Q_1}L_{\tilde Q_2}=L_{\tilde Q_1\tilde Q_2},
\qquad
R_{\tilde Q_1}R_{\tilde Q_2}=R_{\tilde Q_2\tilde Q_1},
\qquad
L_{\tilde Q_1}R_{\tilde Q_2}=R_{\tilde Q_2}L_{\tilde Q_1}.
$$

*Proof.* On an arbitrary $X$, by associativity and nothing else:

$$
L_{\tilde Q_1}\bigl(L_{\tilde Q_2}(X)\bigr)=\tilde Q_1(\tilde Q_2X)=(\tilde Q_1\tilde Q_2)X,
$$
$$
R_{\tilde Q_1}\bigl(R_{\tilde Q_2}(X)\bigr)=(X\tilde Q_2)\tilde Q_1=X(\tilde Q_2\tilde Q_1),
$$
$$
L_{\tilde Q_1}\bigl(R_{\tilde Q_2}(X)\bigr)=\tilde Q_1X\tilde Q_2=R_{\tilde Q_2}\bigl(L_{\tilde Q_1}(X)\bigr).
$$

The second law is the reason the right family is called an anti-representation: the order of the parameters is reversed. The third says the two families commute element by element.

**Proposition (the unit reads the parameter).** $L_{\tilde Q}(e_t)=\tilde Q=R_{\tilde Q}(e_t)$.

*Proof.* $e_t$ is the unit. Consequently $L_{\tilde Q}=L_{\tilde P}$ if and only if $\tilde Q=\tilde P$, and the same for $R$: evaluate the equality at $e_t$. This is used repeatedly below, and it is the only tool needed to turn an operator identity into an identity between elements.

**Proposition (when a left multiplication is a right one).** $L_{\tilde Q}=R_{\tilde P}$ if and only if $\tilde P=\tilde Q$ and $\tilde Q$ is central.

*Proof.* At $e_t$ both sides give $\tilde Q$ and $\tilde P$, so $\tilde P=\tilde Q$, and the question is when $R_{\tilde Q}=L_{\tilde Q}$, that is when $\tilde QX=X\tilde Q$ for every $X$. Write $\tilde Q=Q_te_t+\vec Q$ with $\vec Q$ in the vector subspace $V$. A central element has $\tilde QX=X\tilde Q$ for every $X$; conversely, taking $X$ in $V$ and using the identity

$$
\vec Q\,u+u\,\vec Q=2\,\mathrm{Sc}(\vec Qu)\,e_t\qquad(u\in V),
$$

which holds on the units by $\vec e_k^2=-e_t$ and $\vec e_j\vec e_k=-\vec e_k\vec e_j$ and extends by bilinearity, the condition $\vec Qu=u\vec Q$ gives $\vec Qu=\mathrm{Sc}(\vec Qu)e_t$. The right side is central, so the left side has no vector part; but $\vec Q\vec e_x=-Q_xe_t+Q_y\vec e_z-Q_z\vec e_y$, so $Q_y=Q_z=0$; and then $\vec Q\vec e_y=Q_x\vec e_z$ forces $Q_x=0$. Hence $\vec Q=0$ and $\tilde Q$ is central. The centre is $\mathbb{C}e_t$, so the common operator is $\lambda\,\mathrm{id}$.

## The Conjugation and the Two Grades

**Definition.** The **quaternion conjugation** is

$$
\natural(\tilde Q)=\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z .
$$

It is the identity on the centre and minus the identity on $V$; on the real quaternions it is the classical conjugation, extended to $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ by complex linearity.

**Proposition (the three properties).**

1. $\natural$ is $\mathbb{C}$-linear.
2. $\natural$ is an involution: $\natural^2=\mathrm{id}$, so $\natural$ is a bijection and $\natural^{-1}=\natural$.
3. $\natural$ is **anti**multiplicative: $\natural(XY)=\natural(Y)\natural(X)$ for all $X,Y$.

*Proof.* The first is immediate from the definition. The second: negating the vector part twice restores it. The third on the units: if $e_\mu e_\nu=\epsilon e_\kappa$ with $\epsilon=\pm1$ and $\kappa$ the third index, then $\natural(e_\mu e_\nu)=\epsilon\,\varepsilon_\kappa e_\kappa$, while $\natural(e_\nu)\natural(e_\mu)=\varepsilon_\nu\varepsilon_\mu\,e_\nu e_\mu=\varepsilon_\mu\varepsilon_\nu\,\epsilon e_\kappa$, and the two agree because the product rule of the units gives $\varepsilon_\mu\varepsilon_\nu=\varepsilon_\kappa$. Both sides are bilinear, so the identity extends to all pairs.

The third property is the whole article. It says that $\natural$ is not an automorphism: it does not respect the order, it reverses it.

**The two grades.** The identity of the next section needs only reversal and bijectivity, so it holds for two kinds of map, and the corpus uses both:

| the map | linearity | grade | exchanges the two families? |
|---|---|---|---|
| $\natural$ | $\mathbb{C}$-linear | anti-automorphism | yes |
| $\ast=\natural\circ\bar{\cdot}$ | conjugate linear | anti-automorphism | yes |
| $\bar{\cdot}$ | conjugate linear | automorphism | no |

The last row is the standing trap. The coefficient conjugation is conjugate linear and involutive like $\ast$, but it preserves the order of products, so it keeps each family in place and only carries the parameter. A map that keeps the sides is not a transposition of them.

## The Theorem

**Theorem (conjugation by an anti-automorphism).** Let $\tau$ be a bijection of $\mathbb{B}$ with

$$
\tau(XY)=\tau(Y)\,\tau(X)\qquad\text{for all }X,Y\in\mathbb{B}.
$$

Then for every $\tilde Q\in\mathbb{B}$,

$$
\tau\,L_{\tilde Q}\,\tau^{-1}=R_{\tau(\tilde Q)},
\qquad\qquad
\tau\,R_{\tilde Q}\,\tau^{-1}=L_{\tau(\tilde Q)} .
$$

*Proof.* Let $X$ be any element and compute. Each line below is one substitution.

$$
\bigl(\tau L_{\tilde Q}\tau^{-1}\bigr)(X)
=\tau\Bigl(L_{\tilde Q}\bigl(\tau^{-1}(X)\bigr)\Bigr)
=\tau\Bigl(\tilde Q\cdot\tau^{-1}(X)\Bigr).
$$

The argument of the outer $\tau$ is a product of two elements, namely $\tilde Q$ and $\tau^{-1}(X)$. Apply the reversal property to that product:

$$
\tau\Bigl(\tilde Q\cdot\tau^{-1}(X)\Bigr)
=\tau\bigl(\tau^{-1}(X)\bigr)\cdot\tau(\tilde Q)
=X\cdot\tau(\tilde Q)
=R_{\tau(\tilde Q)}(X).
$$

The third equality is $\tau\circ\tau^{-1}=\mathrm{id}$. The same computation with the factors in the other order gives the second identity:

$$
\bigl(\tau R_{\tilde Q}\tau^{-1}\bigr)(X)
=\tau\Bigl(\tau^{-1}(X)\cdot\tilde Q\Bigr)
=\tau(\tilde Q)\cdot X
=L_{\tau(\tilde Q)}(X).
$$

Since $X$ was arbitrary, the operators agree on $\mathbb{B}$.

**What the middle step does, and why nothing else can.** At the moment the reversal is applied, two things happen at once, and they must be kept apart.

- The factor $\tau^{-1}(X)$ is carried and returns as $X$, because $\tau$ and $\tau^{-1}$ cancel.
- The factor $\tilde Q$ is carried and becomes $\tau(\tilde Q)$.

The parameter therefore lands **on the right of $X$** and it lands there **as its image**. The first is what makes the result a right multiplication; the second is the transport that the false equation drops.

**The contrast with an automorphism.** Let $\sigma$ preserve products, $\sigma(XY)=\sigma(X)\sigma(Y)$. Then

$$
\bigl(\sigma L_{\tilde Q}\sigma^{-1}\bigr)(X)
=\sigma\Bigl(\tilde Q\cdot\sigma^{-1}(X)\Bigr)
=\sigma(\tilde Q)\cdot\sigma\bigl(\sigma^{-1}(X)\bigr)
=\sigma(\tilde Q)\,X
=L_{\sigma(\tilde Q)}(X),
$$

so the side is kept and only the parameter moves. Comparing the two computations, the exchange of the sides is **exactly** the reversal of the order of the two factors, and nothing else. That is the mechanism in its shortest form.

**Corollary (products of two operators).** For any $\tau$ as in the theorem,

$$
\tau\bigl(L_{\tilde Q_1}R_{\tilde Q_2}\bigr)\tau^{-1}
=R_{\tau(\tilde Q_1)}L_{\tau(\tilde Q_2)}
=L_{\tau(\tilde Q_2)}R_{\tau(\tilde Q_1)} .
$$

The sides are exchanged, the parameters are carried, and the two factors change places in the product.

**Proposition (the reversal is forced).** Let $\Theta$ be a bijection of $\mathbb{B}$ with $\Theta L_{\tilde Q}\Theta^{-1}=R_{\Theta(\tilde Q)}$ for every $\tilde Q$. Then $\Theta$ is antimultiplicative.

*Proof.* Let $X=\Theta(Y)$, so that $Y=\Theta^{-1}(X)$. The hypothesis, evaluated at $X$, reads

$$
\Theta\bigl(\tilde Q\,Y\bigr)=\bigl(\Theta L_{\tilde Q}\Theta^{-1}\bigr)(X)=R_{\Theta(\tilde Q)}(X)=X\,\Theta(\tilde Q)=\Theta(Y)\,\Theta(\tilde Q).
$$

So a bijection that exchanges the two families **must** reverse products. There is no map that exchanges the families and keeps the order, and therefore none that exchanges them without carrying the parameter. This is the structural reason the next section's equation cannot hold in general: it would ask one map to do both.

## The Two Readings at $\tau=\natural$

Take $\tau=\natural$ in the theorem, and use $\natural^{-1}=\natural$. The conclusion is

$$
\natural\,L_{\tilde Q}\,\natural=R_{\natural(\tilde Q)}=R_{\tilde Q^{\natural}} .
$$

**The second reading.** Put $\natural(\tilde Q)$ in place of $\tilde Q$ in the conjugation identity:

$$
\natural\,L_{\natural(\tilde Q)}\,\natural=R_{\natural(\natural(\tilde Q))}=R_{\tilde Q},
$$

because $\natural^2=\mathrm{id}$. Written with the mark on the element, and with $L_{\natural(\tilde Q)}=L_{\tilde Q^{\natural}}$,

$$
\natural\,L_{\tilde Q^{\natural}}\,\natural=R_{\tilde Q}.
$$

The conjugation identity and the renamed identity are one theorem read at two elements. Neither is a shorthand, and neither restricts $\tilde Q$.

**The same two identities, term by term on an element.** For the conjugation identity, let $X$ be arbitrary:

$$
\bigl(\natural L_{\tilde Q}\natural\bigr)(X)
=\natural\Bigl(\tilde Q\cdot\natural(X)\Bigr)
=\natural\bigl(\natural(X)\bigr)\cdot\natural(\tilde Q)
=X\cdot\tilde Q^{\natural}.
$$

The second equality is the reversal applied to the product of $\tilde Q$ and $\natural(X)$; the third is $\natural^2=\mathrm{id}$. The result is $R_{\tilde Q^{\natural}}(X)$ for every $X$, which is the conjugation identity.

For the renamed identity, the same computation with $\tilde Q^{\natural}$ in place of $\tilde Q$:

$$
\bigl(\natural L_{\tilde Q^{\natural}}\natural\bigr)(X)
=\natural\Bigl(\tilde Q^{\natural}\cdot\natural(X)\Bigr)
=\natural\bigl(\natural(X)\bigr)\cdot\natural(\tilde Q^{\natural})
=X\cdot\tilde Q,
$$

using $\natural(\tilde Q^{\natural})=\tilde Q$. The result is $R_{\tilde Q}(X)$ for every $X$, which is the renamed identity.

**Remark (one map, two names).** The renamed identity is what the title names: the transposition of the two sides. It says that the right multiplication by $\tilde Q$ is the left multiplication by $\tilde Q^{\natural}$, read through the conjugation. On parameters, the map it implements is $\tilde Q\mapsto\tilde Q^{\natural}$; on operators, it is $F\mapsto\natural F\natural$.

**Corollary (the conjugation is an involution of the two families).** $\natural\bigl(\natural F\natural\bigr)\natural=F$ for every operator $F$, since $\natural^2=\mathrm{id}$. So the map $F\mapsto\natural F\natural$ is an involution of the whole operator algebra, and it exchanges the two families by the two identities above.

## The Equation That Is False

**Proposition.** $R_{\tilde Q}=\natural L_{\tilde Q}\natural$ if and only if $\tilde Q$ is central.

*Proof.* Suppose the operators are equal and evaluate both at $e_t$. On the right, $R_{\tilde Q}(e_t)=e_t\tilde Q=\tilde Q$. On the left,

$$
\bigl(\natural L_{\tilde Q}\natural\bigr)(e_t)
=\natural\Bigl(\tilde Q\cdot\natural(e_t)\Bigr)
=\natural(\tilde Q\cdot e_t)
=\tilde Q^{\natural},
$$

because $\natural(e_t)=e_t$ and $e_t$ is the unit. Hence $\tilde Q=\tilde Q^{\natural}$, that is $Q_t e_t+\vec Q=Q_te_t-\vec Q$, that is $\vec Q=0$: the element is central. Conversely, if $\tilde Q$ is central then $\tilde Q^{\natural}=\tilde Q$, and the conjugation identity gives $\natural L_{\tilde Q}\natural=R_{\tilde Q^{\natural}}=R_{\tilde Q}$.

**The size of the failure.** For a general element the two operators differ by the vector part. On $e_t$ the right multiplication gives $\tilde Q$ and the conjugated left multiplication gives $\tilde Q^{\natural}$, so the gap is

$$
\tilde Q-\tilde Q^{\natural}=2\vec Q .
$$

For $\tilde Q=e_t+2\vec e_x$ the gap is $4\vec e_x$, and the two operators differ on the unit alone, before any other input is tried.

**Proposition (the exact solution in the parameter).** For a fixed $\tilde Q$ and a variable $\tilde P$,

$$
\natural\,L_{\tilde P}\,\natural=R_{\tilde Q}
\qquad\text{if and only if}\qquad
\tilde P=\tilde Q^{\natural}.
$$

*Proof.* By the conjugation identity the left side is $R_{\tilde P^{\natural}}$, and $R_{\tilde P^{\natural}}=R_{\tilde Q}$ if and only if $\tilde P^{\natural}=\tilde Q$, by the unit. Applying $\natural$ gives $\tilde P=\tilde Q^{\natural}$.

So the parameter of the left multiplication is unique, and it is $\tilde Q^{\natural}$. The equation with $\tilde Q$ itself is the special case in which $\natural$ fixes $\tilde Q$.

**Why the error has a shape.** The false equation is not a slip of the pen; it is the natural confusion of two operations that both move a left multiplication to the right family. The transpose moves it and leaves the parameter alone (next section). The conjugation moves it and carries the parameter. A reader who has only one notation for "move to the other side" writes the transpose's parameter with the conjugation's map. The repair is to name the operation: the transpose is $\mathsf C$ and the conjugation is $\natural(\ )\natural$, and they are different maps of the operator algebra.

## The Crossing of the Comma

**The plain form.** Define

$$
\langle X,Y\rangle=\mathrm{Sc}(XY),
$$

the scalar part of the product. It is symmetric, because $\mathrm{Sc}(XY)=\mathrm{Sc}(YX)$, and it is non-degenerate, because the four diagonal forms $\sum_\mu\varepsilon_\mu X_\mu Y_\mu$ with $\varepsilon=(1,-1,-1,-1)$ separate the units. The form is the plain bilinear form of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

**Definition (the transpose).** For a $\mathbb{C}$-linear $F$ of $\mathbb{B}$, the **transpose** $F^{\mathsf T}$ is the unique operator with

$$
\langle F(X),Y\rangle=\bigl\langle X,F^{\mathsf T}(Y)\bigr\rangle\qquad\text{for all }X,Y .
$$

It exists and is unique because the form is non-degenerate and symmetric, and it depends on no frame: the definition names only the form.

**Proposition (the transpose exchanges the two families and keeps the parameter).**

$$
L_{\tilde Q}^{\mathsf T}=R_{\tilde Q},
\qquad\qquad
R_{\tilde Q}^{\mathsf T}=L_{\tilde Q}.
$$

*Proof.* By the definition, $\langle L_{\tilde Q}(X),Y\rangle=\mathrm{Sc}(\tilde QXY)$. The scalar part is invariant under the cyclic permutation of its factors, so

$$
\mathrm{Sc}(\tilde QXY)=\mathrm{Sc}(XY\tilde Q)=\bigl\langle X,R_{\tilde Q}(Y)\bigr\rangle,
$$

which is the defining property of $R_{\tilde Q}$, and the transpose is unique. The second identity is the same computation with $\tilde Q$ moved the other way.

This is the operator-level content of the sentence "a right multiplication is a transposed left multiplication", and it costs no conjugation whatever: the parameter of $L_{\tilde Q}^{\mathsf T}$ is $\tilde Q$, unchanged. The proof uses only the cyclicity of the scalar part, which is associativity read once.

**Proposition (the transpose against the conjugation).** For every $\tilde Q$,

$$
L_{\tilde Q}^{\mathsf T}=R_{\tilde Q}=\natural\,L_{\tilde Q^{\natural}}\,\natural .
$$

*Proof.* The first equality is the proposition above; the second is the renamed identity.

The display is the shortest statement of the article: the transpose of a left multiplication is the conjugation of the left multiplication of the transposed parameter. Its two halves fail differently. The transpose is always right and conjugates nothing. The conjugation is always right and conjugates the parameter; written with the untransposed parameter, $\natural L_{\tilde Q}\natural$, it is wrong by $2\vec Q$.

## The Three Maps

The two propositions above define three maps of the union of the two families into itself. Each is worth naming, because the confusion of two of them is the error.

| map | definition | $L_{\tilde Q}\mapsto$ | $R_{\tilde Q}\mapsto$ |
|---|---|---|---|
| $\mathsf S$, the **transpose** | $F\mapsto F^{\mathsf T}$ | $R_{\tilde Q}$ | $L_{\tilde Q}$ |
| $\mathsf K$, the **conjugation** | $F\mapsto\natural F\natural$ | $R_{\tilde Q^{\natural}}$ | $L_{\tilde Q^{\natural}}$ |
| $\mathsf C$, the **carry** | $F\mapsto\mathsf S\mathsf K(F)=\mathsf K\mathsf S(F)$ | $L_{\tilde Q^{\natural}}$ | $R_{\tilde Q^{\natural}}$ |

**Proposition (the three are involutions and the outer two commute).**

$$
\mathsf S^2=\mathsf K^2=\mathsf C^2=\mathrm{id},
\qquad
\mathsf S\mathsf K=\mathsf K\mathsf S .
$$

*Proof.* $\mathsf S^2=\mathrm{id}$ is the uniqueness of the transpose applied twice. $\mathsf K^2=\mathrm{id}$ because $\natural F\natural$ conjugated again returns $F$, each factor $\natural^2$ being the identity. The commutation: on $L_{\tilde Q}$, $\mathsf S\mathsf K(L_{\tilde Q})=\mathsf S(R_{\tilde Q^{\natural}})=L_{\tilde Q^{\natural}}$ and $\mathsf K\mathsf S(L_{\tilde Q})=\mathsf K(R_{\tilde Q})=L_{\tilde Q^{\natural}}$, and the same on $R_{\tilde Q}$; so the two agree. Then $\mathsf C=\mathsf S\mathsf K$ is an involution as a composite of two commuting involutions.

**The two mechanisms, kept apart.** $\mathsf S$ is the crossing of the comma: the parameter crosses from one side of the input to the other and is not touched. $\mathsf K$ is the conjugation: the parameter is put through $\natural$ and the operator changes families. $\mathsf C$ carries the parameter and leaves the side alone, which is why it can be mistaken for a transpose, and is not one.

**Corollary (the fixed locus is the centre).** Each of the three maps fixes exactly the multiplications by the centre, $\{L_{\lambda e_t}\}=\{R_{\lambda e_t}\}$. For $\mathsf S$ this is the proposition that $L_{\tilde Q}=R_{\tilde Q}$ only for a central $\tilde Q$; for $\mathsf K$ it is $\tilde Q^{\natural}=\tilde Q$; for $\mathsf C$ it is the same equation, since $\mathsf C(L_{\tilde Q})=L_{\tilde Q^{\natural}}$. These are exactly the parameters on which the false equation $R_{\tilde Q}=\natural L_{\tilde Q}\natural$ holds.

## Consequences

**The right family is an anti-representation, and the reason.** The map $\mathsf K$ is multiplicative on operators, because $\natural^2=\mathrm{id}$:

$$
\mathsf K(F)\mathsf K(G)=\natural F\natural\natural G\natural=\natural FG\natural=\mathsf K(FG).
$$

Since $\mathsf K(L_{\tilde Q^{\natural}})=R_{\tilde Q}$ by the renamed identity, the law of the right family follows from the law of the left one and from the reversal:

$$
R_{\tilde Q}R_{\tilde P}
=\mathsf K\bigl(L_{\tilde Q^{\natural}}\bigr)\mathsf K\bigl(L_{\tilde P^{\natural}}\bigr)
=\mathsf K\bigl(L_{\tilde Q^{\natural}\tilde P^{\natural}}\bigr)
=\mathsf K\bigl(L_{(\tilde P\tilde Q)^{\natural}}\bigr)
=R_{\tilde P\tilde Q},
$$

where the third equality uses $\tilde Q^{\natural}\tilde P^{\natural}=(\tilde P\tilde Q)^{\natural}$, which is the reversal property of $\natural$ read on the two parameters. So the anti-representation of the right family and the antimultiplicativity of $\natural$ are one fact seen twice.

**Every two-sided operator is two left multiplications.** By the renamed identity with $\tilde Q$ replaced by $\tilde P$,

$$
L_{\tilde Q}R_{\tilde P}=L_{\tilde Q}\,\natural\,L_{\tilde P^{\natural}}\,\natural .
$$

So the right factor of a two-sided operator can be written as a left multiplication, at the price of one conjugation of its parameter and two conjugations of the operator. The right family is therefore generated by the left family together with $\natural$, and nothing else is needed.

**The four statements that look alike.** On the two families the following four displays are easy to confuse, and three of them are true:

$$
\underbrace{R_{\tilde Q}=L_{\tilde Q}^{\mathsf T}}_{\text{the transpose}},
\qquad
\underbrace{R_{\tilde Q}=\natural L_{\tilde Q^{\natural}}\natural}_{\text{the renamed identity}},
\qquad
\underbrace{R_{\tilde Q^{\natural}}=\natural L_{\tilde Q}\natural}_{\text{the conjugation identity}},
\qquad
\underbrace{R_{\tilde Q}=\natural L_{\tilde Q}\natural}_{\text{false off the centre}} .
$$

The first is the transpose: the side is exchanged and the parameter is untouched. The second and the third are one theorem read at the parameter and at its image; they exchange the side and carry the parameter. The fourth is the first with the second's notation: it keeps the transpose's parameter and applies the conjugation's map, and it is exact only where $\natural$ fixes the parameter, that is on the centre.

**The other two conjugations.** The theorem holds for $\ast$ as well, because $\ast$ is antimultiplicative:

$$
\ast\,L_{\tilde Q}\,\ast=R_{\tilde Q^{\ast}},
\qquad\qquad
\ast\,L_{\tilde Q^{\ast}}\,\ast=R_{\tilde Q},
$$

the second by $\ast^2=\mathrm{id}$. The coefficient conjugation behaves differently, as the table of §*The Conjugation and the Two Grades* predicts, since it preserves products:

$$
\bar{\cdot}\;L_{\tilde Q}\;\bar{\cdot}=L_{\bar{\tilde Q}},
\qquad\qquad
\bar{\cdot}\;R_{\tilde Q}\;\bar{\cdot}=R_{\bar{\tilde Q}},
$$

which keeps each family in place and carries the parameter. The three maps $\natural$, $\ast$ and $\bar{\cdot}$ therefore produce three different combinations of the two elementary moves, exchange of the side and action on the parameter, and the table of the three maps records the first of them.

## Summary

Two identities hold for every element and choose no frame: $\natural L_{\tilde Q}\natural=R_{\tilde Q^{\natural}}$ and $\natural L_{\tilde Q^{\natural}}\natural=R_{\tilde Q}$. Both are instances of one theorem, that conjugation by an anti-automorphism sends a left multiplication to a right multiplication of the carried parameter, $\tau L_{\tilde Q}\tau^{-1}=R_{\tau(\tilde Q)}$, which is proved by applying the reversal of the product to $\tilde Q\cdot\tau^{-1}(X)$: the factor $\tau^{-1}(X)$ returns as $X$, the factor $\tilde Q$ becomes $\tau(\tilde Q)$, and the parameter therefore lands on the right as its image.

The equation $R_{\tilde Q}=\natural L_{\tilde Q}\natural$, with the same element on both sides, is false off the centre, and it fails already on the unit: the right side sends $e_t$ to $\tilde Q^{\natural}$, the left side to $\tilde Q$, and the gap is $2\vec Q$. It holds exactly on the centre, which is the fixed locus of the conjugation. The confusion it represents is the confusion of two operations that both exchange the sides: the transpose, $\langle F(X),Y\rangle=\langle X,F^{\mathsf T}(Y)\rangle$, which exchanges them and leaves the parameter alone, $L_{\tilde Q}^{\mathsf T}=R_{\tilde Q}$ by the cyclicity of the scalar part; and the conjugation, which exchanges them and carries the parameter. The shortest correct statement joins the two,

$$
L_{\tilde Q}^{\mathsf T}=R_{\tilde Q}=\natural\,L_{\tilde Q^{\natural}}\,\natural,
$$

and the map $F\mapsto\mathsf S\mathsf K(F)$ which composes them keeps the side and carries the parameter, which is why it can be mistaken for a transpose.

Three maps act on the two families, each an involution, the outer two commuting: the transpose, the conjugation, and the carry. Their common fixed set is the centre, and the anti-representation of the right family, the generation of every two-sided operator by the left family and $\natural$, and the two conjugate-linear cases $\ast$ and $\bar{\cdot}$ all follow from the one theorem. No step uses a topology, a distance, a limit or a basis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}(X)=\tilde QX$, $R_{\tilde Q}(X)=X\tilde Q$ | the left and the right multiplication |
| $L_{\tilde Q_1}L_{\tilde Q_2}=L_{\tilde Q_1\tilde Q_2}$, $R_{\tilde Q_1}R_{\tilde Q_2}=R_{\tilde Q_2\tilde Q_1}$, $L_{\tilde Q_1}R_{\tilde Q_2}=R_{\tilde Q_2}L_{\tilde Q_1}$ | the three laws, from associativity alone |
| $L_{\tilde Q}(e_t)=\tilde Q=R_{\tilde Q}(e_t)$ | the unit reads the parameter, and separates two operators |
| $\natural(\tilde Q)=\tilde Q^{\natural}=Q_te_t-\vec Q$ | the quaternion conjugation: $\mathbb{C}$-linear, involutive, antimultiplicative |
| $\natural L_{\tilde Q}\natural=R_{\tilde Q^{\natural}}$ | what the conjugation does to a left multiplication |
| $\natural L_{\tilde Q^{\natural}}\natural=R_{\tilde Q}$ | the same theorem with the parameter renamed: the transposition of the two sides |
| $\tau L_{\tilde Q}\tau^{-1}=R_{\tau(\tilde Q)}$, $\tau R_{\tilde Q}\tau^{-1}=L_{\tau(\tilde Q)}$ | the theorem for any anti-automorphism |
| $R_{\tilde Q}=\natural L_{\tilde Q}\natural$ if and only if $\tilde Q$ central | the false equation, and its exact solution set |
| $\langle X,Y\rangle=\mathrm{Sc}(XY)$, $\langle F(X),Y\rangle=\langle X,F^{\mathsf T}Y\rangle$ | the plain form and the transpose it defines |
| $L_{\tilde Q}^{\mathsf T}=R_{\tilde Q}$, $R_{\tilde Q}^{\mathsf T}=L_{\tilde Q}$ | the transpose exchanges the families and keeps the parameter |
| $\mathsf S$, $\mathsf K$, $\mathsf C=\mathsf S\mathsf K$ | the transpose, the conjugation, the carry; three involutions, the outer two commuting |
| $L_{\tilde Q}R_{\tilde P}=L_{\tilde Q}\natural L_{\tilde P^{\natural}}\natural$ | every two-sided operator as two left multiplications |
| $\ast=\natural\bar{\cdot}$ | the Hermitian conjugation, antimultiplicative and conjugate linear, with $\ast L_{\tilde Q}\ast=R_{\tilde Q^{\ast}}$ |

## Further Reading

- [Operators Acting on One Side](operators-acting-on-one-side.html), for the two families, their laws, their images and their commutants
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the products $L_{\tilde Q}R_{\tilde P}$, their adjoint and their isometries
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the Conway basis and the generation of the endomorphism algebra by the two families
- [The Group of Involutions](the-group-of-involutions.html), for $\natural$, $\ast$ and $\bar{\cdot}$, their linearity and their grades
- [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html), for the associate $(L_{\tilde Q})^{\approx}=R_{\tilde Q}$ read as the transpose of the plain form, and for the other three adjoints
- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html), for the swap of the two slots, for the grading and for the difference between that swap and the conjugation of this article
- [The Hermitian Pair of Operators Acting on One Side](the-hermitian-pair-of-operators-acting-on-one-side.html), for the same theorem with $\ast$ in place of $\natural$ and for the pair whose adjoints stay on one side
- [Bilinear Forms](bilinear-forms.html), §*Isometries*, for the transpose of a bilinear form, of which $\mathsf S$ is the biquaternion case
