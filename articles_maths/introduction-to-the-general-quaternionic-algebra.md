# __Introduction to the General Quaternionic Algebra__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, defined side by side in *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*. Read as a multiplication, the first of them makes that space an associative unital algebra, and that reading is *Introduction to the Biquaternion Algebra*; the second is the **general quaternionic bilinear product** $\tilde P^{\natural}\tilde Q$, and it is the subject of this article. The name is the one of the four-general-products article: *complex* is the base ring, over which all four rules are written, and *quaternionic* marks the product whose first element is read through the natural conjugation ${}^{\natural}$, the $\mathbb{C}$-linear extension of the quaternionic conjugation. The word names a slot and not a base ring. The product is $\mathbb{C}$-bilinear and it is nothing more: it is not associative and it is unital on one side alone, so it is not the multiplication of an associative unital algebra, as the comparison of the four settles. What it defines is a multiplication in the weak sense of *Algebras: A General Introduction*, additive in each variable and linear over the commutative ring $\mathbb{C}$, and this article builds the algebra that this multiplication makes of $\mathbb{B}$.

The construction is short and the consequences are of two kinds. The product is the plain multiplication with one conjugation inserted in the first slot, so the table is read off the quaternion table, bilinearity is immediate, and the failure of the axioms is decided by short computations on the basis; but the product is also the multiplication whose square of every element lands in the scalar line and whose symmetrisation is scalar. The article therefore has a negative half — the axioms the product fails, among them the three quaternionic scalar laws, which is where the base ring is fixed — and a positive half, in which the square, the idempotents, the nilpotents and the graded behaviour on the remarkable subspaces are read off.

The boundaries are stated at once. The product is not defined here: the coordinate rule and the four names are *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, the identities that link the four general products are *Relations Between the Four General Products*, and their properties are compared in *Comparison Between the Four General Products*. The same space read with the plain product is *Introduction to the Biquaternion Algebra* and with the star in the second slot is *Introduction to the General Plain Sesqualgebra*; the fourth product is *Introduction to the General Quaternionic Sesqualgebra*. The question of the base rings is *The Realification and the Effect of the Change of Scalars*, and the centre is proved in *Introduction to the Biquaternion Algebra*, §*The Scalars Are the Centre*; what is done here with the base ring is narrower and sharp: the three quaternionic scalar laws are tested on the product and the answer fixes the base at $\mathbb{C}$. The elements, the basis, the conjugations and the remarkable subspaces are *The Biquaternioid as a Vector Space over $\mathbb{C}$*, *Introduction to the Remarkable Subspaces*, *Decompositions Along the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*, and the span table of the plain product on the remarkable subspaces is *Remarkable Subspaces and the Four General Products*; what is done here with the subspaces is narrower, the agreement with the plain product on the scalar line, the negated quaternion product on the vector part, and the $\mathbb{Z}/2$-grading that the real quaternion splitting gives to this multiplication. The general theory is *Algebras: A General Introduction*, associativity is *Associative Algebras*, the identity is *Unital Algebras*, the three weaker identities are *Non-Associative Algebras and the Property Ladder*, and the anti-automorphisms are *Opposite Algebras and Anti-Isomorphisms*. On the biquaternion side, the units and the invertibility criterion are read in the same article, the zero divisors are *Zero Divisors of the Biquaternion Algebra*, and the idempotents of the algebra are *Idempotents of the General Plain Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and central scalar imaginary $i$, $i^2=-1$; a general element is $\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. Throughout, an element is written $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=\sum_{\mu=1}^{3}Q_\mu\vec e_\mu$, and $(\vec P,\vec Q)=\sum_\mu P_\mu Q_\mu$ and $\vec P\times\vec Q$ are the complex bilinear dot and cross products of the vector parts. The conjugations are the natural one ${}^{\natural}$, which keeps the scalar coordinate and negates the three vector coordinates, the coefficientwise one $\bar{\cdot}$, which conjugates the four coefficients, and the star ${}^{*}=\bar{\cdot}\circ{}^{\natural}={}^{\natural}\circ\bar{\cdot}$; the sign vector is $\varepsilon=(1,-1,-1,-1)$, so that $Q^{\natural}_\nu=\varepsilon_\nu Q_\nu$. The plain product is written $\tilde P\tilde Q$ and the product of this article is written $\star$, with

$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q
$$

throughout. The four general products and their notation are those of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*.

## The Multiplication as a Binary Operation

### The Rule

**Definition.** The **multiplication** of the algebra is the rule

$$
\star \; : \; \mathbb{B}\times\mathbb{B}\longrightarrow\mathbb{B} , \qquad
(\tilde P,\tilde Q)\longmapsto \tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\mu P_\mu Q_\nu\,e_\mu e_\nu ,
$$

the general quaternionic bilinear product of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*. Each of the sixteen products $e_\mu e_\nu$ is a basis element up to sign, so the double sum is a complex combination of $e_t,\dots,\vec e_z$: the rule is a map into $\mathbb{B}$ and is well defined. On the four coordinates it reads

$$
\tilde P\star\tilde Q=\bigl(P_tQ_t+P_xQ_x+P_yQ_y+P_zQ_z\bigr)
+\bigl(P_tQ_x-P_xQ_t-P_yQ_z+P_zQ_y\bigr)\vec e_x
+\bigl(P_tQ_y+P_xQ_z-P_yQ_t-P_zQ_x\bigr)\vec e_y
+\bigl(P_tQ_z-P_xQ_y+P_yQ_x-P_zQ_t\bigr)\vec e_z ,
$$

### The Scalar–Vector Form

Collecting the scalar part and the vector part of the two elements, the same product reads

$$
\tilde P\star\tilde Q=\bigl(P_tQ_t+(\vec P,\vec Q)\bigr)+P_t\vec Q-Q_t\vec P-\vec P\times\vec Q ,
$$

