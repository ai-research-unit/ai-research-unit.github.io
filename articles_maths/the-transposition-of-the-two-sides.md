# __The Transposition of the Two Sides__

## Introduction

**The fact.** A right multiplication is a transposed left multiplication, at the price of one relabelling. In the axis-free frame the two halves of that sentence are

$$
\boxed{\;R_{\mathrm{axf}}(\tilde Q)=\mathsf D\,L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}\mathsf D\;},\qquad
L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L_{\mathrm{axf}}(\tilde Q^{\natural}),
$$

with $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$ the switch of the frame, the real sign matrix that also carries the left family onto the right one. The second identity says what a transpose does in this frame: it turns a left matrix into another left matrix, the one of the quaternion conjugate. The first says what must be added to reach the other side, namely one conjugation by the switch.

**Why the second identity is the interesting half.** Transposition alone never leaves the left. It gives another left multiplication, so $R_{\mathrm{axf}}(\tilde Q)=L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}$ holds only for central $\tilde Q$: the two arrays differ by a sign on the six entries with one vector index, and equality forces the three vector coefficients to vanish. The right side is reached only when the transposed array is read through the sign matrix of the frame, and that sign matrix is the object the corpus calls the switch. The transposition of the two sides is a transpose together with a change of reading, and neither half can be dropped.

**What the article proves.** The identity is not an accident of one basis. At the level of operators it reads

$$
R_{\tilde Q}=\natural\,L_{\tilde Q^{\natural}}\,\natural,
$$

which contains no matrix and no frame: the quaternion conjugation $\natural$ acts on the carrier, and the right multiplication is a left multiplication by the conjugate parameter, conjugated by that same $\natural$. The mechanism is one sign count, and the article states it in four steps: the two displays differ on six entries, the transpose turns all twelve off-diagonal entries, the switch turns six of them back, and the six that stay turned are the pairs of distinct vector units, which are the pairs that anticommute.

**Boundaries.** The two families and their laws are *Operators Acting on One Side*, their products *Operators Acting on Two Sides*, the ambient space *The Endomorphisms of the Biquaternion Algebra*. The entry-by-entry computation of the stitch in the axis-free frame is *$M_4(\mathbb{C})$ Axis-Free Representation : Operators*, §*The Stitch Between the Copies*; this article states the identity as a theorem about operators and says why it holds. The conjugations are *The Group of Involutions*, the forms *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. Everything below is written in the coefficient frame $e_t,\vec e_x,\vec e_y,\vec e_z$, and no step uses a topology.

## The Two Displays Differ on Six Entries

**The two arrays.** For $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$,

$$
L_{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix},\qquad
R_{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&Q_z&-Q_y\\
Q_y&-Q_z&Q_t&Q_x\\
Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}.
$$

**The comparison at one element.** At $\tilde Q=e_t+2\vec e_x+3\vec e_y+4\vec e_z$ the two arrays are

$$
L=
\begin{pmatrix}
1&-2&-3&-4\\
2&1&-4&3\\
3&4&1&-2\\
4&-3&2&1
\end{pmatrix},\qquad
R=
\begin{pmatrix}
1&-2&-3&-4\\
2&1&4&-3\\
3&-4&1&2\\
4&3&-2&1
\end{pmatrix}.
$$

They agree on the diagonal and in the first row and the first column, and they disagree on the six entries whose two indices are both vector: the pairs $(x,y)$, $(x,z)$ and $(y,z)$, each in its two orders.

**The rule, and its reason.** The entry $(\mu,\nu)$ of the left display is the $\mu$-th coordinate of $\tilde Qe_\nu$, and the entry $(\mu,\nu)$ of the right display is the $\mu$-th coordinate of $e_\nu\tilde Q$. The two agree when $\mu=\nu$, when $\nu=t$ and when $\mu=t$, and they are opposite in the remaining six places. The reason is the multiplication table. The row $t$ of the table is the identity, so the coordinate $t$ of a product is read without any reordering of the factors; the row $k$ carries the two remaining vector coordinates with opposite signs, so a coordinate $k$ changes sign exactly when the second factor is a vector unit other than $\vec e_k$. The six signs by which the displays differ are therefore the non-commutativity of the algebra and nothing else, and in a commutative algebra the two displays would coincide.

