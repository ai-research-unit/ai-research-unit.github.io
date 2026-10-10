# __The Four General Products and Their Two Slots: the Two Algebras and the Two Sesqualgebras__

## Introduction

The underlying complex vector space of $\mathbb{B}$ carries four general products, and the category studies them as four objects: the two whose second argument is read without a conjugation are named *algebras over $\mathbb{C}$*, and the two whose second argument carries one are named *sesqualgebras over $\mathbb{C}$*. *The Four General Products of the Biquaternion $\mathbb{C}$ Space* introduces the four independently on the coordinates of the two arguments, *Relations Between the Four General Products* relates them by conjugating one or the other factor, and *Comparison Between the Four General Products* compares them by their algebraic properties. This article is the map of that material. It exhibits the four general products as the four settings of **one** construction, and it derives the division of the four objects into two and two from that construction instead of reading it off the four definitions.

The construction is that each product reads its two arguments through the involutions of the algebra, independently. Write the product as $x\star y=K_1(x)K_2(y)$: the **first slot** $K_1$ takes the identity or the natural conjugation ${}^{\natural}$, the **second slot** $K_2$ the identity or the Hermitian conjugation ${}^{*}$, and the four general products of the corpus are the four settings. §*The Four General Products in Coordinates* writes the four out on the coordinates first, and the construction is read on them afterwards. The result of the article is that **the two slots decide different properties, and each slot decides a whole family of them.** The second slot decides whether the operation is bilinear or sesquilinear, whether the unit acts as a left unit, and whether the left multiplications compose. The first slot decides whether the unit acts as a right unit and whether the induced form is definite on each sector, and it toggles the coefficient $\varepsilon$ of the scalar part. Since the second slot toggles $\varepsilon$ as well, the coefficient survives in a given setting exactly when the two slots agree, so that one property is carried by the two slots together. Both slots together decide associativity, and it fails unless both are trivial.

The two-and-two of the category follows at once. The second slot is exactly what separates an algebra over $\mathbb{C}$ from a sesqualgebra over $\mathbb{C}$, so the four names track the **second** slot, and the adjective *quaternionic* in two of them records the **first**. §*The Two Algebras and the Two Sesqualgebras* states this.

The article is the algebra companion of *The Four Pairings of the Biquaternion Algebra*. That article settles a question about the four **forms** and about the norms read from them; this one settles a question about the four **products** and finds one construction. It cites *Comparison Between the Four General Products* for the property table and its companion for the Gram matrices and the signatures, *Introduction to the General Plain Sesqualgebra of Biquaternions* and *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* for the derived operation and the isotope, and *Algebras* and *Sesqualgebras* for the two kinds of structure. **No physics is invoked.**

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$ satisfying $e_k^{2}=-e_0$ and $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and with central scalar imaginary $i$. A general element is $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The conjugations are the natural conjugation $J={}^{\natural}$, which is $\mathbb{C}$-linear and negates the three vector units, the complex conjugation $c=\bar{\cdot}$, which is conjugate-linear and fixes the units, and their composites, the Hermitian conjugation ${}^{*}=c\circ{}^{\natural}={}^{\natural}\circ c$ and $\flat=-{}^{*}$; all four commute. The four general products are

$$
\tilde{P}\tilde{Q},\qquad \tilde{P}^{\natural}\tilde{Q},\qquad \tilde{P}\tilde{Q}^{*},\qquad \tilde{P}^{\natural}\tilde{Q}^{*}.
$$

The scalar part is $\mathrm{Sc}(\tilde{Q})=Q_0$, and for a product of two elements the scalar part is $\mathrm{Sc}(\tilde{P}\tilde{Q})=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ with $\varepsilon=(1,-1,-1,-1)$. The Gram matrix of a form is written in the basis $e_0,e_1,e_2,e_3$, so that $\mathrm{E}=\mathrm{diag}(1,-1,-1,-1)$ and $\mathrm{I}_4$ are the two matrices that occur. The real coordinates are $Q_\mu=q_\mu+iq'_\mu$; the **Hermitian subspace** $\mathbb{M}_+$ and the **anti-Hermitian subspace** $\mathbb{M}_-$ are the fixed spaces of ${}^{*}$ and of $\flat=-{}^{*}$, real subspaces of dimension four (*The Six Subspaces and the Four General Products*), and a form is called **definite on a sector** when it is definite as a real form on each of them.

## The Four General Products in Coordinates

This section writes the four out on the coordinates, which is the form in which *The Four General Products of the Biquaternion $\mathbb{C}$ Space* states them and the form the reader meets before the slot language of §*The Two Slots*; the same four are read there as the four settings of one construction. An element is $\tilde P=P_0e_0+P_1e_1+P_2e_2+P_3e_3$ with $P_\mu\in\mathbb{C}$, its scalar part is $\mathrm{Sc}(\tilde P)=P_0$ and its vector part is $\mathbf P=P_1e_1+P_2e_2+P_3e_3$. The natural conjugation reverses the sign of the three vector coordinates, and the star does the same and conjugates the coefficients:

$$
\tilde P^{\natural}=P_0e_0-P_1e_1-P_2e_2-P_3e_3,\qquad \tilde P^{*}=\overline{P_0}e_0-\overline{P_1}e_1-\overline{P_2}e_2-\overline{P_3}e_3 ,
$$