the coordinate display of the definition with the vector part of the first factor negated, which is what the conjugation ${}^{\natural}$ does to it; both displays are quoted from *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*. The scalar part of the product is $\mathrm{Sc}(\tilde P\star\tilde Q)=\sum_{\mu\in\{t,x,y,z\}}P_\mu Q_\mu$, written on the coordinates of the two factors.

### The Multiplication Table

A product that is additive in each argument and linear over $\mathbb{C}$ is fixed by its values on the basis pairs, so the multiplication is fixed by the following sixteen products.

**Proposition.** The products of the basis elements are $e_\mu\star e_\nu=\varepsilon_\mu\,e_\mu e_\nu$, and they are

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $e_t$ | $-\vec e_z$ | $\vec e_y$ |
| $\vec e_y$ | $-\vec e_y$ | $\vec e_z$ | $e_t$ | $-\vec e_x$ |
| $\vec e_z$ | $-\vec e_z$ | $-\vec e_y$ | $\vec e_x$ | $e_t$ |

**Proof.** Read from the rule: $e_\mu\star e_\nu=(e_\mu)^{\natural}e_\nu=\varepsilon_\mu e_\mu e_\nu$, and the entries are the products of the quaternion units, $\vec e_x \vec e_y=\vec e_z$, $\vec e_y \vec e_z=\vec e_x$, $\vec e_z \vec e_x=\vec e_y$ and $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$, of *Quaternion Algebra*, multiplied by the sign $\varepsilon_\mu$.

The table is not the quaternion table, and the differences are worth naming because they carry the whole structure. Its diagonal is $e_t$ throughout, while three entries of the quaternion diagonal are $-e_t$; its first row is the identity row, $e_t\star e_\nu=e_\nu$, while its first column is the negation of the basis, $e_\mu\star e_t=-e_\mu$ for $\mu\neq t$; and the three-by-three block of the imaginary units is the quaternion table with every entry negated, $e_\mu\star \vec e_\nu=-e_\mu \vec e_\nu$ there. The scalar imaginary $i$ occurs nowhere among the entries, being central and so confined to the coefficients. A table with a positive diagonal and a negated first column is the table of the quaternion product read with the first factor conjugated, which is exactly $\star$.

### Additivity and the Determination by the Table

**Proposition.** The multiplication is **$\mathbb{C}$-bilinear**: it is additive in each variable and

$$
(\tilde P+\tilde Q)\star\tilde R=\tilde P\star\tilde R+\tilde Q\star\tilde R , \qquad
\tilde R\star(\tilde P+\tilde Q)=\tilde R\star\tilde P+\tilde R\star\tilde Q , \qquad
(A\tilde P)\star\tilde Q=A(\tilde P\star\tilde Q)=\tilde P\star(A\tilde Q) , \qquad A\in\mathbb{C} .
$$

**Proof.** The natural conjugation is $\mathbb{C}$-linear, $(\lambda\tilde P)^{\natural}=\lambda\tilde P^{\natural}$, and the plain product is $\mathbb{C}$-bilinear; the three identities follow. Equivalently they are read coordinate by coordinate on the developed form, every coordinate of which is a sum of terms $P_\mu Q_\nu$ with fixed coefficients.

**Proposition (determination by the table).** The multiplication is the unique $\mathbb{C}$-bilinear map $\mathbb{B}\times\mathbb{B}\to\mathbb{B}$ sending the pair $(e_\mu,e_\nu)$ to the product $e_\mu\star e_\nu$ of the table.

**Proof.** A $\mathbb{C}$-bilinear map is determined by its values on the pairs of basis elements, and the double sum of the definition is such a map and takes those values.

**Corollary.** Two multiplications on the same space that agree on the sixteen pairs of basis elements agree on every pair.

## The Base Ring Is $\mathbb{C}$ and Not $\mathbb{H}$

### The Four Quaternionic Scalar Laws

The space $\mathbb{B}$ is a module over $\mathbb{C}$ and also, by restriction of scalars along $\mathbb{R}\subset\mathbb{C}$, a real vector space of dimension eight carrying the left and the right action of the subalgebra $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_t+\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$. Four laws ask whether a multiplication is linear for those two actions, and they are the four a product must satisfy to define an algebra over the skew field $\mathbb{H}$ rather than over the field $\mathbb{C}$.

**Definition.** Let $\cdot$ be a multiplication on $\mathbb{B}$. Then $\cdot$ is **left $\mathbb{H}$-linear in the first slot**, **left $\mathbb{H}$-linear in the second**, **right $\mathbb{H}$-linear in the second** and **compatible with the $\mathbb{H}$-ring structure** when, for all $h\in\mathbb{H}$ and all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
(h\tilde P)\cdot\tilde Q=h(\tilde P\cdot\tilde Q) , \qquad
\tilde P\cdot(h\tilde Q)=h(\tilde P\cdot\tilde Q) , \qquad
\tilde P\cdot(\tilde Q h)=(\tilde P\cdot\tilde Q)h , \qquad
(\tilde P h)\cdot\tilde Q=\tilde P\cdot(h\tilde Q) ,
$$

the products $h\tilde P$ and $\tilde Q h$ being those of the algebra. The first two are the two ways the left action of $\mathbb{H}$ moves through the product, the third is the way the right action does, and the fourth is the balance of the two actions in the middle slot, the condition for the product to descend to the tensor product $\mathbb{B}\otimes_{\mathbb{H}}\mathbb{B}$; a product that satisfies the first, the third and the fourth makes of $\mathbb{B}$ a multiplication of the $\mathbb{H}$-bimodule, and one that satisfies all four makes it one over a central action.