**What the six signs are not.** They are not a defect of the frame. A change of basis conjugates both arrays at once, so it preserves the fact that they differ, and it moves the difference around. The six entries that carry it are named by the multiplication table and not by the basis.

## The Transpose of a Left Matrix

**The observation.** The left display carries $Q_t$ on the diagonal and is skew off it: $L_{\mu\nu}=-L_{\nu\mu}$ whenever $\mu\ne\nu$. The transpose therefore has the diagonal of the display and the negative of the display everywhere else, which is one line:

$$
L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}=2Q_t\,\mathrm I_4-L_{\mathrm{axf}}(\tilde Q).
$$

**The dictionary.** The map $\tilde Q\mapsto 2Q_te_t-\tilde Q$ is the quaternion conjugation, which keeps the scalar coefficient and negates the three vector coefficients, and the assignment $\tilde Q\mapsto L_{\mathrm{axf}}(\tilde Q)$ is linear. Applying the conjugation to the display is the same as negating the three vector coefficients in it, which is the transpose:

$$
L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L_{\mathrm{axf}}(\tilde Q^{\natural}).
$$

The transpose of a left matrix is a left matrix. It is the left matrix of the quaternion conjugate, and it is not the right matrix: the right display agrees with the transpose on the diagonal and on the six entries with two vector indices, and differs from it by a sign on the six with one vector index.

**The reading.** Transposition exchanges the two indices of every entry. In this frame the two indices play symmetric roles in the scalar part and antisymmetric roles in the vector part, and the transpose reads exactly that antisymmetry. It is not a change of side but a change of element, and the element it produces is the quaternion conjugate.

**The same shape in the Peirce frame.** There the left matrix is the tensor product $\mathrm I_2\otimes\mathsf M_2(\tilde Q)$, so its transpose is $\mathrm I_2\otimes\mathsf M_2(\tilde Q)^{\mathsf T}$, a left matrix again. It is the left matrix of the element whose $2\times2$ image is $\mathsf M_2(\tilde Q)^{\mathsf T}$, and that element is the exchange $S\tilde Q$ of *Operators Acting on One Side*, §*The Flip of the Two Mixed Units*. In both frames the transpose of a left matrix is a left matrix; what differs from frame to frame is the element the transpose implements, $\natural$ in the axis-free frame and $S$ in the Peirce frame.

## The Switch Restores the Six Entries

**Theorem.** In the axis-free frame, for every $\tilde Q\in\mathbb{B}$,

$$
R_{\mathrm{axf}}(\tilde Q)=\mathsf D\,L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}\,\mathsf D,
\qquad
\mathsf D=\operatorname{diag}(1,-1,-1,-1).
$$

*Proof.* Write $s_t=1$ and $s_x=s_y=s_z=-1$, so that $\mathsf D=\operatorname{diag}(s_\mu)$ and $\tilde Q^{\natural}$ carries the coefficients $s_\mu Q_\mu$. The product $\mathsf D M\mathsf D$ multiplies the entry $(\mu,\nu)$ of a matrix $M$ by $s_\mu s_\nu$, which is $-1$ when exactly one of the two indices is $t$ and $+1$ otherwise.

By the preceding section the transpose negates the twelve off-diagonal entries of the display and keeps the four diagonal ones. Conjugating by $\mathsf D$ then negates the six entries that carry exactly one index $t$, which are the six entries of the first row and the first column off the diagonal, and keeps the diagonal and the six entries with two vector indices. The two steps give an array that agrees with the display on the diagonal and on the six entries with one scalar index, and is the negative of the display on the six with two vector indices. That is the right display, by the rule of §*The Two Displays Differ on Six Entries*.

**Why the switch stands on both sides.** The array $\mathsf D L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}$ alone is not a right matrix: its first row is $(Q_t,Q_x,Q_y,Q_z)$ where the right display has $(Q_t,-Q_x,-Q_y,-Q_z)$, because one factor turns the entries of one index only. The switch is applied through both indices of the array because the two indices are the two slots of the operator, and the sign that separates the two families depends on the pair.