which in the sign vector $\varepsilon=(1,-1,-1,-1)$ is $\tilde P^{\natural}_\mu=\varepsilon_\mu P_\mu$ and $P^{*}_\mu=\varepsilon_\mu\overline{P_\mu}$. Each of the four general products multiplies the coordinates of the two factors on the basis of the units, the first factor read plain or through ${}^{\natural}$ and the second plain or through ${}^{*}$, the two choices independent; with the sums over $\mu,\nu=0,\dots,3$,

$$
\tilde P\tilde Q=\sum_{\mu,\nu}P_\mu Q_\nu\,e_\mu e_\nu,\qquad \tilde P^{\natural}\tilde Q=\sum_{\mu,\nu}\varepsilon_\mu P_\mu Q_\nu\,e_\mu e_\nu,
$$
$$
\tilde P\tilde Q^{*}=\sum_{\mu,\nu}\varepsilon_\nu P_\mu\overline{Q_\nu}\,e_\mu e_\nu,\qquad \tilde P^{\natural}\tilde Q^{*}=\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu P_\mu\overline{Q_\nu}\,e_\mu e_\nu .
$$

Their scalar parts are the four forms the rest of the article reads, and written out term by term they are

$$
\begin{aligned}
\mathrm{Sc}(\tilde P\tilde Q)&=\textstyle\sum_\mu\varepsilon_\mu P_\mu Q_\mu=P_0Q_0-P_1Q_1-P_2Q_2-P_3Q_3,\\
\mathrm{Sc}(\tilde P^{\natural}\tilde Q)&=\textstyle\sum_\mu P_\mu Q_\mu=P_0Q_0+P_1Q_1+P_2Q_2+P_3Q_3,\\
\mathrm{Sc}(\tilde P\tilde Q^{*})&=\textstyle\sum_\mu P_\mu\overline{Q_\mu}=P_0\overline{Q_0}+P_1\overline{Q_1}+P_2\overline{Q_2}+P_3\overline{Q_3},\\
\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})&=\textstyle\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}=P_0\overline{Q_0}-P_1\overline{Q_1}-P_2\overline{Q_2}-P_3\overline{Q_3}.
\end{aligned}
$$

The first is the general plain bilinear form, the second the general quaternionic bilinear, the third the general plain sesquilinear and the fourth the general quaternionic sesquilinear; the four leading expressions are the *scalar part* column of the table of *The Four Pairings of the Biquaternion Algebra*, and the vector parts, that is the remaining coordinates of the four general products, are displayed product by product in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*.

## The Two Slots

**Definition (the slot family).** Let $A$ be a unital associative $\mathbb{C}$-algebra, and let $\natural$ and $\varsigma$ be involutive anti-automorphisms of $A$ that commute, with $\natural$ $\mathbb{C}$-linear and $\varsigma$ conjugate-linear, and with $\natural(1)=\varsigma(1)=1$. For $K_1\in\{\mathrm{id},\natural\}$ and $K_2\in\{\mathrm{id},\varsigma\}$ put

$$
x\star_{K_1K_2}y=K_1(x)\,K_2(y).
$$

The **first slot** is $K_1$ and the **second slot** is $K_2$. In $\mathbb{B}$ one takes $A=\mathbb{B}$, $\natural$ the natural conjugation and $\varsigma={}^{*}$ the Hermitian conjugation, and the four settings of the definition are then the four general products of §*Conventions*, in the order $(\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},{}^{*})$.

The four settings are collected in the grid, which is the article's object of study.

| | $K_2=\mathrm{id}$ | $K_2={}^{*}$ |
|---|---|---|
| $K_1=\mathrm{id}$ | the plain product $\tilde{P}\tilde{Q}$ | the general plain sesquilinear product $\tilde{P}\tilde{Q}^{*}$ |
| $K_1={}^{\natural}$ | the quaternionic product $\tilde{P}^{\natural}\tilde{Q}$ | the general quaternionic sesquilinear product $\tilde{P}^{\natural}\tilde{Q}^{*}$ |

**Remark (why the family has four members and not sixteen).** The involutions at hand are four — $\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}$ — so a two-slot construction over them would a priori have sixteen settings. The four general products of the corpus use only $\mathrm{id}$ or ${}^{\natural}$ in the first slot and only $\mathrm{id}$ or ${}^{*}$ in the second. Two features of that choice matter below. First, the first slot is $\mathbb{C}$-linear, so it never conjugates the coefficients, while the second slot is conjugate-linear whenever it is not the identity; this is the asymmetry that makes the two slots not interchangeable, and it is the source of every entry of the table of §*The Slot Calculus*. Second, the choice of the two conjugations is not free but is the one that produces the classification of §*The Two Algebras and the Two Sesqualgebras*, in which the second slot alone decides the kind of structure. The articles of the corpus state the four general products directly; this article asserts nothing about the other twelve settings, and every statement below is about these four.

**Remark (the two rows are the first slot, the two columns the second).** The upper row of the grid carries no ${}^{\natural}$ and the lower row carries it; by §*The Slot Calculus* that single difference decides whether the unit is a right unit and whether the induced form is definite on a sector, and it toggles the coefficient $\varepsilon$, which the second slot toggles as well, so that $\varepsilon$ survives exactly when the two slots agree. The left column has no ${}^{*}$ and the right column has it; that single difference decides whether the operation is bilinear or sesquilinear. **The rows and the columns are the two slots, and each slot is one binary choice.**

## The Slot Calculus