**Proposition.** The product $\star$ is right $\mathbb{H}$-linear in the second slot, and it fails the other three laws.

**Proof.** Since $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, the second slot enters as a factor of the plain product, so moving $h$ within that factor is free: $\tilde P\star(\tilde Q h)=\tilde P^{\natural}\tilde Qh=(\tilde P\star\tilde Q)h$, which is the third law. For the first law put $h=\vec e_x$ and $\tilde P=\tilde Q=e_t$: the left-hand side is $(\vec e_x e_t)\star e_t=\vec e_x\star e_t=-\vec e_x$, while the right-hand side is $\vec e_x(e_t\star e_t)=\vec e_x e_t=\vec e_x$, and the two differ. For the second law put $h=\vec e_x$, $\tilde P=\vec e_y$ and $\tilde Q=e_t$: the left-hand side is $\vec e_y\star \vec e_x=(\vec e_y)^{\natural}\vec e_x=-\vec e_y \vec e_x=\vec e_z$, while the right-hand side is $\vec e_x(\vec e_y\star e_t)=\vec e_x(\vec e_y)^{\natural}=-\vec e_x \vec e_y=-\vec e_z$, and the two differ. For the fourth law put $h=\vec e_x$ and $\tilde P=\tilde Q=e_t$: the left-hand side is $(e_t \vec e_x)\star e_t=\vec e_x\star e_t=-\vec e_x$, while the right-hand side is $e_t\star(\vec e_x e_t)=e_t\star \vec e_x=\vec e_x$, and the two differ.

The laws are gathered in the table, "yes" meaning that the law holds for every $h$, $\tilde P$ and $\tilde Q$.

| law of the multiplication | plain | $\star$ |
|---|---|---|
| left linear in the first slot, $(h\tilde P)\cdot\tilde Q=h(\tilde P\cdot\tilde Q)$ | yes | no |
| left linear in the second slot, $\tilde P\cdot(h\tilde Q)=h(\tilde P\cdot\tilde Q)$ | no | no |
| right linear in the second slot, $\tilde P\cdot(\tilde Q h)=(\tilde P\cdot\tilde Q)h$ | yes | yes |
| compatible with the $\mathbb{H}$-ring, $(\tilde P h)\cdot\tilde Q=\tilde P\cdot(h\tilde Q)$ | yes | no |

**Corollary.** The product $\star$ is not $\mathbb{H}$-bilinear in any sense, and $\mathbb{B}$ with $\star$ is not an algebra over the quaternion skew field $\mathbb{H}$: three of the four laws fail, the only survivor being the right action in the second slot, and a multiplication over a skew field needs the left action in both slots together with the balance of the two actions.

**Proposition (the plain product, for contrast).** The plain product satisfies the first, the third and the fourth laws, and it fails the second: at $h=\vec e_x$, $\tilde P=\vec e_y$ and $\tilde Q=e_t$ the left-hand side $\tilde P(h\tilde Q)$ is $-\vec e_z$ while the right-hand side $h(\tilde P\tilde Q)$ is $\vec e_z$.

**Proof.** The first, the third and the fourth are associativity of the plain product read in the three slots; the second is the first composed with the commutation of $h$ past $\tilde P$, and it fails at the witness because the quaternion units do not commute.

**Remark.** The plain product is thus the multiplication of the $\mathbb{H}$-**bimodule** $\mathbb{B}$: it is balanced, left $\mathbb{H}$-linear in the first slot and right $\mathbb{H}$-linear in the second, which is what *Modules over the Quaternion Algebra* records as the two commuting actions. The $\natural$-product keeps the third law alone, the one that involves the second slot and the right action; it fails the balance and both laws of the first slot, so **it is not a multiplication of the $\mathbb{H}$-bimodule**, and what it keeps is exactly what survives of the bimodule laws when the first factor is conjugated. The second law fails for the plain product too, and for the same reason: it asks the left action to pass a factor that need not commute with it, and over the non-commutative $\mathbb{H}$ only a central scalar does.

**Corollary (where the scalars come from).** The base ring of the multiplication $\star$ is $\mathbb{C}$: the product is $\mathbb{C}$-bilinear by the proposition of the preceding section, and the $\mathbb{H}$-actions do not pass through it, by the two columns of the table, the plain product keeping the three laws of the bimodule and this one keeping a single one-sided law. The central imaginary $i$ acts as a scalar, $i(\tilde P\star\tilde Q)=(i\tilde P)\star\tilde Q=\tilde P\star(i\tilde Q)$, while the quaternion units $\vec e_x,\vec e_y,\vec e_z$ do not, as the witness of the first law shows. This is the narrow statement the article owns; the general question of which rings are admissible for the *plain* product, and the centrality criterion that answers it, are *The Realification and the Effect of the Change of Scalars*.

### The Product as the Plain Product with the Conjugation Inserted

**Proposition.** The multiplication $\star$ is the **isotope** of the plain multiplication determined by the pair $(\natural,\mathrm{id})$, that is,

$$
\tilde P\star\tilde Q=\natural(\tilde P)\,\tilde Q \qquad\text{with}\qquad \natural(\tilde P)=\tilde P^{\natural} ,
$$

the insertion of $\natural$ in the first slot being the isotope, and $\natural$ being a $\mathbb{C}$-linear anti-automorphism of the algebra.

**Proof.** The first display is the definition of the product: an isotope of a binary operation is the operation $(\tilde P,\tilde Q)\mapsto\varphi(\tilde P)\psi(\tilde Q)$ obtained by inserting a pair of bijections, here $\natural$ in the first slot and the identity in the second. The map $\natural$ is $\mathbb{C}$-linear, involutive and anti-multiplicative, $(\tilde P\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural}$ (*The Group of Involutions*, *Introduction to the Biquaternion Algebra*), so it is an anti-automorphism, and it is its own inverse, hence bijective.

