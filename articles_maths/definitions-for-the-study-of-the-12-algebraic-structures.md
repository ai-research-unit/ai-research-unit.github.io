# __Definitions for the Study of the 12 Algebraic Structures__

## Introduction

This article collects, in one place, the definitions of the classes of elements and of the derived operations with which the twelve algebraic structures of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* are studied. It is a definitions article: each notion is stated for a general product, and its statement is then read on the products of the space. It follows the article that names the twelve structures and precedes the articles that study them, so that each of the twelve cites one owner for its vocabulary rather than restating it.

The point of collecting them is that **every definition is relative to a product**, and this is easy to lose when each structure is read on its own. The words *zero divisor*, *idempotent*, *nilpotent*, *unit* each name an equation, and the equation names a product; an element that satisfies the equation of one product need not satisfy that of another. The definitions are therefore stated for a general product $\star$, and every statement that singles out a product names it.

**Conventions.** The complex space is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$ and central imaginary $i$, and an element is $\tilde P=P_0e_0+\mathbf P$ with $\mathbf P=\sum_{k=1}^{3}P_ke_k$, $P_\mu\in\mathbb{C}$. The natural conjugation is ${}^{\natural}$, the star is ${}^{*}$, and the four general products are
$$
\tilde P\tilde Q,\qquad \tilde P^{\natural}\tilde Q,\qquad \tilde P\tilde Q^{*},\qquad \tilde P^{\natural}\tilde Q^{*}.
$$
The **generic product** is written $\star$; the **general plain bilinear product**, the multiplication of the algebra, is written $\tilde P\tilde Q$. Unqualified, a class is taken in the general plain bilinear product, and where another product is meant it is named. The twelve products are the four general products and their symmetric and antisymmetric parts.

- The elements, the basis and the four conjugations are *Biquaternions as a Vector Space over $\mathbb{C}$*.
- The four general products, their co-ordinate forms and the tables of the twelve are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and *The 12 Products of the Biquaternion Complex Space*.
- The twelve structures and their three-letter names are *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.
- The general algebra vocabulary — the unit, the inverse, the Peirce decomposition — is *Unital Algebras*, and the corpus-wide readings of the words are *Conventions in Mathematics*.

This article defines. It states the relativity of the definitions as the principle it is, and it proves the one structural fact the definitions turn on, the transport of §*Transport Along an Isomorphism*; every specialization is cited to the article that owns it.

---

## 1. The Product, its Slots and its Class

A **product** on $\mathbb{B}$ is a map
$$
\star \;:\; \mathbb{B}\times\mathbb{B}\longrightarrow\mathbb{B},
$$
and the twelve products of the space are its instances. A product is read by its **two slots**: the first slot is read either as it stands (**plain**, letter $\mathrm P$) or through the natural conjugation (**quaternionic**, letter $\mathrm Q$), and the second slot is read either as it stands (the **algebra**, letter $\mathrm A$) or through the star (the **sesqualgebra**, letter $\mathrm S$). The four general products are the four combinations, and each of their symmetric and antisymmetric parts is one of the twelve.

**Definition (class of a product).** A product $\star$ is read in each slot through an involution: it is $\sigma$-semilinear in the first slot and $\varsigma$-semilinear in the second,
$$
\star(\lambda x,y)=\sigma(\lambda)\star(x,y),\qquad \star(x,\lambda y)=\varsigma(\lambda)\star(x,y),
$$
where each of $\sigma,\varsigma$ is the identity or the complex conjugation. The product is **$\mathbb{C}$-bilinear** when both are the identity, and **sesquilinear** when the second slot carries the conjugation; the first slot carries one too or not according to the family. Of the four general products only the plain bilinear is $\mathbb{C}$-bilinear, the quaternionic bilinear carries the conjugation in the first slot, the plain sesquilinear in the second, and the quaternionic sesquilinear in both.

**Definition (the laws of a product).** A product $\star$ is **associative** when $(x\star y)\star z=x\star(y\star z)$ for all $x,y,z$; **commutative** when $x\star y=y\star x$; **alternating** when $x\star x=0$ for every $x$, which for a bilinear product is equivalent to anticommutativity, $x\star y=-y\star x$. It satisfies the **Jacobi identity** when $x\star(y\star z)+y\star(z\star x)+z\star(x\star y)=0$, and the **Jordan identity** when $(x\star x)\star(y\star x)=\bigl((x\star x)\star y\bigr)\star x$. The laws decide which classical structure the product defines, and the reading of the twelve one by one is *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### The Relativity of the Definitions