**Both directions.** The identity is symmetric in the two sides, since $\mathsf D^2=\mathrm I_4$:

$$
R_{\mathrm{axf}}(\tilde Q)=\mathsf D\,L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}\mathsf D,
\qquad
L_{\mathrm{axf}}(\tilde Q)=\mathsf D\,R_{\mathrm{axf}}(\tilde Q)^{\mathsf T}\mathsf D .
$$

Each family is the transposed image of the other. Both forms hold at residual $0$ on $100$ random elements.

## The Anti-Automorphism Behind the Transpose

**Definition.** An **anti-automorphism** of $\mathbb{B}$ is an additive bijection $\tau$ with

$$
\tau(xy)=\tau(y)\tau(x)\qquad\text{for all }x,y\in\mathbb{B},
$$

which is either $\mathbb{C}$-linear, $\tau(\lambda x)=\lambda\tau(x)$, or $\mathbb{C}$-antilinear, $\tau(\lambda x)=\bar\lambda\,\tau(x)$, for central $\lambda$. The two grades are kept apart, because the operators of the corpus are complex-linear and an antilinear map does not act on them. The inverse of an anti-automorphism is an anti-automorphism of the same grade. Order two is not required anywhere below: the identities use $\tau$ and $\tau^{-1}$ in that order and never $\tau$ alone.

**Theorem ($\natural$ is a complex-linear anti-automorphism).** The quaternion conjugation, $\natural(e_t)=e_t$ and $\natural(\vec e_k)=-\vec e_k$, satisfies $\natural(xy)=\natural(y)\natural(x)$ and is $\mathbb{C}$-linear.

*Proof.* Three cases on the basis. A product with $e_t$ is unchanged by the exchange of the order, and $\natural$ fixes $e_t$. A square $\vec e_k\vec e_k=-e_t$ is scalar, and the two signs cancel, $\natural(\vec e_k\vec e_k)=-e_t=\natural(\vec e_k)\natural(\vec e_k)$. For distinct $k\ne l$ the product $\vec e_k\vec e_l$ is $\pm$ the third unit, so $\natural(\vec e_k\vec e_l)=\mp\vec e_m$, while $\natural(\vec e_l)\natural(\vec e_k)=(-\vec e_l)(-\vec e_k)=-\vec e_k\vec e_l=\mp\vec e_m$. The two sides agree in the three cases, and both are additive and $\mathbb{C}$-linear on the coordinates.

**Theorem ($\ast$ is an antilinear anti-automorphism).** The Hermitian conjugation $\ast=\natural\circ\bar{\cdot}$ satisfies $\ast(xy)=\ast(y)\ast(x)$ and $\ast(\lambda x)=\bar\lambda\,\ast(x)$.

*Proof.* $\ast(xy)=\natural(\bar x\bar y)=\natural(\bar y)\natural(\bar x)=\ast(y)\ast(x)$, the middle equality being the preceding theorem applied to the two conjugated factors.

**Theorem (the coefficient conjugation is not one).** The map $\bar{\cdot}$ that conjugates each of the four coefficients is a $\mathbb{C}$-antilinear **automorphism**, $\overline{xy}=\bar x\,\bar y$.

*Proof.* The structure constants in the coefficient frame are $0$ and $\pm1$, all real, so conjugating the coordinates of a product conjugates the coordinates of the two factors and nothing else.

### The Three Maps of the Coefficient Frame

| map | linearity | the product | fixed space |
|---|---|---|---|
| $\natural$ | $\mathbb{C}$-linear | reversed | $\mathbb{C}e_t$ |
| $\ast=\natural\bar{\cdot}$ | $\mathbb{C}$-antilinear | reversed | $\mathbb{B}_{\Psi}$ |
| $\bar{\cdot}$ | $\mathbb{C}$-antilinear | **preserved** | — |

**The trap.** The coefficient conjugation is the standing error of the subject. It looks like a change of side, because it changes every coefficient, and it exchanges nothing: an identity built on it fails for every noncentral parameter. The mistake is structural and not numerical. The transport of a parameter needs an anti-automorphism, the coefficient conjugation is an automorphism, and the sign it does not supply is the sign of the three vector units, which is the sign that reverses the products.