**Remark.** The reading is worth keeping because it explains the failures at once. An isotope of an associative product is associative only when the inserted maps are compatible with the multiplication, and the anti-automorphism $\natural$ is the wrong way round; it is this reversal that produces the associator of the next section, the reversed composition of the left multiplications, and the failure of the quaternionic scalar laws. The two bilinear products of the four are therefore not two unrelated multiplications: one is the isotope of the other, and the comparison of the four records the same fact in its own words, the $\natural$-product being *the general plain bilinear product read with the $\mathbb{C}$-linear conjugation inserted in the first slot* (*Comparison Between the Four General Products*).

## The Algebra Axioms

### Associativity

**Proposition.** The multiplication is **not associative**.

**Proof.** $(\vec e_x\star \vec e_x)\star \vec e_x=e_t\star \vec e_x=\vec e_x$ while $\vec e_x\star(\vec e_x\star \vec e_x)=\vec e_x\star e_t=-\vec e_x$, and the two differ because $\vec e_x\neq-\vec e_x$.

**Proposition (the associator).** The **associator** of the multiplication,

$$
[\tilde P,\tilde Q,\tilde R]=(\tilde P\star\tilde Q)\star\tilde R-\tilde P\star(\tilde Q\star\tilde R) ,
$$

is

$$
[\tilde P,\tilde Q,\tilde R]=\bigl(\tilde Q^{\natural}\tilde P-\tilde P^{\natural}\tilde Q^{\natural}\bigr)\tilde R .
$$