Every class below is defined by an equation whose symbol is the product, so the product is part of the definition and not a background convention.

**Principle (relativity).** Let $\star$ be a product and let $\mathcal E_\star(x)$ be any equation in the element $x$ whose only operation is $\star$ and whose constants are fixed elements or scalars. The class of solutions of $\mathcal E_\star$ depends on $\star$: replacing the product replaces the equation and can replace the class.

The definitions of this article are all of that form — $\tilde Q\star\tilde R=0$ for the zero divisor, $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ for the idempotent, $\tilde\Upsilon\star\tilde\Upsilon=0$ for the nilpotent, and so on — and none of them is a property of the element alone. The word is therefore always read with *of*: a zero divisor **of** $\star$, an idempotent **of** $\star$. Two products may select the same class and two may not, and when they do not the difference is a computation, of which §9 gives the table for the four general products.

### Transport Along an Isomorphism

The relativity has one structural counterpart, which is why two products may share a class without sharing the equation.

**Proposition (transport).** Let $\star$ and $\star'$ be two products on $\mathbb{B}$ and let $\theta$ be a bijection of $\mathbb{B}$ with
$$
\theta(x\star y)=\theta(x)\star'\theta(y) \qquad\text{for all } x,y .
$$
Then $\theta$ carries every class of §2 to §5 from $\star$ onto the corresponding class of $\star'$: the $\star$-units onto the $\star'$-units, the $\star$-invertible elements onto the $\star'$-invertible elements with $\theta(x^{-1})=\theta(x)^{-1}$, the $\star$-idempotents onto the $\star'$-idempotents, the $\star$-nilpotents onto the $\star'$-nilpotents, and the $\star$-zero divisors onto the $\star'$-zero divisors.

**Proof.** Apply $\theta$ to the defining equation and use multiplicativity. If $x\star x=x$ then $\theta(x)\star'\theta(x)=\theta(x\star x)=\theta(x)$; if $x\star x=0$ then $\theta(x)\star'\theta(x)=\theta(0)=0$; if $x\star y=0$ with $x,y\neq0$ then $\theta(x)\star'\theta(y)=0$ with $\theta(x),\theta(y)\neq0$; and if $e$ is a unit of $\star$ then $\theta(e)\star'\theta(x)=\theta(e\star x)=\theta(x)$ and $\theta(x)\star'\theta(e)=\theta(x)$, so $\theta(e)$ is a two-sided unit of $\star'$, from which $x\star y=y\star x=e$ gives $\theta(x)\star'\theta(y)=\theta(e)$. $\square$

Two products related by such a $\theta$ have the same element theory up to $\theta$, and the definitions of this article cannot separate them. Two products not so related may differ on every class, which is what §9 computes for the four general products. The relations among the four general products under the conjugations, and the question of which pairs are isomorphic in this sense, are *Relations Between the Four General Products*.

---

## 2. The Unit and the Inverse