The properties of the four general products need not be checked one at a time. Each is decided by one slot, by both, or by singling out one setting, and the rules are theorems about the slot family of §*The Two Slots* rather than facts about $\mathbb{B}$ alone. Two of the three rules below are stated in that generality and one is not, and the distinction is marked.

**Theorem (the second slot rules the composition).** With $A$, $\natural$, $\varsigma$ as in §*The Two Slots*, let $K_1\in\{\mathrm{id},\natural\}$, $K_2\in\{\mathrm{id},\varsigma\}$ and $x\star y=K_1(x)K_2(y)$. Then the following four statements are equivalent.

- $K_2=\mathrm{id}$.
- $\star$ is $\mathbb{C}$-bilinear in its second argument.
- $1$ is a left unit for $\star$: $1\star x=x$ for every $x$.
- The left multiplications $L_x:x\mapsto x'\mapsto x\star x'$ of $\star$ are closed under composition.

When they hold, $L_x\circ L_y=L_{xy}$ if $K_1=\mathrm{id}$ and $L_x\circ L_y=L_{yx}$ if $K_1={}^{\natural}$, so the monoid of left multiplications is $A$ in the first case and the opposite monoid of $A$ in the second — for the quaternionic product the detailed study is *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*. When they fail, $L_x\circ L_y$ is $\mathbb{C}$-linear in its argument while every $L_z$ is conjugate-linear, so the composition is not a left multiplication at all, and it is non-zero for non-zero $x$ and $y$.

**Proof.** ($K_2=\mathrm{id}$ implies bilinear.) $x\star(\lambda y)=K_1(x)\lambda y=\lambda(K_1(x)y)=\lambda(x\star y)$. ($K_2=\mathrm{id}$ implies left unit.) $1\star x=K_1(1)x=x$, since $\natural(1)=1$. ($K_2=\mathrm{id}$ implies closure.) $L_x\circ L_y(x')=K_1(x)K_1(y)x'$. If $K_1=\mathrm{id}$ this is $(xy)x'=L_{xy}(x')$; if $K_1={}^{\natural}$ it is $\natural(x)\natural(y)x'=\natural(yx)x'=L_{yx}(x')$, the middle step because $\natural$ is an anti-automorphism.

(Bilinear implies $K_2=\mathrm{id}$.) Suppose $K_2=\varsigma$. Then $1\star(\lambda\cdot1)=K_1(1)\varsigma(\lambda)=\bar{\lambda}\varsigma(1)=\bar{\lambda}$, while $\lambda(1\star1)=\lambda$, and $\bar{\lambda}=\lambda$ fails for $\lambda=i$. So $\star$ is not $\mathbb{C}$-bilinear in the second argument, and it is linear in the first, since $K_1$ is: $(\lambda x)\star y=K_1(\lambda x)K_2(y)=\lambda\left(K_1(x)K_2(y)\right)$.

(Left unit implies $K_2=\mathrm{id}$.) Suppose $K_2=\varsigma$ and $1\star x=x$ for all $x$. Then $\varsigma(x)=K_1(1)^{-1}x=x$, so $\varsigma=\mathrm{id}$ against hypothesis; the same conclusion follows from comparing the conjugate-linear left side with the linear right side.

(Closure implies $K_2=\mathrm{id}$.) Suppose $K_2=\varsigma$. Then

$$
(L_x\circ L_y)(x')=K_1(x)\,\varsigma\!\left(K_1(y)\,\varsigma(x')\right)=K_1(x)\,x'\,\varsigma(K_1(y)),
$$