**Proof.** The product satisfies $(\tilde P\star\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P$, since $\natural$ is an anti-automorphism and an involution; hence $(\tilde P\star\tilde Q)\star\tilde R=(\tilde P\star\tilde Q)^{\natural}\tilde R=\tilde Q^{\natural}\tilde P\tilde R$, while $\tilde P\star(\tilde Q\star\tilde R)=\tilde P^{\natural}(\tilde Q\star\tilde R)=\tilde P^{\natural}\tilde Q^{\natural}\tilde R$. The difference is the displayed form.

**Corollary.** The associator is $\mathbb{C}$-bilinear in the three variables, and it is the product of a fixed defect, $\tilde Q^{\natural}\tilde P-\tilde P^{\natural}\tilde Q^{\natural}$, on the right by $\tilde R$.

**Corollary.** The multiplication agrees with the plain product, and is therefore associative and commutative, on the scalar line $\mathbb{C}e_t$, which is the fixed subspace of $\natural$; and it is not associative on the subspace spanned by $e_t$ and any one of $\vec e_x,\vec e_y,\vec e_z$, by the witness above. Associativity of the $\natural$-product is thus the triviality of the conjugation, which happens on the scalar line alone.

### The Unit

**Proposition.** The element $e_t$ is a **left unit** of the multiplication: $e_t\star\tilde Q=\tilde Q$ for every $\tilde Q$. It is the only left unit.

**Proof.** $\natural$ fixes $e_t$, so $e_t\star\tilde Q=e_t\tilde Q=\tilde Q$; and a left unit $\tilde E$ satisfies $\tilde E\star\tilde Q=\tilde Q$ for every $\tilde Q$, which at $\tilde Q=e_t$ reads $\tilde E^{\natural}=e_t$, whence $\tilde E=e_t$, the map $\natural$ being an involution.

**Proposition.** There is **no right unit**: the equation $\tilde P\star\tilde E=\tilde P$ for all $\tilde P$ has no solution.

**Proof.** At $\tilde P=e_t$ it reads $\tilde E=e_t$, and at $\tilde P=\vec e_x$ it reads $\vec e_x\star e_t=\vec e_x$, which is false, the value being $-\vec e_x$.

**Remark.** The two actions of the unit by multiplication are therefore the identity and a conjugation: the left action is the identity, $e_t\star\tilde Q=\tilde Q$, and the right action is the natural conjugation, $\tilde Q\star e_t=\tilde Q^{\natural}$. Neither is a two-sided unit, and no element of $\mathbb{B}$ is one, so the multiplication has a unit on one side alone. The left multiplications nonetheless compose, in reversed order, by the proposition below, and that is why the comparison of the four records a monoid of left multiplications for this product although the product has no two-sided unit.

**Proposition (the left multiplications).** The left multiplications $L_{\tilde P}(\tilde Q_1)=\tilde P\star\tilde Q_1$ compose in the reversed order of the algebra,

$$
L_{\tilde P}\circ L_{\tilde R}=L_{\tilde R\tilde P} ,
$$

so they form a monoid anti-isomorphic to the multiplicative monoid of $\mathbb{B}$.

**Proof.** $L_{\tilde P}(L_{\tilde R}(\tilde Q_1))=\tilde P^{\natural}(\tilde R^{\natural}\tilde Q_1)=(\tilde R\tilde P)^{\natural}\tilde Q_1=L_{\tilde R\tilde P}(\tilde Q_1)$, using the anti-multiplicativity of $\natural$ twice.

### Non-Commutativity and the Centre

**Proposition.** The multiplication is **not commutative**.

**Proof.** $\vec e_x\star \vec e_y=-\vec e_z$ while $\vec e_y\star \vec e_x=\vec e_z$.

**Proposition (the centre is trivial).** No nonzero element of $\mathbb{B}$ commutes with every element for the multiplication $\star$.

**Proof.** Let $\tilde Q_2$ satisfy $\tilde Q_2\star\tilde Q_1=\tilde Q_1\star\tilde Q_2$ for every $\tilde Q_1$. At $\tilde Q_1=e_t$ it reads $\tilde Q_2\star e_t=\tilde Q_2^{\natural}$ on the left and $e_t\star\tilde Q_2=\tilde Q_2$ on the right, so $\tilde Q_2^{\natural}=\tilde Q_2$ and $\tilde Q_2$ has zero vector part, $\tilde Q_2=Q_{2t}e_t$. The identity then reads $Q_{2t}\tilde Q_1$ on the left, since $\tilde Q_2\star\tilde Q_1=\tilde Q_2^{\natural}\tilde Q_1=Q_{2t}\tilde Q_1$, and $Q_{2t}\tilde Q_1^{\natural}$ on the right, so $Q_{2t}\tilde Q_1=Q_{2t}\tilde Q_1^{\natural}$ for every $\tilde Q_1$; at $\tilde Q_1=\vec e_x$ this is $Q_{2t}\vec e_x=-Q_{2t}\vec e_x$, whence $Q_{2t}=0$.

**Remark.** The product has no centre at all, and this separates it sharply from the plain product, whose centre is the scalar line $\mathbb{C}e_t$ (*Introduction to the Biquaternion Algebra*). The complex scalars still act, by the corollary of the preceding section, and their action is left multiplication by $\varphi(A)=Ae_t$, since $\natural$ fixes the scalar line and $A\tilde Q=(Ae_t)\star\tilde Q$; but the element $\varphi(A)$ that represents the action is not central, $\tilde Q\star(Ae_t)=A\tilde Q^{\natural}$. Centrality is an axiom of the associative reading and not of the bilinear one: a $\mathbb{C}$-bilinear product needs its scalars to act compatibly in both slots, which $\star$ does, and needs no central element to represent them, which $\star$ does not have.

### The Weaker Identities

The three classical weakenings of associativity are settled by the witnesses already computed in *Comparison Between the Four General Products*, and they are recalled here in the notation of this article.

**Proposition.** The multiplication is **not alternative**, **not flexible** and **not power associative**.

**Proof.** The left alternative law $\tilde P\star(\tilde P\star\tilde Q)=(\tilde P\star\tilde P)\star\tilde Q$ fails at $\tilde P=\vec e_z$, $\tilde Q=-\vec e_z$, where the two sides are $\vec e_z$ and $-\vec e_z$; the flexible law $(\tilde P\star\tilde Q)\star\tilde P=\tilde P\star(\tilde Q\star\tilde P)$ fails at $\tilde P=\vec e_z$, $\tilde Q=e_t$, where the two sides are $-e_t$ and $e_t$; and the degree-three identity $\tilde P\star(\tilde P\star\tilde P)=(\tilde P\star\tilde P)\star\tilde P$ fails at $\tilde P=\vec e_z$, where the two sides are $-\vec e_z$ and $\vec e_z$.

**Corollary.** The multiplication is not a Jordan algebra multiplication, being not commutative, and no power of an element is well defined in the sense of power associativity: the two ways of bracketing the triple product of $\vec e_z$ differ.

### The Algebra Structure

**Theorem.** With the general quaternionic bilinear product as its multiplication, $\mathbb{B}$ is a four-dimensional algebra over $\mathbb{C}$ in the sense of *Algebras: A General Introduction* — additive in each variable and $\mathbb{C}$-bilinear — with a left unit $e_t$ and no right one; it is neither associative nor commutative, has trivial centre, and satisfies none of the alternative, the flexible and the degree-three identities.

**Proof.** The product is a $\mathbb{C}$-bilinear binary operation on the $\mathbb{C}$-vector space $\mathbb{B}$ by the propositions of §*The Multiplication as a Binary Operation*, which is the definition of an algebra over the commutative ring $\mathbb{C}$ in the broad sense; the dimension is four on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ (*The Biquaternioid as a Vector Space over $\mathbb{C}$*); and the remaining clauses are the propositions above.

**Remark.** What the algebra is not is as informative as what it is. It is not associative, so the associative theory — the two-sided ideals of *Ideals and Peirce Decomposition of the Biquaternion Algebra*, the modules of *Modules over the Biquaternion Algebra*, the opposite algebra — does not apply to it; it is not two-sidedly unital, so there is no group of units of its own; and it is not commutative, so no centre carries its scalars. What survives is the bilinear structure, the square, and the reading of the product as an isotope of the plain one.

## The Square and the Elements It Distinguishes

### The Square Lies in the Scalar Line

**Proposition.** The square of an element in the multiplication is

$$
\tilde Q\star\tilde Q=\tilde Q^{\natural}\tilde Q=\Bigl(\sum_{\mu\in\{t,x,y,z\}}Q_\mu^2\Bigr)e_t ,
$$

so the square is a scalar element, in the scalar line $\mathbb{C}e_t$.

**Proof.** The scalar–vector form gives $\tilde Q^{\natural}\tilde Q=(Q_t-\vec Q)(Q_t+\vec Q)=Q_t^2-\vec Q^2$, and $\vec Q^2=-(\vec Q,\vec Q)$ for a vector part, so the value is $\bigl(Q_t^2+(\vec Q,\vec Q)\bigr)e_t=\sum_\mu Q_\mu^2e_t$. The same scalar is produced in the two orders, $\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q$.

**Corollary.** Every square lies in the scalar line $\mathbb{C}e_t$; it is fixed by the natural conjugation, and it is central for the plain product. The squaring map of the multiplication is $\tilde Q\mapsto\bigl(\sum_\mu Q_\mu^2\bigr)e_t$, with its values in the scalar line rather than in the field.

**Remark.** The plain product and the $\natural$-product therefore have different squares: the square in the multiplication is $\bigl(\sum_\mu Q_\mu^2\bigr)e_t$ for every $\tilde Q$, whereas the square in the plain product is $Q_t^2-(\vec Q,\vec Q)+2Q_t\vec Q$, which lands in the scalar line exactly when $\tilde Q$ is a multiple of $e_t$, and is then $Q_t^2e_t$, or when its scalar part vanishes, and is then $-\bigl(\sum_{\mu=1}^{3}Q_\mu^2\bigr)e_t$. Which of the two a statement about squares is about must be said each time, and the two are the pair of structures attached to the two bilinear products of the space.

### The Symmetrised and the Antisymmetrised Product

**Proposition.** The product is symmetric modulo its scalar line, and its symmetrisation is scalar:

$$
\tilde P\star\tilde Q+\tilde Q\star\tilde P=2\,\mathrm{Sc}(\tilde P^{\natural}\tilde Q)\,e_t=2\bigl(P_tQ_t+(\vec P,\vec Q)\bigr)e_t , \qquad
\tilde P\star\tilde Q-\tilde Q\star\tilde P=2P_t\vec Q-2Q_t\vec P-2\vec P\times\vec Q .
$$

**Proof.** The sum of the left-hand sides is $\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P$, whose scalar part is twice $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_tQ_t+(\vec P,\vec Q)$ and whose vector part is $P_t\vec Q-Q_t\vec P-\vec P\times\vec Q+Q_t\vec P-P_t\vec Q+\vec P\times\vec Q=0$; the difference is the same computation with the signs kept.

**Corollary.** The symmetrised product lies in the scalar line and the antisymmetrised product in the vector part. The multiplication is thus the sum of a symmetric scalar part and an antisymmetric vector part, the two added inside the algebra rather than in separate spaces, which is the shape in which the quaternion product itself is usually written.

### The Idempotents

**Definition.** Let $\star$ be a product on $\mathbb{B}$. An element is **idempotent of $\star$** when $\tilde Q\star\tilde Q=\tilde Q$, and of **index two**, or **square-zero**, when $\tilde Q\neq0$ and $\tilde Q\star\tilde Q=0$. The definitions are *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, §*The Idempotent, the Projection and the Peirce Decomposition* and §*The Nilpotent*, and they name the product at every step; throughout this article the product is the multiplication $\tilde P^{\natural}\tilde Q$.

**Proposition.** The idempotents of the multiplication are $0$ and $e_t$.

**Proof.** A square lies in $\mathbb{C}e_t$ by the preceding subsection, so an idempotent lies in $\mathbb{C}e_t$, say $\tilde Q=Q_te_t$; the equation $\tilde Q\star\tilde Q=\tilde Q$ then reads $Q_t^2e_t=Q_te_t$, that is $Q_t\in\{0,1\}$.

**Remark.** The multiplication therefore has only the two trivial idempotents, and it has them by the same computation that shows the square to be a scalar. The nontrivial idempotents of the algebra, the elements $\tfrac12(e_t+\xi i)$ with $\xi$ a root of $-1$ of *Idempotents of the General Plain Algebra*, are not idempotent here, and they fail to be so in the strongest way: being zero divisors (*Zero Divisors of the Biquaternion Algebra*), they have $\sum_\mu Q_\mu^2=0$, so by the proposition below their squares in the multiplication vanish rather than returning the elements themselves. The contrast with the sesquilinear reading is sharp: the fourth product of the four has a two-parameter family of idempotents, and it is the subject of *Introduction to the General Quaternionic Sesqualgebra*.

### The Nilpotents and the Zero Divisors

**Proposition.** For a nonzero element the following are equivalent:

$$
\tilde Q\star\tilde Q=0 \iff \sum_{\mu\in\{t,x,y,z\}}Q_\mu^2=0 \iff \tilde Q\ \text{is a zero divisor of the algebra} .
$$

The origin has a vanishing square and is not a zero divisor, the two factors of the defining equation being required to be nonzero.

**Proof.** The first equivalence is the preceding subsection. The second is the unit criterion of the algebra: $\tilde Q$ is a unit exactly when the central scalar $\tilde Q\tilde Q^{\natural}=\bigl(\sum_\mu Q_\mu^2\bigr)e_t$ is non-zero, and the zero divisors are the nonzero elements where it vanishes, classified in *Zero Divisors of the Biquaternion Algebra*.

**Corollary.** The elements whose square vanishes in the multiplication are the solutions of $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$, and they are the zero divisor set of *Zero Divisors of the Biquaternion Algebra* together with the origin: a complex cone of complex dimension $3$ in $\mathbb{B}\cong\mathbb{C}^4$, from which the origin is removed when the zero divisors are meant. The elements $\pm \vec e_x\pm i\vec e_y$, which are pure, and $e_t\pm i\vec e_x$, which are not, are examples; and the word must be watched, because a *nilpotent* of *Zero Divisors of the Biquaternion Algebra* is an element with $\tilde Q\tilde Q=0$ and is pure, while here every zero divisor has a vanishing square. What the multiplication detects is the failure of division, and it detects it in one line: the square $\tilde Q\star\tilde Q=\bigl(\sum_\mu Q_\mu^2\bigr)e_t$ is the central scalar on which invertibility turns.

## The Product on the Remarkable Subspaces

The remarkable subspaces and the exact span table of the plain product on them are *Introduction to the Remarkable Subspaces*, *Comparison of the Remarkable Subspaces* and *Remarkable Subspaces and the Four General Products*; this section records only the three facts that the conjugation in the first slot makes new for this multiplication, the value on the scalar line, the value on the vector part, and the grading.

### The Scalar Line and the Vector Part

**Proposition.** On the scalar line the multiplication agrees with the plain product and is the multiplication of the field: $(Ae_t)\star(Be_t)=ABe_t$ for $A,B\in\mathbb{C}$. On the vector part it is the negated quaternion product: $\vec U\star\vec V=-\vec U\vec V$ for pure vector parts, so its symmetric part is the dot product, $\vec U\star\vec V+\vec V\star\vec U=2(\vec U,\vec V)e_t$, and its antisymmetric part is minus the cross product.

**Proof.** The natural conjugation fixes the scalar line and negates the vector part; on the vector part the plain product of two pure vectors is $-(\vec U,\vec V)+\vec U\times\vec V$, and the product is its negative.

**Remark.** On the vector part the multiplication is therefore the companion of the plain product in the same sense as the quaternion product is the companion of the vector product: the plain product has the symmetric part $-(\vec U,\vec V)$ beside the cross product, and the $\natural$-product has the symmetric part $+(\vec U,\vec V)$ beside the negative cross product. On the scalar line the two agree, which is the statement that $\natural$ is the identity where the conjugation has nothing to do.

### The Quaternion Subspace and Its Imaginary

Let $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_t+\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$ be the real quaternion subspace and $i\mathbb{H}_{\mathbb{B}}$ its imaginary, so that $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ as real vector spaces (*The Biquaternioid as a Vector Space over $\mathbb{C}$*).

**Proposition.** The product respects the splitting: $\mathbb{H}_{\mathbb{B}}\star\mathbb{H}_{\mathbb{B}}\subseteq\mathbb{H}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}\star i\mathbb{H}_{\mathbb{B}}\subseteq i\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}\star\mathbb{H}_{\mathbb{B}}\subseteq i\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}\star i\mathbb{H}_{\mathbb{B}}\subseteq\mathbb{H}_{\mathbb{B}}$. The splitting is therefore a $\mathbb{Z}/2$-grading for the multiplication.