**Definition (unit of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star x=x$ for every $x$; a **right unit of $\star$** when $x\star e=x$ for every $x$; and a **two-sided unit of $\star$**, or an **identity of $\star$**, when it is both. A product that has a two-sided unit is **unital**. A two-sided unit, when it exists, is unique.

**Definition (inverse).** Let $\star$ be a product with a two-sided unit $e$. An element $x$ is **left-invertible of $\star$** when there is $y$ with $y\star x=e$; **right-invertible** when there is $y$ with $x\star y=e$; and **invertible of $\star$** when there is $y$ with $x\star y=y\star x=e$. Such a $y$ is an **inverse of $x$ of $\star$**, written $x^{-1}$. In an associative unital product the inverse is unique and the invertible elements form the **group of units**.

The inverse is defined by an equation in $\star$, so it is relative to the product in the same way as the classes of §3 to §5: the inverse element of $x$ for one product is not the inverse for another, and the symbol $x^{-1}$ is read only with the product in force.

**The four general products.** Only one of the four has a two-sided unit.

| product | left unit | right unit | two-sided unit |
|---|---|---|---|
| $\tilde P\tilde Q$ | $e_0$ | $e_0$ | $e_0$ |
| $\tilde P^{\natural}\tilde Q$ | $e_0$ | none | none |
| $\tilde P\tilde Q^{*}$ | none | $e_0$ | none |
| $\tilde P^{\natural}\tilde Q^{*}$ | none | none | none |

The table is verified on the identity equations and it is the unit table of *Comparison Between the Four General Products*. Three of the four products are therefore not unital, and for them the group of units is not available; what survives is the one-sided inverse, and its equations are in *The Zero Divisors and the Four General Products*, §*The One-Sided Inverse Equations*.

The general reading, for an associative unital algebra, is *Unital Algebras*; the invertibility criterion of the plain product, $\tilde P$ invertible exactly when the central square $c(\tilde P)=\sum_\mu P_\mu^{2}$ is nonzero, is *Biquaternion Norm and Invertibility*.

---

## 3. The Zero Divisor and the Annihilator

**Definition (zero divisor of a product).** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde Q\in\mathbb{B}$. The element $\tilde Q$ is a **left zero divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R=0$; a **right zero divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde R\star\tilde Q=0$; and a **zero divisor of $\star$** when it is one or the other. It is a **two-sided zero divisor of $\star$** when it is both.

Both elements are required to be nonzero, and that is essential: the origin is not a zero divisor of any product, even though $0\star\tilde R=0$ for every $\tilde R$.

**Definition (annihilator).** Let $\star$ be a product and let $\tilde Q$ be a zero divisor of $\star$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in $\star$ are the sets
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
They are the kernels of the two one-sided multiplications of §7, they are nonzero exactly when $\tilde Q$ is a zero divisor of the corresponding side, and an element is a two-sided zero divisor exactly when both are nonzero.

**Definition (regular element).** An element of a unital product that is neither a left nor a right zero divisor is **regular**.

Written on the four general products, the definition of a left zero divisor is one of $\tilde Q\tilde R=0$, $\tilde Q^{\natural}\tilde R=0$, $\tilde Q\tilde R^{*}=0$, $\tilde Q^{\natural}\tilde R^{*}=0$, and the definition of a right zero divisor is the same with the factors exchanged. The eight equations are the four definitions, and the equation is the whole of the definition. For the biquaternion algebra the four definitions select one and the same set,
$$
\{\tilde Q\neq0:\ c(\tilde Q)=0\},
$$
a fact about the algebra and not a property of the definitions, proved in *The Zero Divisors and the Four General Products*, §*The Four Zero-Divisor Sets Coincide*. **The word is *coincide*, not *independent*:** the four products are four definitions, and their agreement is a theorem. The criterion $c(\tilde Q)=0$ for the plain product, the two families and their structure are *Zero Divisors of the General Plain Algebra*; the annihilators of one zero divisor, which do depend on the product, are in the same article of the four products and in *The Annihilating Elements of the Four General Products*.

---

## 4. The Idempotent, the Projection and the Peirce Decomposition

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Pi$ is an **idempotent of $\star$** when
$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi .
$$
The origin and, when the product is unital, the unit are idempotents of every product: they are the **trivial idempotents**, and the others are **nontrivial**. The set of the idempotents of $\star$ is its **idempotent set**.

**Definition (orthogonal, complete, primitive).** Idempotents $\tilde\Pi,\tilde\Pi'$ of an associative product are **orthogonal** when $\tilde\Pi\star\tilde\Pi'=\tilde\Pi'\star\tilde\Pi=0$; a family is **pairwise orthogonal** when $\tilde\Pi_i\star\tilde\Pi_j=0$ for $i\neq j$, and **complete** when in addition $\sum_i\tilde\Pi_i$ is the unit. A nontrivial idempotent is **primitive** when it is not the sum of two nonzero orthogonal idempotents, and for a semisimple algebra $\tilde\Pi$ is primitive exactly when $\tilde\Pi\star\mathbb{B}\star\tilde\Pi$ is a division ring.

**Definition (projection).** When the product is the multiplication of a $*$-algebra, an idempotent $\tilde\Pi$ with $\tilde\Pi^{*}=\tilde\Pi$ is a **projection**; with the plain product and the star, the projections are the **orthogonal projections**, and the associated decomposition of §*The Peirce Decomposition* is an orthogonal direct sum.

**Definition (Peirce decomposition).** Let the product be associative with unit, and let $\tilde\Pi$ be an idempotent. The **Peirce decomposition** of the algebra relative to $\tilde\Pi$ is the splitting of the regular module into the four pieces indexed by the pair $(\tilde\Pi,1-\tilde\Pi)$; its two diagonal pieces are the **corner algebras** $\tilde\Pi\star\mathbb{B}\star\tilde\Pi$ and $(1-\tilde\Pi)\star\mathbb{B}\star(1-\tilde\Pi)$.

The idempotent is the root of $+1$ in the scaled sense of §6, and the idempotent sets of the four general products differ: the plain product has the family $\tfrac12(e_0+\xi i)$ over the roots $\xi$ of $-1$, the natural product has the trivial idempotents alone, the plain sesquilinear product has the Hermitian idempotents, and the quaternionic sesquilinear product has the family $-\tfrac12e_0+\mu$. The table is in *The Zero Divisors and the Four General Products*, §*The Square, the Idempotents and the Units*; the classification for the plain product is *Idempotents of the General Plain Algebra*, the general theory is *Unital Algebras*, and the Peirce decomposition of the biquaternion algebra is *Biquaternion Ideals and Peirce Decomposition*.

---

## 5. The Nilpotent

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Upsilon$ is **nilpotent of $\star$** when some power of it vanishes,
$$
\tilde\Upsilon^{\star k}=0 \quad\text{for some } k\geq1 ,
$$
the power being read in the sense of §6. The least such $k$ is the **index of nilpotency**, and an element of index two, $\tilde\Upsilon\star\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, is a **square-zero element of $\star$**. The origin is a nilpotent, the trivial one, and the article is concerned with the others.

The nilpotent is the root of $0$ in the sense of §6. In the plain product the index is two or nothing — an element with vanishing cube already has vanishing square, so the nonzero nilpotents there are exactly the square-zero elements (*Nilpotents of the General Plain Algebra*) — but the index is not bounded by two in every product of the twelve, and the square-zero element is the case the comparison of the four general products is made in.

The square-zero sets of the four general products differ, and the difference is sharp.

| product | square-zero elements |
|---|---|
| $\tilde P\tilde Q$ | the pure isotropic cone $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$ |
| $\tilde P^{\natural}\tilde Q$ | the whole zero-divisor cone $\{c=0\}$ |
| $\tilde P\tilde Q^{*}$ | the origin alone |
| $\tilde P^{\natural}\tilde Q^{*}$ | the solutions of $\overline{\tilde P}\tilde P=0$ |

The table is verified on the squares and is the table of *The Square-Zero Elements of the Four General Products*, where the four sets, their chain $Z_1\subseteq Z_2$, $Z_4\subseteq Z_2$, $Z_3=\{0\}$ and their incomparable pair are proved. **The implication "nilpotent implies zero divisor" is not uniform**: it holds for the plain product and the natural product, and it fails for the plain sesquilinear product, whose only square-zero element is the origin. It is a statement of a product and not of the twelve.

---

## 6. Powers, the Square and the Roots

**Definition (power).** Let $\star$ be a product. The **square** of an element is $\tilde P^{\star2}=\tilde P\star\tilde P$. When $\star$ is associative the higher powers are unambiguous, $\tilde P^{\star k}=\tilde P\star\cdots\star\tilde P$, and they obey $\tilde P^{\star(i+j)}=\tilde P^{\star i}\star\tilde P^{\star j}$; when $\star$ is not associative the notation needs a bracketing, and the **left-nested reading** is $\tilde P^{\star k}=\bigl(\cdots\bigl((\tilde P\star\tilde P)\star\tilde P\bigr)\cdots\star\tilde P\bigr)$. Of the four general products only the plain one is associative, so only there is $\tilde P^{\star k}$ bracketing-free.

**Definition (root of a central value).** Let $\lambda\in\mathbb{C}$. A **root of $\lambda$ in $\star$** is a nonzero element with
$$
\tilde P\star\tilde P=\lambda e_0 .
$$
The three central values the biquaternion algebra singles out are $-1$, $+1$ and $0$: the roots of $-1$ are the imaginary units, the roots of $+1$ are the involutions, and the roots of $0$ are the nonzero nilpotents of §5.

**Definition (square root of an element).** For an element $a\in\mathbb{B}$, a **square root of $a$ in $\star$** is an element with $\tilde P\star\tilde P=a$; the roots of a central value are the special case $a=\lambda e_0$.

The reading of the roots of $-1$, of $0$ and of $+1$ in the plain product, and the classification of the roots of a general element, are *Biquaternion Square Roots of Minus One, Zero and Plus One* and *Biquaternion Square Roots of a General Element*. The idempotents of §4 are the roots of $+1$ halved: the map $\xi\mapsto\tfrac12(e_0+\xi)$ carries the roots of $+1$ onto the idempotents of the plain product, and the nilpotents of §5 are the roots of $0$.

---

## 7. The Derived Operations

**Definition (the commutator and the symmetrisation).** For a product $\star$,
$$
[x,y]_\star=x\star y-y\star x , \qquad x\circ_\star y=x\star y+y\star x ,
$$
and the **symmetric part** and the **antisymmetric part** of the product are $\tfrac12(x\star y+y\star x)$ and $\tfrac12(x\star y-y\star x)$. Each of the four general products splits into its two parts, and the split is the source of the twelve: four general products, three operations to a family. The method and the class-preserving exchange are *The Symmetric and Antisymmetric Parts of an Algebra Product* and *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

**Definition (the associator and the ternary product).** For a product $\star$,
$$
(x,y,z)_\star=(x\star y)\star z-x\star(y\star z)
$$
is the **associator**, and the **ternary product** is the trilinear operation $x\star y\star z$ read with the same bracketing. The product is associative exactly when the associator vanishes identically, so the associator is the obstruction to associativity and, through it, to the unambiguous power of §6.

**Definition (the two identities).** The **Jacobi identity** and the **Jordan identity** of §1 are the statements that single out the two classical non-associative structures among the twelve; the two, their witnesses and the failure of the other six parts are *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Two That Are Lie and Jordan Products*, and *Jordan Algebras*.

**Definition (left and right multiplication).** For $a\in\mathbb{B}$,
$$
L_a^{\star}(x)=a\star x , \qquad R_a^{\star}(x)=x\star a .
$$
They are the two one-sided multiplications of §3, their kernels are the two annihilators, and their composition measures the failure of associativity and of multiplicativity. **Definition (sandwich).** For a product with a two-sided unit and an involution, the **sandwich** of $a$ is the two-sided operator $x\mapsto a\star x\star a^{*}$. The operators of the biquaternion algebra are *Two-Sided Operators on the General Plain Algebra of Biquaternions*, *One-Sided Operators on the General Plain Algebra of Biquaternions* and *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*.

**Definition (derivation).** An operator $D$ on $\mathbb{B}$ is a **derivation of $\star$** when $D(x\star y)=Dx\star y+x\star Dy$ for all $x,y$.

---

## 8. The Form-Theoretic Classes

The classes so far are those of the multiplication alone. The structures also carry forms and norms, and the definitions they use are collected here in the same product-relative spirit; the forms themselves are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* and the norms *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*.

**Definition (centre and commutant).** The **commutant** of a subset $S\subseteq\mathbb{B}$ in a product $\star$ is $\{x: x\star s=s\star x\ \text{for all }s\in S\}$; the **centre** is the commutant of the whole space. For the plain product the centre is the scalar line $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ (*Introduction to the General Plain Algebra of Biquaternions*).

**Definition (isotropic element, radical).** Let $\langle\cdot,\cdot\rangle$ be a form on $\mathbb{B}$. An element is **isotropic** for the form when $\langle x,x\rangle=0$, and the **radical** is the set of elements orthogonal to the whole space. The isotropic elements of the four forms are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, and the isotropic cone of the quaternionic product is *The Isotropic Structure of the General Quaternionic Algebra*.

**Definition (adjoint, Hermitian, normal).** Let $\langle\cdot,\cdot\rangle$ be a form with an involution ${}^{*}$. The **adjoint of $a$** is the element $a^{\dagger}$ with $\langle a\star x,y\rangle=\langle x,a^{\dagger}\star y\rangle$; an element is **Hermitian** when $a^{\dagger}=a$, **anti-Hermitian** when $a^{\dagger}=-a$, and **normal** when $a\star a^{\dagger}=a^{\dagger}\star a$. The four adjoints of the two algebras and the two sesqualgebras are worked in *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*; the trace form is *The Trace Form and the Invariance of the Symmetric Plain Algebra*, and the invariant form of the antisymmetric product is *The Killing Form of the Antisymmetric Plain Algebra*.

---

## 9. The Dictionary: The Classes and the Four General Products

The four general products are four definitions to a class, and the table says which of the four agree. The entry *coincide* means that the four definitions select one and the same subset of $\mathbb{B}$; *differ* means that they do not, and the specializing article carries the sets.

| class of §  | $\tilde P\tilde Q$ | $\tilde P^{\natural}\tilde Q$ | $\tilde P\tilde Q^{*}$ | $\tilde P^{\natural}\tilde Q^{*}$ | verdict |
|---|---|---|---|---|---|
| unit | $e_0$ two-sided | left only | right only | none | differ |
| zero divisor | $\{c=0\}\setminus\{0\}$ | same | same | same | **coincide** |
| idempotent | $\tfrac12(e_0+\xi i)$ | the trivial pair | the Hermitian ones | $-\tfrac12e_0+\mu$ | differ |
| square-zero | the pure cone | the whole cone | $\{0\}$ | $\{\overline{\tilde P}\tilde P=0\}$ | differ |
| annihilator of a fixed zero divisor | one plane | another | another | another | differ |
| invertibility | $c\neq0$ | no two-sided notion | no two-sided notion | no two-sided notion | — |

The one row on which the four products agree is the zero-divisor set. It is the reason the zero divisor is the subject of a synthesis article of its own, *The Zero Divisors and the Four General Products*, and it is the exception that proves the rule of §*The Relativity of the Definitions*: the definitions are four, and their agreement in this one row is a theorem about the biquaternion algebra, not a feature of the definitions. Every other row shows the four products separating, and each is computed in *The Annihilating Elements of the Four General Products* and *Comparison Between the Four General Products*.

---

## Summary

A definition of the element theory names a product. This article states, once and for a general product $\star$, the unit and the inverses of a product; the left, right and two-sided zero divisor and the two annihilators; the idempotent, its orthogonal, complete and primitive families and the projection; the nilpotent, its index and the square-zero element; the powers and their bracketing, the root of a central value and the square root of an element; the commutator and the symmetrisation with the two parts of a product; the associator and the ternary product with the two classical identities; the left and right multiplications, the sandwich and the derivation; and the centre, the commutant, the isotropic element, the radical and the adjoint. Each is then read on the products of the space, and the dictionary of §9 records that the zero-divisor set is the single row on which the four general products agree, while the units, the idempotents, the square-zero elements and the annihilators separate them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\star$ | a general product, one of the twelve, with the class of §1 |
| $\tilde P\tilde Q$ | the general plain bilinear product, the multiplication of the algebra |
| $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q^{*}$ | the other three general products |
| $e$ | a unit; left, right or two-sided, per §2 |
| $x^{-1}$ | the inverse of $x$, read in the product in force |
| $c(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, deciding the zero divisor of the plain product |
| $A_\star(\tilde Q),B_\star(\tilde Q)$ | the left and the right annihilator of $\tilde Q$ in $\star$ |
| $\tilde\Pi$ | an idempotent; $\tilde\Pi^{*}=\tilde\Pi$ makes it a projection |
| $\tilde\Upsilon$ | a nilpotent of the plain product; index two, hence square-zero |
| $[x,y]_\star$, $x\circ_\star y$ | the commutator and the symmetrisation of $\star$ |
| $(x,y,z)_\star$ | the associator of $\star$ |
| $L_a^{\star},R_a^{\star}$ | the left and the right multiplication by $a$ in $\star$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre of the plain product |

## Further Reading

- *The 12 Products of the Biquaternion Complex Space* and *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, for the products and the structures the definitions here serve, and for the tables of the laws, the units and the images.
- *The Zero Divisors and the Four General Products*, for the product-relative definition read on the four products, the coincidence of the four zero-divisor sets, and the product-dependent readings of the annihilators, the square, the idempotents and the units.
- *Zero Divisors of the General Plain Algebra*, *Idempotents of the General Plain Algebra* and *Nilpotents of the General Plain Algebra*, for the three element classes of the plain product.
- *The Square-Zero Elements of the Four General Products* and *The Annihilating Elements of the Four General Products*, for the two readings of §5 and §9 that the four products decide.
- *Unital Algebras* and *Conventions in Mathematics*, for the general algebra vocabulary and the corpus-wide readings of the words, and *Biquaternions as a Vector Space over $\mathbb{C}$* for the elements and the conjugations.