using that $\varsigma$ is an involution and an anti-automorphism. The right-hand side is $\mathbb{C}$-linear in $x'$, while $L_z(x')=K_1(z)\varsigma(x')$ is conjugate-linear, and no non-zero map is both. For $x,y\neq0$ the composition is non-zero, so it is not a left multiplication. $\square$

**Theorem (the first slot rules the right unit).** With the hypotheses and notation of the previous theorem, $1$ is a right unit for $\star$ if and only if $K_1=\mathrm{id}$.

**Proof.** $x\star1=K_1(x)K_2(1)=K_1(x)$, since $\varsigma(1)=1$. This equals $x$ for every $x$ if and only if $K_1=\mathrm{id}$. $\square$

**Theorem (associativity requires both slots trivial, in $\mathbb{B}$).** In $\mathbb{B}$ the product $\star_{K_1K_2}$ is associative if and only if $K_1=\mathrm{id}$ and $K_2=\mathrm{id}$.

**Proof.** One direction is trivial: $\star_{\mathrm{id}\,\mathrm{id}}$ is the multiplication of the associative algebra $\mathbb{B}$. For the converse, take first $K_2=\mathrm{id}$ and $K_1={}^{\natural}$. Then $(x\star y)\star z=\natural\!\left(\natural(x)y\right)z=\natural(y)\,x\,z$ while $x\star(y\star z)=\natural(x)\natural(y)z$, and at $x=y=e_1$, $z=e_0$ the two are $e_0$ and $-e_0$. Now take $K_2={}^{*}$. As a function of $z$ the left-nested term $(x\star y)\star z=K_1\!\left(K_1(x)\varsigma(y)\right)\varsigma(z)$ is conjugate-linear, while the right-nested term

$$
x\star(y\star z)=K_1(x)\,\varsigma\!\left(K_1(y)\,\varsigma(z)\right)=K_1(x)\,z\,\varsigma(K_1(y))
$$

is $\mathbb{C}$-linear, by the computation of the previous theorem; a map that is both must vanish, and the second one does not, being $z\mapsto z$ at $x=y=e_0$. $\square$

**Remark (associativity is the one rule of the three that is not general).** The two theorems above hold in any $A$ of §*The Two Slots*, because their proofs use only that $\varsigma$ is conjugate-linear and not linear and that $\natural$ is an anti-automorphism. Associativity does not. In a commutative algebra with $\natural=\varsigma=\mathrm{id}$ all four settings coincide and all four are associative, so no slot rule can be stated in that generality; the theorem is a statement about $\mathbb{B}$, and it is the statement the property table of *Comparison Between the Four General Products* already carries. It is proved here in the slot language because the proof is two lines of it and because it is the row that makes the two-sided unit unique.

### The Table of the Slots

The rules are collected in the table, with the entry that carries each property. The italic entries are the two that are special to $\mathbb{B}$.

| property of $\star_{K_1K_2}$ | decided by | the rule |
|---|---|---|
| $\mathbb{C}$-bilinear in the second argument | second slot | yes if and only if $K_2=\mathrm{id}$ |
| $e_0$ is a left unit | second slot | yes if and only if $K_2=\mathrm{id}$ |
| the left multiplications compose | second slot | yes if and only if $K_2=\mathrm{id}$ |
| $e_0$ is a right unit | first slot | yes if and only if $K_1=\mathrm{id}$ |
| the coefficient $\varepsilon$ survives in the scalar form | both slots | yes if and only if the two slots agree |
| the induced form is positive definite | exactly one setting | only at $(\mathrm{id},{}^{*})$ |
| the induced form is definite on each sector | first slot | yes if and only if $K_1=\mathrm{id}$ |
| $e_0$ is a two-sided unit | both slots | yes if and only if $K_1=K_2=\mathrm{id}$ |
| *associative* | both slots | yes if and only if $K_1=K_2=\mathrm{id}$ |
| *the square is scalar* | exactly one setting | only at $(K_1,K_2)=({}^{\natural},\mathrm{id})$ |

The first four rows are the slot reading of the property table of *Comparison Between the Four General Products*, whose columns are the four general products. The fifth is the coefficient $\varepsilon$, and the sixth and the seventh are the scalar form read, in turn, on the whole real space and on the two sectors $\mathbb{M}_-$ and $\mathbb{M}_+$ of dimension four. The eighth is the two unit rows together. The table is the article's central claim. It says that the second slot governs the **composition** — whether the operation can be iterated, whether the unit acts on the left, and whether the left multiplications form a monoid are one property of one slot — and that the first slot governs the **form** — whether the unit acts on the right, whether the induced form is definite on a sector, and, jointly with the second slot, whether the coefficient $\varepsilon$ survives. A product in the right-hand column is a pairing and not a composition, and no choice in the first slot repairs that.

**Remark (why the first slot rules definiteness on a sector).** On a sector every coordinate is real or purely imaginary: writing $Q_\mu=s_\mu r_\mu$ with $r_\mu$ real gives $s_\mu^{2}=-\varepsilon_\mu$ on $\mathbb{M}_-$ and $s_\mu^{2}=\varepsilon_\mu$ on $\mathbb{M}_+$, so **each sector contributes the sign pattern $\pm\varepsilon$**. A bilinear form contributes $\varepsilon_\mu$ when $K_1=\mathrm{id}$ and $1$ when $K_1={}^{\natural}$, so on a sector its signs are $\varepsilon_\mu(\pm\varepsilon_\mu)=\pm1$ in the first case — one and the same sign four times — and $\pm\varepsilon_\mu$ in the second, mixed. A sesquilinear form contributes $\lvert s_\mu\rvert^{2}=1$ and so sees no sector pattern at all, leaving the pattern $1$ when $K_1=\mathrm{id}$ and $\varepsilon_\mu$ when $K_1={}^{\natural}$. In every case the form is definite on each sector exactly when $K_1=\mathrm{id}$, and it is the sector's own pattern $\pm\varepsilon$ that makes the remaining settings indefinite on a sector.

**Corollary (which of the four have a unit, and on which side).** $e_0$ is a left unit for the two products whose second slot is trivial and a right unit for the two whose first slot is trivial. Hence exactly one of the four — the plain product — has a two-sided unit, the quaternionic product has a left unit and no right one, the general plain sesquilinear product has a right unit and no left one, and the general quaternionic sesquilinear product has no unit on either side.

**Remark (the two one-sided actions of the unit are the two conjugations).** For the general quaternionic sesquilinear product the two failures are explicit and are the two conjugations of the algebra:

$$
e_0\star\tilde{Q}=\tilde{Q}^{*},\qquad \tilde{Q}\star e_0=\tilde{Q}^{\natural}.
$$

The left action is ${}^{*}$ and the right action is ${}^{\natural}$, which is the statement of *The Two One-Sided Actions and the Absence of a Unit*, and the remark for the quaternionic product is in *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, §*The Two Actions of the Unit*.

### A Second Instance

The two slot rules are not a property of $\mathbb{B}$, and a second instance separates them from the coincidences of one algebra. Take $A=M_2(\mathbb{C})$, $\natural$ the transposition $T$ and $\varsigma$ the conjugate transposition, both of which are involutive anti-automorphisms and commute, and the unit $1=\mathrm{I}_2$. The four settings are $AB$, $A^TB$, $AB^{*}$ and $A^TB^{*}$, and the computation gives the following.

| product | associative | left unit | right unit | $\mathbb{C}$-linear in the 2nd argument |
|---|---|---|---|---|
| $AB$ | yes, residual $9.5\times10^{-16}$ | yes | yes | yes |
| $A^TB$ | no, residual $4.3$ | yes | no, residual $1.9$ | yes |
| $AB^{*}$ | no, residual $4.7$ | no, residual $2.0$ | yes | no, residual $8.9$ |
| $A^TB^{*}$ | no, residual $6.1$ | no, residual $2.0$ | no, residual $1.8$ | no, residual $5.8$ |

The pattern is the pattern of the table of §*The Table of the Slots*: bilinearity, the left unit and associativity follow the two columns, the right unit follows the two rows. The residuals are the maxima over random complex $2\times2$ matrices of the norm of the difference of the two sides, and "no" means a residual of order one, not a small multiple of the machine epsilon. **The slot rules of the two theorems therefore hold in this second algebra as well**, which is what the corollary of §*The Square, the Derived Operation and the Isotope* uses to isolate what does not.

## The Two Algebras and the Two Sesqualgebras

The four general products are the multiplications of four named structures, and the definitions of the two kinds are quoted here in the form the corpus uses.

**Definition (algebra over $\mathbb{C}$).** A **non-associative algebra over $\mathbb{C}$** is a $\mathbb{C}$-vector space with a product additive in each variable and $\mathbb{C}$-bilinear; associativity and a unit are not assumed.

**Definition (sesqualgebra over $\mathbb{C}$).** A **sesqualgebra over $\mathbb{C}$** is a $\mathbb{C}$-vector space with a product additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second, the base involution being the conjugation $\varsigma(z)=\bar{z}$:

$$
(\lambda x)\star y=\lambda(x\star y),\qquad x\star(\lambda y)=\bar{\lambda}(x\star y).
$$

Again associativity and a unit are not assumed. The two definitions are those of *Algebras* and *Sesqualgebras*, of which the four objects of the corpus are the two instances of each.

**Theorem (the second slot is the split).** With the notation of §*The Two Slots*, the product $\star_{K_1K_2}$ is the multiplication of an algebra over $\mathbb{C}$ if and only if $K_2=\mathrm{id}$, and of a sesqualgebra over $\mathbb{C}$ if and only if $K_2=\varsigma$.

**Proof.** $\mathbb{C}$-linearity in the first argument holds for all four settings because $K_1$ is $\mathbb{C}$-linear, and $\mathbb{C}$-linearity or conjugate-linearity in the second argument is the theorem of §*The Slot Calculus*. The two definitions differ in nothing else. $\square$

**Corollary (two and two, and the names track the second slot).** The four general products are the multiplications of exactly two algebra structures and two sesqualgebra structures on the underlying space of $\mathbb{B}$, the division being the column of the grid. The four named objects of the category are therefore indexed by the grid as follows; the adjective *quaternionic* records the first slot and nothing else.

| object | slot pair | first slot | second slot | maths anchor |
|---|---|---|---|---|
| *Introduction to the General Plain Algebra of Biquaternions* | $(\mathrm{id},\mathrm{id})$ | none | none | the multiplication of the associative algebra |
| *Introduction to the General Quaternionic Algebra of Biquaternions* | $({}^{\natural},\mathrm{id})$ | ${}^{\natural}$ | none | the $\natural$-isotope of the multiplication |
| *Introduction to the General Plain Sesqualgebra of Biquaternions* | $(\mathrm{id},{}^{*})$ | none | ${}^{*}$ | the derived operation of the algebra with ${}^{*}$ |
| *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* | $({}^{\natural},{}^{*})$ | ${}^{\natural}$ | ${}^{*}$ | the $\natural$-isotope of the derived operation |

**Remark (the first column and the second column are read differently).** The two entries of the first column are one algebra and one isotope of it, and the two entries of the second column are one derived operation and one isotope of it. §*The Square, the Derived Operation and the Isotope* states this precisely; the table records it in advance because it is the reason the four names are not four unrelated objects.

**Remark (what the two-and-two is not).** The division into two algebras and two sesqualgebras is not a division of the space, of the basis, or of the real form: all four are defined on one and the same $\mathbb{C}$-vector space of dimension four, with the same units $e_0,e_1,e_2,e_3$. It is a division of the four **products**, and it is the statement that $\mathbb{B}$ carries two associative-algebra readings and two sesqualgebra readings of its own underlying space.

## The Four Scalar Forms and the Two Marks

Each product induces a form, its scalar part, and the four forms are the subject of the four degree-2 form articles of the category. Their relation to the slots is exact and short.

**Theorem (the two marks).** For $\tilde{P},\tilde{Q}\in\mathbb{B}$ and a slot pair $(K_1,K_2)$,

$$
\mathrm{Sc}\!\left(K_1(\tilde{P})\,K_2(\tilde{Q})\right)
=\sum_{\mu=0}^{3}\varepsilon_\mu^{\,1-[K_1={}^{\natural}]}\,
P_\mu\,\left(K_2\tilde{Q}\right)_\mu ,
$$

in which the exponent is $0$ when $K_1={}^{\natural}$ and $1$ when $K_1=\mathrm{id}$. In the four settings the forms are therefore

$$
\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu,\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\sum_\mu P_\mu Q_\mu,\qquad
\langle\tilde{P},\tilde{Q}\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu},\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}.
$$