**Proof.** The complex structure is $J(\tilde Q)=i\tilde Q$, and $\natural$ commutes with $J$, being $\mathbb{C}$-linear; the plain product is compatible with $J$ in both slots, $J(\tilde P\tilde Q)=(J\tilde P)\tilde Q=\tilde P(J\tilde Q)$, since $i$ is central. Hence $\star$, which is the plain product with $\natural$ in the first slot, is compatible with $J$ in the same way, and the four inclusions are that statement read on the two halves.

**Proposition.** On the quaternion subspace the multiplication is the plain product with the quaternionic conjugate in the first slot, $h\star g=\bar h\,g$ for real $h,g$, and its square is $h\star h=\bigl(h_t^2+h_x^2+h_y^2+h_z^2\bigr)e_t$. It is not associative there: on the subspace spanned by $e_t$ and one vector unit it fails the associative law, as in §*Associativity*. Its square vanishes on $\mathbb{H}_{\mathbb{B}}$ only at $0$, a sum of squares of real coordinates vanishing only when every coordinate vanishes, and in this it agrees with the record of *Zero Divisors of the Biquaternion Algebra* that the real quaternion subspace carries no zero divisor.

**Proof.** On real coordinates the natural conjugation is the quaternionic conjugation $\bar h$, so $h\star g=\bar hg$; the square is the sum of the squares of the four real coordinates; and the failure of associativity is the witness of §*Associativity*.