### All the Complex-Linear Ones

**Proposition.** For every invertible $\tilde U$ the map $\tau_{\tilde U}(\tilde X)=\tilde U\natural(\tilde X)\tilde U^{-1}$ is a complex-linear anti-automorphism, and every complex-linear anti-automorphism arises this way.

*Proof.* The composite of the anti-automorphism $\natural$ with two inner automorphisms is an anti-automorphism, and it is complex-linear. Conversely, the composite of two anti-automorphisms is an automorphism, every $\mathbb{C}$-linear automorphism of a central simple algebra is inner (*Biquaternion Automorphisms and Derivations*, §*Standing Facts: Simplicity and the Centre*), and $\natural$ is one anti-automorphism.

**The order is not order two.** For a general $\tilde U$ the map $\tau_{\tilde U}$ is not an involution: $\tau_{\tilde U}^2$ is the inner automorphism by $\tilde U\natural(\tilde U)$, which is the identity only when that product is central. The identity of the next section needs no more than an anti-automorphism, and it is written with $\tau^{-1}$ for that reason.

## Conjugation by an Anti-Automorphism

**Theorem (the two families are conjugate).** For an anti-automorphism $\tau$ and every $\tilde Q$,

$$
\tau L_{\tilde Q}\tau^{-1}=R_{\tau(\tilde Q)},\qquad
\tau R_{\tilde Q}\tau^{-1}=L_{\tau(\tilde Q)} .
$$

*Proof.* $\tau\bigl(L_{\tilde Q}\tau^{-1}\tilde Y\bigr)=\tau\bigl(\tilde Q\,\tau^{-1}\tilde Y\bigr)=\tau(\tau^{-1}\tilde Y)\,\tau(\tilde Q)=\tilde Y\,\tau(\tilde Q)=R_{\tau(\tilde Q)}\tilde Y$ for every $\tilde Y$, and $\tau$ is a bijection. The second identity is the same computation with the two factors exchanged, and $\tau^{-1}$ is an anti-automorphism of the same grade.

**Corollary (the two images are exchanged).** The map $T\mapsto\tau T\tau^{-1}$ on $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is multiplicative and exchanges the two images, $\tau L(\mathbb{B})\tau^{-1}=R(\mathbb{B})$ and $\tau R(\mathbb{B})\tau^{-1}=L(\mathbb{B})$. It is $\mathbb{C}$-linear in $T$ when $\tau$ is, and conjugate-linear when $\tau$ is antilinear.

**Corollary (a two-sided operator stays two-sided).** $\tau\bigl(L_{\tilde Q_1}R_{\tilde Q_2}\bigr)\tau^{-1}=L_{\tau(\tilde Q_2)}R_{\tau(\tilde Q_1)}$. The sides exchange and the parameters are carried. The corpus records the case $\tau=\natural$ in one line, $\natural L_{\tilde Q}\natural=R_{\tilde Q^{\natural}}$ (*Operator Chirality on the Biquaternion Algebra*, §*Conjugation Exchanges the Sides*).

### Three Maps That Are Not This One

**The three.** Three maps are easy to confuse with this one, and each answers a different question.

- The **matrix transpose** acts on arrays and not on operators. It depends on the frame, and the entry $M^{\mathsf T}$ has the two indices of $M$ exchanged.
- The **associate** $F^{\approx}$ of *Adjoint Pair of $L$ and $R$ Operators* is an adjoint, defined by the plain bilinear form, and it exchanges the families while keeping the parameter: $(L_{\tilde Q})^{\approx}=R_{\tilde Q}$.
- The **swap** $\sigma$ of *Operator Chirality on the Biquaternion Algebra* exchanges the two slots and keeps the parameter, $\sigma(L_aR_b)=L_bR_a$, and it is not inner.

**The fourth, which is this one.** Conjugation by an anti-automorphism reverses the order of the products and carries the parameter, $\tau L_{\tilde Q}\tau^{-1}=R_{\tau(\tilde Q)}$. The associate and the swap describe where an operator sits, and they leave the parameter alone; the conjugation moves the parameter. It is the one the display realises, because a transpose moves the entries of an array and not the operator they display.