**Proof.** The scalar part of a product is $\mathrm{Sc}(XY)=\sum_\mu\varepsilon_\mu X_\mu Y_\mu$. Its first factor is $(K_1\tilde{P})_\mu=\varepsilon_\mu^{[K_1={}^{\natural}]}P_\mu$, because $\natural$ negates exactly the three vector coordinates and fixes the scalar one; its second factor is $(Q^{*})_\mu=\varepsilon_\mu\overline{Q_\mu}$ when $K_2={}^{*}$, and $Q_\mu$ when $K_2=\mathrm{id}$. Substituting,

$$
\mathrm{Sc}(K_1\tilde{P}\cdot K_2\tilde{Q})
=\sum_\mu\varepsilon_\mu\,\varepsilon_\mu^{[K_1={}^{\natural}]}P_\mu(K_2\tilde{Q})_\mu
=\sum_\mu\varepsilon_\mu^{\,1-[K_1={}^{\natural}]}P_\mu(K_2\tilde{Q})_\mu,
$$

using $\varepsilon_\mu^{2}=1$. The four settings are read off, and the identity $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ is the one the corpus writes $\langle\tilde{P},\tilde{Q}\rangle_{*}$. $\square$

**Corollary (the coefficient $\varepsilon$ survives when the two slots agree).** In the table of the theorem the coefficient is $\varepsilon_\mu$ for the plain product and for the general quaternionic sesquilinear product — the two settings in which the slots are equal, both trivial or both non-trivial — and it is $1$ for the general quaternionic bilinear and the general plain sesquilinear products, the two settings in which the slots differ. The general plain bilinear form and the general quaternionic sesquilinear form are the two forms whose coordinate expression carries the signature of the scalar part; the other two are the ones in which it has cancelled.