**Remark.** The four inclusions say that the multiplication does not mix the two halves in the wrong way, and they hold for the same reason they hold for the plain product: the complex structure is an algebra automorphism for both products. On either half the multiplication has neither a two-sided unit nor associativity; on the even part its square is the sum of the squares of the real coordinates, which vanishes only at the origin, and the two halves are exchanged by the odd products.

## The Position Among the Four General Products

### The Identities That Link the Two Bilinear Products

The identities of *Relations Between the Four General Products* give the multiplication in terms of the plain one and of the scalar part of the first factor:

$$
\tilde P^{\natural}\tilde Q=2P_t\tilde Q-\tilde P\tilde Q , \qquad
\tilde P\tilde Q+\tilde P^{\natural}\tilde Q=2P_t\tilde Q , \qquad
\tilde P\tilde Q-\tilde P^{\natural}\tilde Q=2\vec P\tilde Q .
$$

The first display is the second identity solved for the $\natural$-product, and the three say the same thing: **the multiplication of this article is the plain multiplication with the scalar part of the first factor doubled and the plain product subtracted, that is, with the first factor replaced by its conjugate.** Hence the two bilinear products agree exactly where the first factor is scalar, and the whole difference is carried by the vector part of the first factor. In the language of the preceding section, this is the isotope identity read on the coordinates.

### Which of the Four Is a Multiplication

The comparison of the four settles the question of the two-sided object at once: the two rows that name the categories read yes, yes, no, no for the bilinear kind and no, no, yes, yes for the sesquilinear one, the two bilinear products being the ones that define an algebra over $\mathbb{C}$ in the broad sense (*Comparison Between the Four General Products*). Within the bilinear pair, **exactly one product is the multiplication of an associative unital algebra, and it is the plain product**: the $\natural$-product is $\mathbb{C}$-bilinear, not associative and unital on the left alone, which is the theorem of *Introduction to the Biquaternion Algebra*.

The sharper test of the *derived operation* of *Sesqualgebras* separates the pair in the same way and for the same reason. Let $\sigma(\tilde Q_3)=e_t\star\tilde Q_3$ be the first row of the product, as in the sibling article. Here $\sigma$ is the identity, since $\natural$ fixes $e_t$, so $\sigma$ is not conjugate-linear and condition (i) fails; and condition (ii), $\tilde P\star\tilde Q=\tilde P\sigma(\tilde Q)$, would read $\tilde P^{\natural}\tilde Q=\tilde P\tilde Q$, which fails at $\tilde P=\vec e_x$ and $\tilde Q=e_t$. The $\natural$-product therefore fails both conditions, and it is not the derived operation of the algebra with an involution on either side; the correction it needs is not a conjugation in the second slot but the $\mathbb{C}$-linear conjugation inserted in the first, which is the isotope of §*The Product as the Plain Product with the Conjugation Inserted*.