**The transposition, with no matrix.** Take $\tau=\natural$. The matrix of $\natural$ in the axis-free frame is $\mathsf D$, so the matrix of $\natural L_{\tilde Q}\natural$ is $\mathsf D\,L_{\mathrm{axf}}(\tilde Q)\,\mathsf D$. The theorem therefore reads

$$
\natural\,L_{\tilde Q}\,\natural=R_{\tilde Q^{\natural}},
\qquad\text{that is}\qquad
\mathsf D\,L_{\mathrm{axf}}(\tilde Q)\,\mathsf D=R_{\mathrm{axf}}(\tilde Q^{\natural}),
$$

and with $\tilde Q$ replaced by $\tilde Q^{\natural}$ it is the boxed identity of the introduction, because $L_{\mathrm{axf}}(\tilde Q^{\natural})=L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}$. The matrix identity and the operator identity are one statement. The transposition of the two sides is a conjugation by the quaternion conjugation, and the switch is the display of that conjugation.

## Every Operator Is a Left Multiplication

**Theorem.** $R_{\tilde Q}=\natural\,L_{\natural(\tilde Q)}\,\natural$, and therefore

$$
\boxed{\;L_{\tilde Q_1}R_{\tilde Q_2}=L_{\tilde Q_1}\,\natural\,L_{\natural(\tilde Q_2)}\,\natural\;}.
$$

*Proof.* The theorem of the preceding section reads $\natural R_{\tilde Q}=L_{\natural(\tilde Q)}\natural$; composing with $\natural^{-1}=\natural$ on the left gives the first identity, and substituting it into the product gives the second.

**The general form.** The same computation for any anti-automorphism reads $\tau R_{\tilde Q}=L_{\tau(\tilde Q)}\tau$, that is $R_{\tilde Q}=\tau^{-1}L_{\tau(\tilde Q)}\tau$, and the product becomes $L_{\tilde Q_1}R_{\tilde Q_2}=L_{\tilde Q_1}\tau^{-1}L_{\tau(\tilde Q_2)}\tau$. Nothing in it uses order two, which is why the inverse and not the map itself stands on the left.

**The reading.** Both factors act on the left. The right factor becomes a left factor at the price of one application of $\natural$ before it and one after it. This is the sense in which the corpus writes every action on the left: a right multiplication is not a second kind of operator, it is a left multiplication by the quaternion conjugate composed with the conjugation, and the conjugation falls on the operand as well as on the parameter.

### The Anti-Representation Explained

**Corollary.** The right family is an anti-representation, $R_{\tilde Q_1}R_{\tilde Q_2}=R_{\tilde Q_2\tilde Q_1}$, while $\tilde Q\mapsto L_{\natural(\tilde Q)}$ is a representation. The first is the second conjugated by $\natural$:

$$
\natural L_{\natural(\tilde Q_1)}\natural\;\natural L_{\natural(\tilde Q_2)}\natural
=\natural\,L_{\natural(\tilde Q_2)\natural(\tilde Q_1)}\,\natural .
$$

The exchange of order inside the right family and the exchange of order inside $\natural$ are one and the same exchange, read once on the parameters and once on the products. Nothing is added to the algebra to obtain an anti-representation: one conjugation removes it.

### Generation

**Corollary.** The operators of $\mathbb{B}$ are generated by the left multiplications together with $\natural$.

*Proof.* The two families together generate $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, by $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ (*The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*). Every right multiplication is $\natural L\natural$ by the theorem above, so it lies in the algebra generated by $L(\mathbb{B})$ and $\natural$.

## Every Frame Has Its Switch

**A general carrier basis.** A transpose depends on the frame, so $R=\mathsf D L^{\mathsf T}\mathsf D$ is the shape the identity takes in the axis-free frame and not the shape it takes everywhere. In a carrier basis where the plain bilinear form $\beta$ has Gram matrix $\mathsf W$ the adjoint of a matrix is $\mathsf W^{-1}M^{\mathsf T}\mathsf W$, and the two families are related by

$$
[R(\tilde Q)]=\mathsf W^{-1}[L(\tilde Q)]^{\mathsf T}\mathsf W .
$$