**Corollary (consequence for the Gram matrices and the signatures).** The Gram matrix of the form of $\star_{K_1K_2}$ is $\mathrm{E}$ when the two slots agree and $\mathrm{I}_4$ when they differ. In the real coordinates $Q_\mu=q_\mu+iq'_\mu$ the four forms have the real signatures

$$
(4,4),\qquad (4,4),\qquad (8,0),\qquad (2,6)
$$

for the general plain bilinear, general quaternionic bilinear, general plain sesquilinear and general quaternionic sesquilinear forms respectively, those of *The Four Pairings of the Biquaternion Algebra*. **The general plain sesquilinear form is the only positive definite one of the four**, and it is the setting whose first slot is trivial and whose second is not.

**Remark (what the signature separates and what it does not).** The signatures do not separate the four between them, and the Gram matrices of the previous corollary do not either: the two bilinear forms share the signature $(4,4)$ and the general plain bilinear form shares the Gram matrix $\mathrm{E}$ with the general quaternionic sesquilinear one. What separates the rows is the pair (Gram matrix, bilinearity), that is, the two slots read together, and this is the content of the comparison table of *The Four Pairings of the Biquaternion Algebra*, §*The Forms in Comparison*. The four **forms** are four readings of one algebra exactly as the four **products** are four settings of one construction.

## The Square, the Derived Operation and the Isotope

Two structural facts complete the map, and they are the ones that assign the four settings their places rather than merely their properties.

**Theorem (the square is scalar at exactly one setting).** In $\mathbb{B}$, $\tilde{Q}\star_{K_1K_2}\tilde{Q}$ is a scalar, that is, a multiple of $e_0$, if and only if $(K_1,K_2)=({}^{\natural},\mathrm{id})$; and then

$$
\tilde{Q}^{\natural}\tilde{Q}=N(\tilde{Q})\,e_0,\qquad N(\tilde{Q})=\sum_{\mu=0}^{3}Q_\mu^{2}.
$$

**Proof.** For the plain product the vector part $2Q_0\mathbf{Q}+\mathbf{Q}\times\mathbf{Q}$ survives; for the two products whose second slot is ${}^{*}$ the vector part survives as well, since the star negates the vector coefficients and leaves the cross terms. For $({}^{\natural},\mathrm{id})$, $\natural$ is the standard involution of the quaternion algebra $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$, whose norm form $\natural(\tilde{Q})\tilde{Q}$ takes values in the centre $\mathbb{C}e_0$ by definition of a quaternion algebra; the value $\sum_\mu Q_\mu^{2}$ is the computation on the basis. $\square$

**Remark (this rule is not general, unlike the two of §*The Slot Calculus*).** In the second instance of §*A Second Instance* the square $A^TA$ is not a scalar multiple of $\mathrm{I}_2$; the property depends on $\natural$ being the standard involution of a quaternion algebra, so the norm form lands in the centre. The two slot rules of §*The Slot Calculus* hold in any such $A$; this one holds in $\mathbb{B}$ because $\mathbb{B}$ is a quaternion algebra over $\mathbb{C}$. The distinction is the reason the row is italicised in the table of §*The Table of the Slots*.