**The classification of the four.** One product is the multiplication of an associative unital algebra, the plain one; one is a $\mathbb{C}$-bilinear multiplication that keeps only the left unit and the reversed composition of the left multiplications, the $\natural$-product, which is the isotope of the first; and two are the multiplications of a sesqualgebra over the conjugation, of which one, the general plain sesquilinear product, is the derived operation of the algebra with its star, while the fourth, the general quaternionic sesquilinear product, is the isotope of that derived operation by the same conjugation and the subject of *Introduction to the General Quaternionic Sesqualgebra*.

## Summary

The general quaternionic bilinear product $\tilde P^{\natural}\tilde Q$ of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, read as a multiplication, is $\mathbb{C}$-bilinear and additive in each variable, and it is the isotope of the plain product determined by the natural conjugation in the first slot.

$$
\boxed{\
\begin{aligned}
&\text{With the general quaternionic bilinear product, } \mathbb{B} \text{ is a four-dimensional } \mathbb{C}\text{-algebra with a left unit } e_t \text{ and no right one,}\\
&\text{neither associative nor commutative, with trivial centre.}
\end{aligned}
\ }
$$

Its table has $e_t$ on the diagonal, the identity row and the negated column, and the negated quaternion table on the imaginary block. It is $\mathbb{C}$-linear and fails the three $\mathbb{H}$-laws that involve the first slot, keeping only right $\mathbb{H}$-linearity in the second, so it is a multiplication over $\mathbb{C}$ and not over $\mathbb{H}$; the plain product, by contrast, satisfies the three laws that make the same space an $\mathbb{H}$-bimodule, and the two products differ exactly in the laws of the first slot. The associator is $\bigl(\tilde Q^{\natural}\tilde P-\tilde P^{\natural}\tilde Q^{\natural}\bigr)\tilde R$, the product is neither alternative, flexible nor power associative, the left multiplications compose in the reversed order and form a monoid anti-isomorphic to that of the algebra, and the centre is zero while the complex scalars still act by left multiplication by $Ae_t$. The square of an element is the central scalar $\tilde Q\star\tilde Q=\bigl(\sum_\mu Q_\mu^2\bigr)e_t$, so the square lies in the scalar line, the idempotents are $0$ and $e_t$ alone, and the square-zero elements are the zero divisors, the origin apart; the symmetrised product is scalar, read on the scalar line. On the scalar line the multiplication is the plain one, on the vector part it is minus the quaternion product, and the splitting of $\mathbb{B}$ into the quaternion subspace and its imaginary is a $\mathbb{Z}/2$-grading for it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, read here with the general quaternionic bilinear multiplication |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | complex basis; $e_t$ the unit, $\vec e_\mu$ the quaternion units |
| $i$ | central scalar imaginary, $i^2=-1$ |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion and its scalar–vector split, $\vec Q=\sum_\mu Q_\mu\vec e_\mu$ |
| $(\vec P,\vec Q)=\sum_\mu P_\mu Q_\mu$ | complex bilinear dot product of the vector parts |
| $\vec P\times\vec Q$ | complex bilinear cross product of the vector parts |
| ${}^{\natural}$ | the natural conjugation, the $\mathbb{C}$-linear anti-automorphism of the first slot |
| $\bar{\cdot}$, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | the coefficientwise conjugation and the star |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product, the multiplication of the article |
| $\varepsilon=(1,-1,-1,-1)$ | the signs of the conjugation on the basis, $Q^{\natural}_\nu=\varepsilon_\nu Q_\nu$ |
| $[\tilde P,\tilde Q,\tilde R]$ | the associator, $(\tilde Q^{\natural}\tilde P-\tilde P^{\natural}\tilde Q^{\natural})\tilde R$ |
| $L_{\tilde P}$ | the left multiplication $\tilde Q_1\mapsto\tilde P\star\tilde Q_1$, with $L_{\tilde P}\circ L_{\tilde R}=L_{\tilde R\tilde P}$ |
| $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_t+\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$ | the quaternion subspace, on which $\star$ is $\bar hg$ |
| $\sum_\mu Q_\mu^2$ | the scalar coefficient of the square, $\tilde Q\star\tilde Q=\bigl(\sum_\mu Q_\mu^2\bigr)e_t$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion product whose conjugation-twisted form is the multiplication of this article.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for algebras over a commutative ring, the module laws and the tensor product of algebras.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the isotopes and homotopes of an algebra, which is the reading of the $\natural$-product used in this article.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the anti-automorphisms of an algebra and the maps they insert in a product.
- *The Four General Products of the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternioid-c-space.md`), for the product, its coordinate rule and its scalar–vector form.
- *Relations Between the Four General Products* (`articles_maths/relations-between-the-four-general-products.md`), for the identities that link the four general products, among them $\tilde P^{\natural}\tilde Q=2P_t\tilde Q-\tilde P\tilde Q$.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table, the witnesses and the position of the product among the four.
- *Introduction to the Biquaternion Algebra* (`articles_maths/introduction-to-the-biquaternion-algebra.md`), for the associative unital reading of the plain product, its centre and its presentation.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the units and the invertibility criterion.
- *Zero Divisors of the Biquaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), for the zero divisor cone, the two families of zero divisors and the idempotents that lie in it.
- *Square Roots of One and the Idempotents of the Biquaternion Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.md`), for the idempotents $\tfrac12(e_t+\xi i)$ of the algebra, which are not idempotent for the multiplication of this article.
- *Non-Associative Algebras and the Property Ladder* (`articles_maths/non-associative-algebras-and-the-property-ladder.md`), for the alternative, flexible and degree-three identities and the place of this multiplication on the ladder.