The matrix $\mathsf W$ is the switch. It is symmetric, and it is the Gram matrix of $\beta$ and not a change of basis: a change of basis replaces it by $\mathsf P^{\mathsf T}\mathsf W\mathsf P$ and the array by $\mathsf P^{-1}[X]\mathsf P$, and the two changes cancel. The identity $\mathsf W^2=\mathrm I_4$ holds only in the axis-free frame, which is why the symmetric form $\mathsf W(\cdot)^{\mathsf T}\mathsf W$ is not the general rule and the inverse must be written.

**The two frames of the corpus.**

| frame | switch | the transpose of a left matrix |
|---|---|---|
| axis-free | $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$ | the left matrix of $\tilde Q^{\natural}$ |
| Peirce | $\mathsf P$, the display of the exchange $S$ | the left matrix of $S\tilde Q$ |

**The reading.** The transposition of the two sides survives every frame: the right array is always the transposed left array read through the switch. What changes from frame to frame is the element map that the transpose implements, and with it the usefulness of the dictionary. The corpus keeps the axis-free frame because there the transpose implements the quaternion conjugation, so the passage from one side to the other is a passage from an element to its conjugate, and the display of the price is a sign matrix.

## The Parameter

**Proposition.** $R_{\tilde Q}=L_{\tilde Q}$ exactly when $\tilde Q$ is central.

*Proof.* The identity $\tilde X\tilde Q=\tilde Q\tilde X$ for every $\tilde X$ is the definition of the centre, which is $\mathbb{C}e_t$.

**Proposition (the shortcut on a fixed space).** If $\tau(\tilde Q)=\tilde Q$, then $\tau R_{\tilde Q}=L_{\tilde Q}\tau$: on the fixed space of an anti-automorphism, a right multiplication by $\tilde Q$ is a left multiplication by $\tilde Q$ once $\tau$ is carried through.

*Proof.* $\tau(\tilde X\tilde Q)=\tau(\tilde Q)\tau(\tilde X)=\tilde Q\tau(\tilde X)$.

The fixed spaces are the last column of the table of §*The Three Maps of the Coefficient Frame*: the centre for $\natural$, where the shortcut is the triviality $R=L$, and the sector $\mathbb{B}_{\Psi}$ for $\ast$, where it is a genuine transfer, since $R_{\tilde Q}\ne L_{\tilde Q}$ off the centre.

**The two errors, which are distinct.** The first is to take the coefficient conjugation for an anti-automorphism: it preserves the product, so the family it is expected to exchange is not exchanged, and the identity it is expected to give fails for every noncentral parameter. The second is to drop the transport of the parameter: the identity $\tau(\tilde X\tilde Q)=\tilde Q\tau(\tilde X)$ holds on the fixed space and nowhere else, so an equation written with the same parameter on both sides is a statement about a fixed point of $\tau$ and not a general one.

## Summary

A right multiplication is a transposed left multiplication read through the switch. In the axis-free frame the two halves are $L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L_{\mathrm{axf}}(\tilde Q^{\natural})$ and $R_{\mathrm{axf}}(\tilde Q)=\mathsf D L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}\mathsf D$. The first says that a transpose keeps the operator on the left and changes the element into its quaternion conjugate, because the left display is diagonal and skew off the diagonal, $L^{\mathsf T}=2Q_t\mathrm I_4-L$. The second says that reaching the other side costs one conjugation by the switch.

The mechanism is a sign count on the two displays. They agree on the diagonal, on the first row and on the first column, and they differ on the six entries whose two indices are both vector, because distinct vector units anticommute. The transpose turns all twelve off-diagonal signs, the switch turns back the six that carry one scalar index, and the six that survive are the six that anticommute. That is the whole proof.