**Theorem (the first slot is isotopy, the second is the derived operation).** Let $K_1\in\{\mathrm{id},\natural\}$ and $K_2\in\{\mathrm{id},{}^{*}\}$. The product $\star_{K_1K_2}$ is the $K_1$-**isotope** of the product $\star_{\mathrm{id}K_2}$, that is, it is the product obtained from the latter by the read-out $K_1$ in the first slot; and $\star_{\mathrm{id}\mathrm{id}}$ and $\star_{\mathrm{id}{}^{*}}$ are respectively the multiplication of the associative algebra $\mathbb{B}$ and its **derived operation** with respect to the involution ${}^{*}$, while $\star_{{}^{\natural}\mathrm{id}}$ and $\star_{{}^{\natural}{}^{*}}$ are their $\natural$-isotopes.

**Proof.** The isotope statement is the definition: $x\star_{K_1K_2}y=K_1(x)\star_{\mathrm{id}K_2}y$ and $K_1$ is a bijection. For the other, the derived operation of an associative algebra $A$ with a conjugate-linear involution $\varsigma$ is the product $x\varsigma(y)$, and the corpus's theorem (*Introduction to the General Plain Sesqualgebra of Biquaternions*) is that $\tilde{P}\tilde{Q}^{*}$ is exactly this with $\varsigma={}^{*}$; the failure of the same test for $\tilde{P}^{\natural}\tilde{Q}^{*}$, and the identification of the fourth product as the $\natural$-isotope of the derived operation, are the content of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, §*The Product Is Not the Derived Operation*. $\square$

**Corollary (the four settings are one product and its three modifications).** The four general products are the plain multiplication, its $\natural$-isotope, the derived operation with respect to ${}^{*}$, and the $\natural$-isotope of that derived operation. Each modification is one slot, and the two modifications commute because the two slots are read independently. **The four objects of the category are therefore the four vertices of the square generated by two operations on one product, and not four general products chosen from a list of sixteen.**

**Remark (the fourth setting fails the two tests its siblings pass).** The general quaternionic sesquilinear product has no unit on either side, by the corollary of §*The Table of the Slots*, and consequently it is not the derived operation of $\mathbb{B}$ with respect to any involution; and its ternary product fails the Jordan triple identity, its left model $\tilde{X}^{*}\tilde{Y}\tilde{Z}$ replacing the middle model $\tilde{X}\tilde{Y}^{*}\tilde{Z}$ that satisfies it (*The Ternary Product and the Failure of the Jordan Triple Identity*, *The Associator of the General Quaternionic Sesquilinear Product*). Both failures are the insertion of ${}^{\natural}$ in the first slot and are recorded in *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*; they are quoted here because they show that the fourth vertex is reached not by the two operations separately but by their composite, and that the composite is not the sum of its parts.

## The Verdict

The four general products of the biquaternion algebra are the four settings of one two-slot construction, $x\star y=K_1(x)K_2(y)$, in which the first slot takes the identity or the natural conjugation and the second the identity or the Hermitian conjugation. The second slot decides everything about the composition — bilinearity, the left unit, the closure of the left multiplications under composition — and the first slot decides the right unit and what the induced form reads on the two sectors, while the coefficient $\varepsilon$ and the Gram matrix $\mathrm{E}$ or $\mathrm{I}_4$ are decided by the two slots together, $\varepsilon$ surviving exactly when they agree. Associativity and the two-sided unit require both slots to be trivial. The division of the four objects of the category into two algebras over $\mathbb{C}$ and two sesqualgebras over $\mathbb{C}$ is the column of the grid, so the four names track the second slot and the adjective *quaternionic* records the first. **The four general products are therefore not four structures but one structure and its two-slot square.** The construction is one and its properties are read off the slots, exactly as the four forms of *The Four Pairings of the Biquaternion Algebra* are four readings of one algebra that coincide.

**The slots and the two exchanges.** The second slot also decides which split of a product keeps the class. When both slots are trivial the swap of the two arguments returns a product of the same class, and the **plain exchange** is the class-preserving one; when one slot is trivial and the other carries the conjugation, as in the two sesquilinear rows, the swap alone returns a product of the opposite parity and the exchange must be composed with a conjugation, $f^{c}(\tilde{P},\tilde{Q})=c(f(\tilde{Q},\tilde{P}))$. So the two sesquilinear products carry **two** splits each, the plain one, whose parts are only $\mathbb{R}$-bilinear, and the adapted one, whose parts are sesquilinear again; and the adapted split of $\tilde{P}\tilde{Q}^{*}$ is the scalar–vector split of its value, into the central scalar part and the vector part, while the adapted split of $\tilde{P}^{\natural}\tilde{Q}^{*}$ is the symmetrisation of $\tilde{P}^{\natural}$ with $\tilde{Q}^{*}$ and half their commutator. The twelve names of the corpus are read against the plain exchange; the adapted one is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*, with the biquaternion instance in *The 12 Products of the Biquaternion Complex Space*, §*The Other Exchange, and the Class It Keeps*.

**Remark (the caveat belongs to the reader).** The four general products are introduced in the corpus one at a time, on their coordinates, and each of the four groups of the category develops one of them. Nothing in that development depends on the present article; its object is to make the relation between the four citable in one place instead of restated in four.

## Summary

The underlying $\mathbb{C}$-vector space of $\mathbb{B}$ carries four general products, and each is obtained from one of them by inserting the involutions of the algebra into the two arguments independently: with $x\star y=K_1(x)K_2(y)$, the first slot $K_1$ is the identity or the natural conjugation ${}^{\natural}$ and the second slot $K_2$ the identity or the Hermitian conjugation ${}^{*}$. The second slot decides the whole composition: bilinearity in the second argument, the existence of a left unit, and the closure of the left multiplications hold if and only if $K_2=\mathrm{id}$, and the monoid of left multiplications is $A$ or its opposite according to the first slot. The first slot decides the right unit, which exists if and only if $K_1=\mathrm{id}$, and the two slots together decide associativity, which fails unless both are trivial. Hence exactly one of the four general products is associative and two-sidedly unital, the quaternionic product $\tilde{P}^{\natural}\tilde{Q}$ has a left unit and no right one, the general plain sesquilinear product $\tilde{P}\tilde{Q}^{*}$ a right unit and no left one, and the general quaternionic sesquilinear product $\tilde{P}^{\natural}\tilde{Q}^{*}$ neither; and the square of an element is a scalar for the quaternionic product alone, where it is the norm $\sum_\mu Q_\mu^{2}$. The scalar parts of the four general products are the four forms, and the coefficient $\varepsilon$ of the scalar part survives precisely when the two slots agree, so the Gram matrix is $\mathrm{E}$ for the plain and the general quaternionic sesquilinear forms and $\mathrm{I}_4$ for the general quaternionic bilinear and general plain sesquilinear ones, whose real forms have signatures $(4,4),(4,4),(8,0)$ and $(2,6)$; only the general plain sesquilinear form is positive definite. Finally the first slot is isotopy and the second is the passage to the derived operation, so the four general products are one multiplication, its $\natural$-isotope, the derived operation with respect to ${}^{*}$, and the isotope of that. The division of the four objects of the category into two algebras over $\mathbb{C}$ and two sesqualgebras over $\mathbb{C}$ is the division of the four general products by the second slot, and, with associativity excepted as noted in §*The Table of the Slots*, the slot rules are theorems about any unital associative algebra with two commuting anti-involutions, verified on a second instance.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $x\star_{K_1K_2}y=K_1(x)K_2(y)$ | the slot family; $K_1\in\{\mathrm{id},{}^{\natural}\}$, $K_2\in\{\mathrm{id},{}^{*}\}$ |
| $(\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}^{\natural},{}^{*})$ | the plain, quaternionic, general plain sesquilinear and general quaternionic sesquilinear products |
| $K_2=\mathrm{id}$ | bilinear in the second argument, left unit, left multiplications compose |
| $K_1=\mathrm{id}$ | right unit; the induced form is definite on each sector |
| the two slots agree | the coefficient $\varepsilon$ survives in the scalar form, and the Gram matrix is $\mathrm{E}$ |
| $K_1=K_2=\mathrm{id}$ | associative and two-sidedly unital |
| $({}^{\natural},\mathrm{id})$ | the only setting whose square is scalar: $\tilde{Q}^{\natural}\tilde{Q}=N(\tilde{Q})e_0$ |
| $\mathrm{Sc}(K_1\tilde{P}\cdot K_2\tilde{Q})=\sum_\mu\varepsilon_\mu^{1-[K_1={}^{\natural}]}P_\mu(K_2\tilde{Q})_\mu$ | the two marks; $\varepsilon$ survives when the slots agree |
| $\mathrm{E}$, $\mathrm{I}_4$ | the Gram matrix of the agreeing and of the differing settings |
| $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ | the real signatures of the four forms |
| isotope, derived operation | the first slot and the second slot read as the two operations on the product |
| $M_2(\mathbb{C})$ with $(T,{}^{*})$ | the second instance on which the slot rules were checked |

## Further Reading

- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the four general products introduced independently on the coordinates
- *Relations Between the Four General Products* (`articles_maths/relations-between-the-four-general-products.md`), for the identities that link the four general products and the four forms
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table read by slot in §*The Table of the Slots*, and for the list of which of the four is an associative or a sesquilinear multiplication
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), the companion that reads the four forms as four diagonals, with the Gram matrices, the signatures $(4,4),(4,4),(8,0),(2,6)$ and the automorphism groups on one space
- *Introduction to the General Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-biquaternions.md`), for the first vertex and the ideals and Peirce decomposition of the plain product
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the second vertex, its sign table and the property that its square is scalar
- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the third vertex and the theorem that $\tilde{P}\tilde{Q}^{*}$ is the derived operation
- *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the fourth vertex, the two one-sided actions of the unit, the failure of the derived-operation test and the failure of the Jordan triple identity
- *Algebras: A General Introduction* (`articles_maths/algebras-a-general-introduction.md`) and *Sesqualgebras* (`articles_maths/sesqualgebras.md`), for the two definitions of §*The Two Algebras and the Two Sesqualgebras*
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`) and *The Two One-Sided Actions and the Absence of a Unit* (`articles_maths/the-two-one-sided-actions-and-the-absence-of-a-unit.md`), for the per-product development of the two slot rules of §*The Slot Calculus*
- *The Ternary Product and the Failure of the Jordan Triple Identity* (`articles_maths/the-ternary-product-and-the-failure-of-the-jordan-triple-identity.md`) and *The Associator of the General Quaternionic Sesquilinear Product* (`articles_maths/the-associator-of-the-quaternionic-sesquilinear-product.md`), for the failure of the fourth setting recorded in §*The Square, the Derived Operation and the Isotope*
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the four commuting conjugations and the place of $\natural$ and ${}^{*}$ among them
- Physics companion *The Four General Products and Their Physical Readings* (`articles_physics/the-four-general-products-and-their-physical-readings.md`), the same grid read physically, blocks of the physics menu and the four jobs of composition, causality, probability and gauge