At the level of operators no matrix is needed. An anti-automorphism conjugates the left family onto the right one, $\tau L_{\tilde Q}\tau^{-1}=R_{\tau(\tilde Q)}$, and with $\tau=\natural$ this is $R_{\tilde Q}=\natural L_{\tilde Q^{\natural}}\natural$, which is the same equation as the boxed display, because the matrix of $\natural$ is the switch and the transpose is $\natural$. Hence $R_{\tilde Q}=\natural L_{\natural(\tilde Q)}\natural$, and every two-sided operator is two left multiplications separated by one conjugation, $L_{\tilde Q_1}R_{\tilde Q_2}=L_{\tilde Q_1}\natural L_{\natural(\tilde Q_2)}\natural$. The anti-representation of the right family is the representation of the left family conjugated by $\natural$, and the left family together with $\natural$ generates every operator.

Every frame has its own switch, the Gram matrix of the plain form there, and its own element map implemented by the transpose; the axis-free frame is kept because there the switch is the display of that map and the price of a change of side is a sign matrix. The parameter is carried by the conjugation, so the shortcut that drops it is exact on the fixed space and false off it, the fixed spaces being the centre for $\natural$ and the sector $\mathbb{B}_{\Psi}$ for $\ast$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau$, $\tau(xy)=\tau(y)\tau(x)$ | an anti-automorphism, complex-linear or conjugation-linear; order two is **not** required |
| $\natural$ | the quaternion conjugation, $\mathrm{id}$ on the centre and $-\mathrm{id}$ on the span of $\vec e_x,\vec e_y,\vec e_z$; a complex-linear anti-automorphism |
| $\ast=\natural\bar{\cdot}$ | the Hermitian conjugation; a conjugation-linear anti-automorphism |
| $\bar{\cdot}$ | the coefficient conjugation; a conjugation-linear **automorphism**, not an anti-automorphism |
| $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$ | the switch of the axis-free frame, the Gram matrix of $\beta$ there, and the matrix of $\natural$; the two axis-free articles write it $D$ |
| $\mathsf W$ | the switch in a general carrier basis, the Gram matrix of $\beta$ there |
| $\mathsf P$ | the display of the exchange $S$ in the Peirce frame, and the switch there |
| $L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}=L_{\mathrm{axf}}(\tilde Q^{\natural})$ | the transpose of a left matrix is a left matrix, of the conjugate element |
| $R_{\mathrm{axf}}(\tilde Q)=\mathsf D L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}\mathsf D$ | the right matrix as a transposed left matrix |
| $[R(\tilde Q)]=\mathsf W^{-1}[L(\tilde Q)]^{\mathsf T}\mathsf W$ | the same identity in a general frame |
| $R_{\tilde Q}=\natural L_{\tilde Q^{\natural}}\natural=\natural L_{\natural(\tilde Q)}\natural$ | the same identity with no matrix |
| $\tau L_{\tilde Q}\tau^{-1}=R_{\tau(\tilde Q)}$ | conjugation by an anti-automorphism exchanges the two families |
| $L_{\tilde Q_1}R_{\tilde Q_2}=L_{\tilde Q_1}\natural L_{\natural(\tilde Q_2)}\natural$ | a two-sided operator as two left multiplications |
| $\tau_{\tilde U}(\tilde X)=\tilde U\natural(\tilde X)\tilde U^{-1}$ | the general complex-linear anti-automorphism, in general not an involution |
| fixed space: $\mathbb{C}e_t$ for $\natural$, $\mathbb{B}_{\Psi}$ for $\ast$ | the parameters the conjugation does not carry |

## Further Reading

- [Operators Acting on One Side](operators-acting-on-one-side.html), for the two families $L(\mathbb{B})$ and $R(\mathbb{B})$, their injectivity and their composition laws, and for the exchange $S$ and the matrix identity $\mathsf P L_{\mathrm{pau}}(\tilde Q)^{\mathsf T}\mathsf P^{-1}=R_{\mathrm{pau}}(\tilde Q)$
- [$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html), §*The Stitch Between the Copies*, for the entry-by-entry computation of $R_{\mathrm{axf}}(\tilde Q)=\mathsf D L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}\mathsf D$ in the frame used here
- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html), for the exchange of the two sides, $\natural L_{\tilde Q}\natural=R_{\tilde Q^{\natural}}$, for the switch as the Gram matrix of the plain form, and for the difference between that map and the swap of the two slots
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the family that this article rewrites as two left multiplications, and for the Hermitian pair $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{\ast}}$
