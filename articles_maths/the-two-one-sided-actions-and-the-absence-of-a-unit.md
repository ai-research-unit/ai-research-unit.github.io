
# __The Two One-Sided Actions and the Absence of a Unit__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four general products on its underlying $\mathbb{C}$-vector space (*The Four General Products of the Biquaternioid $\mathbb{C}$ Space*), and the fourth of them,

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*} ,
$$

is the subject of this group. The rule, the scalar–vector form and the place of the product among the four are *The Four General Products of the Biquaternioid $\mathbb{C}$ Space* §*The General Quaternionic Sesquilinear Product*; the sesqualgebra it defines, its multiplication table and its two actions of the unit are *Introduction to the General Quaternionic Sesqualgebra*. The symbols are those of the group: ${}^{\natural}$ is the natural conjugation $\tilde P^{\natural} = P_t - \vec P$, ${}^{*}$ is the star conjugation $\tilde P^{*} = \overline{P_t} - \overline{\vec P}$, the bar is the coefficientwise complex conjugation, and $\vec P = \sum_k P_k \vec e_k$ is the vector part.

The subject of this article is the pair of **one-sided actions of the unit candidate** $e_t$, and the fact that they are not the identity but the two conjugations of the algebra:

$$
e_t \star \tilde Q = \tilde Q^{*} , \qquad \tilde Q \star e_t = \tilde Q^{\natural} .
$$

Both hold for every $\tilde Q$, and both are then read on the remarkable subspaces. Their consequence is the group's defining negative statement: the multiplication has **no unit on either side**. There is no element $\tilde E$ with $\tilde E \star \tilde Q = \tilde Q$ for all $\tilde Q$, and none with $\tilde Q \star \tilde E = \tilde Q$ for all $\tilde Q$. The third product of the four has a right unit and no left one, the second has a left unit and no right one, and the first has a unit; the fourth has neither, and this is what separates its structure theory from the other three.

The article owns the two actions and the absence of a unit. It reads the actions off the rule, which is *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*; it uses the two scalar rules of the category, which are *Sesqualgebras* §*The Definition*; it uses the derived-operation test with its two conditions, which is *Sesqualgebras* §*The Standard Example* as applied to $\mathbb{B}$ in *Introduction to the General Quaternionic Sesqualgebra* §*The Product Is Not the Derived Operation*; and it uses the reading of the two conjugations on the remarkable subspaces, which is *Introduction to the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*. It does not treat the general operators of the multiplication, which are the later article of this group *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*, nor the ternary product, which is *The Ternary Product and the Failure of the Jordan Triple Identity*.

## The Two Actions of the Unit

### The Left Action Is the Star

**Proposition (the left action).** For every biquaternion $\tilde Q$,

$$
e_t \star \tilde Q = \tilde Q^{*} .
$$

**Proof.** By the rule, $e_t \star \tilde Q = e_t^{\natural}\tilde Q^{*}$. The natural conjugation fixes the identity, $e_t^{\natural} = e_t$, and $e_t$ is the unit of the plain product, so $e_t^{\natural}\tilde Q^{*} = \tilde Q^{*}$.

**Remark.** The left action of the unit candidate is therefore not the identity but the star conjugation, which is conjugate-linear: $e_t \star (\lambda \tilde Q) = (\lambda\tilde Q)^{*} = \bar\lambda\,\tilde Q^{*} = \bar\lambda\,(e_t \star \tilde Q)$. This one computation already rules out a left unit, and it is the operator-level form of the second scalar rule of the category applied at $e_t$.

### The Right Action Is the Natural Conjugation

**Proposition (the right action).** For every biquaternion $\tilde Q$,

$$
\tilde Q \star e_t = \tilde Q^{\natural} .
$$

**Proof.** By the rule, $\tilde Q \star e_t = \tilde Q^{\natural} e_t^{*}$. The star conjugation fixes the identity, $e_t^{*} = e_t$, so $\tilde Q^{\natural}e_t^{*} = \tilde Q^{\natural}$.

**Remark.** The right action is the natural conjugation, which is $\mathbb{C}$-linear: $\tilde Q \star (\lambda e_t) = (\lambda e_t)^{\natural} = \lambda\,\tilde Q^{\natural} = \lambda\,(\tilde Q \star e_t)$. The two actions are thus a conjugate-linear one on the left and a linear one on the right, and they are the two conjugations of the group of involutions (*The Group of Involutions*, *The Involutions of a Sesqualgebra*).

### Both Actions Are Involutions

**Proposition.** The maps $\tilde Q \mapsto e_t \star \tilde Q$ and $\tilde Q \mapsto \tilde Q \star e_t$ are the involutions ${}^{*}$ and ${}^{\natural}$; they are bijections of order two, they commute, and together with the identity and their composite $\overline{\cdot}$ they form the **group of involutions** $\{ \mathrm{id}, {}^{\natural}, {}^{*}, \overline{\cdot} \}$, the Klein four-group $\mathbb{Z}_2 \times \mathbb{Z}_2$ of *The Group of Involutions*.

**Proof.** The two maps are ${}^{*}$ and ${}^{\natural}$ by the propositions above. Each is an involution by the definition of the conjugations, ${}^{*2} = \mathrm{id}$ and ${}^{\natural2} = \mathrm{id}$, and they commute, so their composite is the complex conjugation $\bar{\cdot} = {}^{\natural} \circ {}^{*}$, which is also of order two. The four maps are distinct and form a group isomorphic to $(\mathbb{Z}/2)^{2}$.

**Remark.** The element $e_t$ acts on the left by one involution and on the right by the other, and the composite of the two actions is the coefficientwise complex conjugation. This is the sense in which the unit candidate acts by the *whole* involution group and not by the identity: the failure to be a unit is the failure of the two actions to collapse to $\mathrm{id}$.

## The Absence of a Unit

### No Left Unit

**Theorem.** There is no element $\tilde E$ with $\tilde E \star \tilde Q = \tilde Q$ for all $\tilde Q$.

**Proof.** Suppose $\tilde E$ is a left unit, so that $\tilde E \star \tilde Q = \tilde Q$ for every $\tilde Q$. Testing at $\tilde Q = e_t$ and using the right action of $e_t$ gives

$$
\tilde E \star e_t = \tilde E^{\natural} = e_t ,
$$

and applying the involution ${}^{\natural}$ gives $\tilde E = e_t$. With $\tilde E = e_t$ the left-unit equation would read $e_t \star \tilde Q = \tilde Q^{*} = \tilde Q$ for every $\tilde Q$, which fails at $\tilde Q = \vec e_x$, where $\tilde Q^{*} = -\vec e_x$. Hence there is no left unit.

**Remark.** The first test at $\tilde Q = e_t$ uses the right action to force the candidate to $e_t$, and the second test at $\tilde Q = \vec e_x$ uses the left action to reject it. The two actions are the two halves of the contradiction, and the same pair of tests settles the right-unit case with the roles of the two actions interchanged.

### No Right Unit

**Theorem.** There is no element $\tilde E$ with $\tilde Q \star \tilde E = \tilde Q$ for all $\tilde Q$.

**Proof.** Suppose $\tilde E$ is a right unit, so that $\tilde Q \star \tilde E = \tilde Q$ for every $\tilde Q$. Testing at $\tilde Q = e_t$ and using the left action of $e_t$ gives

$$
e_t \star \tilde E = \tilde E^{*} = e_t ,
$$

and applying the involution ${}^{*}$ gives $\tilde E = e_t$. With $\tilde E = e_t$ the right-unit equation would read $\tilde Q \star e_t = \tilde Q^{\natural} = \tilde Q$ for every $\tilde Q$, which fails at $\tilde Q = \vec e_x$, where $\tilde Q^{\natural} = -\vec e_x$. Hence there is no right unit.

**Remark.** The two proofs are the same computation with the two involutions exchanged, and this is why the absence of a unit holds on both sides and not only on one: each of the two conjugations obstructs one of the two sides. The pair of tests at $e_t$ and $\vec e_x$ is the smallest possible, and it is the one the group article records.

### No Unit and No Inverses

**Corollary.** The multiplication has no two-sided unit. Consequently no element has a left inverse or a right inverse, and the product defines no group of units.

**Proof.** A two-sided unit is a left unit and a right unit at once, and neither exists. An inverse of $\tilde A$ is an element $\tilde Q_1$ with $\tilde A \star \tilde Q_1 = \tilde Q_1 \star \tilde A = \tilde U$ where $\tilde U$ is a unit of the multiplication; with no unit, the notion is empty.

**Caution.** The words *unit* and *inverse* must be used with the multiplication of this group and not with the plain product of the algebra. The algebra $\mathbb{B}$ has a group of units, the elements of nonzero norm $\langle\tilde P\rangle_{\natural} \neq 0$, and its unit group is $GL_2(\mathbb{C})$ through the matrix realization, with the norm-one subgroup $SL_2(\mathbb{C})$ (*Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, *Ideals and Peirce Decomposition of the Biquaternion Algebra*); that group belongs to the plain product and to the algebra, not to $\star$. An element such as an idempotent $\tilde\Pi(\mu)$ of *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra* is a unit of the algebra and not a unit of the multiplication, and it satisfies $\tilde\Pi \star \tilde\Pi = \tilde\Pi$ all the same.

## The Two Actions and the Derived-Operation Test

### The First Row of the Product

**Definition.** The **first row** of the multiplication is the map

$$
\sigma(\tilde Q_2) = e_t \star \tilde Q_2 = \tilde Q_2^{*} ,
$$

obtained by holding the first argument at $e_t$, in the notation of *Sesqualgebras* §*The Standard Example*.

By the first proposition above, the first row of the multiplication is the star conjugation.

### The Two Conditions

The general theory asks whether a sesquilinear product is the **derived operation** $x \star y = xy^{*}$ of an associative algebra with a conjugate-linear involution. It is exactly then that the first row is such an involution and rebuilds the product; stated as in *Introduction to the General Plain Sesqualgebra* §*Which of the Four Is a Sesquilinear Multiplication* and in *Sesqualgebras* §*The Standard Example*, the two conditions are:

(i) $\sigma$ is a conjugate-linear involution of the algebra: $\sigma(\lambda\tilde Q_2) = \bar\lambda\,\sigma(\tilde Q_2)$, $\sigma^{2} = \mathrm{id}$, $\sigma(\tilde Q_3\tilde Q_2) = \sigma(\tilde Q_2)\sigma(\tilde Q_3)$ and $\sigma(e_t) = e_t$;

(ii) $\sigma$ rebuilds the product: $\tilde Q_3 \star \tilde Q_2 = \tilde Q_3\,\sigma(\tilde Q_2)$ for all $\tilde Q_3, \tilde Q_2$.

**Theorem (the first row passes one condition and fails the other).** For the general quaternionic sesquilinear product, $\sigma = {}^{*}$ satisfies condition (i) and fails condition (ii); consequently the product is not the derived operation of the algebra with any involution.

**Proof.** Condition (i): the star conjugation is conjugate-linear, involutive, anti-multiplicative and fixes $e_t$, which is the statement that it is the involution of the derived operation (*The Group of Involutions*, *Introduction to the Biquaternion Algebra*). So (i) holds. Condition (ii) with $\sigma = {}^{*}$ would read $\tilde Q_3^{\natural}\tilde Q_2^{*} = \tilde Q_3\tilde Q_2^{*}$ for all $\tilde Q_3, \tilde Q_2$; at $\tilde Q_2 = e_t$ this is $\tilde Q_3^{\natural} = \tilde Q_3$ for every $\tilde Q_3$, which fails at $\tilde Q_3 = \vec e_x$, where the two sides are $-\vec e_x$ and $\vec e_x$. So (ii) fails.

**Remark.** The failure of (ii) is the absence of a right unit, read in the second slot: with $\tilde Q_2 = e_t$, condition (ii) says $\tilde Q_3 \star e_t = \tilde Q_3\sigma(e_t) = \tilde Q_3$, that is $\tilde Q_3^{\natural} = \tilde Q_3$ for every $\tilde Q_3$, which is exactly the statement that $e_t$ is a right unit of the multiplication. The two forms of the same failure are the derived-operation test and the right-unit test, and the theorem is their equivalence for this product.

### The Isotope Interpretation

**Corollary.** The product is the **isotope** of the derived operation by the natural conjugation,

$$
\tilde P \star \tilde Q = {}^{\natural}(\tilde P)\,\tilde Q^{*} = \tilde P^{\natural}\tilde Q^{*} ,
$$

the insertion being in the first slot and the derived operation being $\tilde P\tilde Q^{*}$ with its star involution.

**Proof.** The formula is the rule. The map ${}^{\natural}$ is a $\mathbb{C}$-linear anti-automorphism and a bijection of $\mathbb{B}$, and an isotope of an operation by a bijection $\varphi$ is the operation $(x,y) \mapsto \varphi(x)\,y$; here $\varphi = {}^{\natural}$.

**Remark.** The two sesquilinear products of the four are the derived operation and its ${}^{\natural}$-isotope, exactly as the two bilinear products of the four are the plain multiplication and its ${}^{\natural}$-isotope; in each pair the second is the first with the $\mathbb{C}$-linear insertion the derived-operation test rejects (*Comparison Between the Four General Products* §*Which of the Four Is a Multiplication*, *Introduction to the General Quaternionic Sesqualgebra* §*The Isotope Interpretation*). The absence of a unit in the second member of each pair is the price of the insertion: the derived operation keeps the right unit $e_t$, and its isotope loses it in the first slot.

## The Actions on the Remarkable Subspaces

The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_{+}$ and the anti-Hermitian subspace $\mathbb{M}_{-}$ (*Introduction to the Remarkable Subspaces*). Each of the two conjugations preserves each of the remarkable subspaces (*Remarkable Subspaces and the Four General Products* §*The four general products have the same value set*), so each action of $e_t$ restricts to each subspace, and the two restrictions are computed below.

**Theorem (the two actions on the remarkable subspaces).**

| subspace | left action $e_t \star \cdot = {}^{*}$ | right action $\cdot \star e_t = {}^{\natural}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $A e_t \mapsto \bar A e_t$ | identity |
| $\mathrm{Vect}(\mathbb{B})$ | $\vec Q \mapsto -\overline{\vec Q}$ | $\vec Q \mapsto -\vec Q$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\tilde Q \mapsto \tilde Q^{\natural}$ | $\tilde Q \mapsto \tilde Q^{\natural}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\tilde Q \mapsto -\tilde Q^{\natural}$ | $\tilde Q \mapsto \tilde Q^{\natural}$ |
| $\mathbb{M}_{+}$ | identity | $\tilde Q \mapsto \tilde Q^{\natural}$ |
| $\mathbb{M}_{-}$ | $-\mathrm{id}$ | $\tilde Q \mapsto \tilde Q^{\natural}$ |

**Proof.** The left column is the star conjugation, $Q^{*}_t = \overline{Q_t}$ and $Q^{*}_k = -\overline{Q_k}$; the right column is the natural conjugation, $\tilde Q^{\natural} = Q_t - \vec Q$.

- On the centre, $\vec Q = 0$, so ${}^{*}$ is the coefficientwise conjugation of the single coordinate and ${}^{\natural}$ fixes the element.
- On the vector subspace, $Q_t = 0$, so ${}^{*}$ sends $\vec Q$ to $-\overline{\vec Q}$ and ${}^{\natural}$ sends it to $-\vec Q$.
- On the quaternion subspace the coordinates are real, so the coefficientwise conjugation is the identity and the two conjugations coincide, both negating the vector part: this is the quaternionic conjugation of the real quaternion subspace.
- On the anti-quaternion subspace write $\tilde Q = i\tilde K$ with $\tilde K$ in the quaternion subspace, so that $\tilde K^{*} = \tilde K^{\natural}$ there and the star is conjugate-linear while ${}^{\natural}$ is $\mathbb{C}$-linear: $\tilde Q^{*} = (i\tilde K)^{*} = -i\,\tilde K^{*} = -i\,\tilde K^{\natural} = -(i\tilde K)^{\natural} = -\tilde Q^{\natural}$, while the right action is $\tilde Q^{\natural}$.
- On the Hermitian subspace, ${}^{*}$ is the identity by definition, and ${}^{\natural}$ fixes the real scalar coordinate and negates the imaginary vector coordinate, $\tilde Q = a_t + i\vec p \mapsto a_t - i\vec p$, which stays in $\mathbb{M}_{+}$.
- On the anti-Hermitian subspace, ${}^{*}$ is $-\mathrm{id}$ by definition, and ${}^{\natural}$ fixes the imaginary scalar coordinate and negates the real vector coordinate, $\tilde Q = i b_t + \vec q \mapsto i b_t - \vec q$, which stays in $\mathbb{M}_{-}$.

**Remark.** Two entries are the identity, and each is instructive. The left action is the identity on the Hermitian subspace, because that is the fixed space of ${}^{*}$; the right action is the identity on the centre, because the natural conjugation does not touch a scalar element; and no action is the identity on all of $\mathbb{B}$, which is the absence of a unit in its subspace form. The table also shows where the two actions agree, on $\mathbb{H}_{\mathbb{B}}$, and where they differ by a sign, on $i\mathbb{H}_{\mathbb{B}}$ and on $\mathbb{M}_{\pm}$.

## The Unit Candidate as an Idempotent

### The Element $e_t$ Is an Idempotent of the Multiplication

**Proposition.** The unit candidate is an idempotent of the multiplication, $e_t \star e_t = e_t$, and both actions fix it.

**Proof.** By the rule, $e_t \star e_t = e_t^{\natural}e_t^{*} = e_te_t = e_t$, the two conjugations fixing the identity and the identity being the unit of the plain product. The two actions fix $e_t$ by the same computation.

**Remark.** The element $e_t$ is the **trivial** idempotent of the multiplication, the one the nontrivial idempotents of *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra* are contrasted with; unlike them it is central, and it is the unit of the plain product. It is therefore the cleanest single witness that the two notions of unit differ: it is a unit of the algebra, and it is not a unit of $\star$ because it acts by the two conjugations.

### The Two Actions and the Norm

**Proposition.** For every biquaternion $\tilde Q$,

$$
N\bigl(e_t \star \tilde Q\bigr) = \langle\tilde Q^{*}\rangle_{\natural} = \overline{\langle\tilde Q\rangle_{\natural}} , \qquad N\bigl(\tilde Q \star e_t\bigr) = \langle\tilde Q^{\natural}\rangle_{\natural} = \langle\tilde Q\rangle_{\natural} .
$$

The left action conjugates the norm and the right action preserves it; both preserve its modulus $\lvert N\rvert$ and hence the zero-divisor cone $\{N = 0\}$.

**Proof.** The norm is multiplicative for the plain product with $N(e_t) = 1$; it is invariant under the natural conjugation, $\langle\tilde Q^{\natural}\rangle_{\natural} = \langle\tilde Q\rangle_{\natural}$, because ${}^{\natural}$ negates an even number of coordinates with the square; and it transforms by the coefficientwise conjugation under ${}^{*}$, $\langle\tilde Q^{*}\rangle_{\natural} = \overline{\langle\tilde Q\rangle_{\natural}}$, because ${}^{*}$ conjugates each coordinate and $N$ is a quadratic form in the coordinates with real coefficients. The two actions are ${}^{*}$ and ${}^{\natural}$.

**Remark.** The two transforms are the numerical trace of the two parities of the actions: the conjugate-linear action conjugates the quadratic form and the linear action fixes it, and the composite, the coefficientwise conjugation, is the Galois action of $\mathbb{C}$ over $\mathbb{R}$ that distinguishes them. The preservation of the modulus is the reason the two actions are symmetries of the zero-divisor cone $N = 0$, the set on which the element theory of the product is read, and it is why an element and its two conjugates are zero divisors together.

## The Consequences of the Absence

### The Notions That Have to Be Replaced

With no unit, the derived vocabulary of an algebra has to be replaced, and the group names the replacements as they are used.

- **The group of units** does not exist for the multiplication; the algebra's group of units is a different group, belonging to the plain product, and is the subject of *Ideals and Peirce Decomposition of the Biquaternion Algebra*. The elements of the multiplication that are units of the algebra are distinguished by the norm, and for the idempotents this is *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*.
- **The inverse** is replaced by the involution: the closest substitute for an inverse, given that $\tilde P\tilde P^{\natural} = \langle\tilde P\rangle_{\natural}e_t$ and the product twists each slot by a conjugation, is the operation of the two conjugations themselves. Each nontrivial idempotent, for example, has inverse its own natural conjugate in the algebra, $\tilde\Pi^{-1} = \tilde\Pi^{\natural}$, although that inverse is not an inverse of the multiplication.
- **One-sided identities** are not available, and the binary structure has to be replaced by the **ternary product**, which is the later article of this group *The Ternary Product and the Failure of the Jordan Triple Identity*. The definition of that ternary product, $\{ \tilde P,\tilde Q,\tilde R \} = (\tilde P \star \tilde Q) \star \tilde R^{*}$, itself uses the star conjugation in the third slot, so the involution that obstructs the unit is the involution that builds the ternary structure.
- **The left multiplications** do not form a monoid, and the composition laws are the later article *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*; the present article supplies the negative statement that makes those laws necessary.

### The Comparison with the Sibling Products

**Theorem (the unit row of the four general products).**

| product | left unit | right unit |
|---|---|---|
| $\tilde P\tilde Q$ | $e_t$ | $e_t$ |
| $\tilde P^{\natural}\tilde Q$ | $e_t$ | none |
| $\tilde P\tilde Q^{*}$ | none | $e_t$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | none | none |

**Proof.** The plain product is the associative product of the algebra and has the two-sided unit $e_t$. For the sibling bilinear product, $e_t \star \tilde Q_2 = e_t^{\natural}\tilde Q_2 = \tilde Q_2$ because ${}^{\natural}$ fixes $e_t$, so $e_t$ is a left unit, and there is no right one (*Introduction to the General Quaternionic Algebra* §*The Unit*). For the sibling sesquilinear product, $\tilde Q_2 \star e_t = \tilde Q_2 e_t^{*} = \tilde Q_2$, so $e_t$ is a right unit, and there is no left one (*Introduction to the General Plain Sesqualgebra* §*The Right Unit*). The fourth row is the two theorems of this article, in the form that both actions of $e_t$ are conjugations and neither is the identity.

**Remark.** The four rows are the sharpest reading of the two slots. Each of the four general products makes one of the two slots the identity and the other slot the twist: the two bilinear products put the twist in the first slot and the identity in the second, one of them losing the right unit and the other the left; the sibling sesquilinear product has the twist in the second slot and the identity in the first, keeping the right unit; and this product puts a twist in both slots, keeping neither. The table is the unit row of the comparison of the four general products, *Comparison Between the Four General Products*, read with the two actions of this article.

## Summary

The two one-sided actions of $e_t$ under the general quaternionic sesquilinear multiplication $\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*}$ are the two conjugations of the algebra: the left action is the star, $e_t \star \tilde Q = \tilde Q^{*}$, and the right action is the natural conjugation, $\tilde Q \star e_t = \tilde Q^{\natural}$. Both actions are involutions of $\mathbb{B}$, they commute, and together with the identity and their composite, the coefficientwise conjugation, they form the group of involutions, the Klein four-group. Their consequence is that the multiplication has no unit on either side: a left-unit candidate is forced by the right action to $e_t$ and then rejected by the left action at $\vec e_x$, and a right-unit candidate is forced by the left action to $e_t$ and then rejected by the right action at $\vec e_x$; hence there is no two-sided unit, no inverse and no group of units of the multiplication, and the group of units of the algebra is a different group belonging to the plain product. On the derived-operation test the first row of the multiplication is the star conjugation, which satisfies condition (i) and fails condition (ii), so the multiplication is the isotope of the derived operation by the natural conjugation and not the derived operation itself. On the remarkable subspaces the two actions restrict to the coefficientwise conjugation, the negation with a conjugation, the quaternionic conjugation, a sign, the identity and a reflection, and no one of them is the identity on all of $\mathbb{B}$. The unit candidate is itself the trivial idempotent of the multiplication, $e_t \star e_t = e_t$, and its two actions transform the norm by the character of their parity, $\langle e_t \star \tilde Q\rangle_{\natural} = \overline{\langle\tilde Q\rangle_{\natural}}$ and $\langle\tilde Q \star e_t\rangle_{\natural} = \langle\tilde Q\rangle_{\natural}$, so that both preserve the modulus and the zero-divisor cone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*}$ | the multiplication of this group |
| $e_t \star \tilde Q = \tilde Q^{*}$ | the left action of $e_t$, the star conjugation |
| $\tilde Q \star e_t = \tilde Q^{\natural}$ | the right action of $e_t$, the natural conjugation |
| $\bar{\cdot} = {}^{\natural} \circ {}^{*}$ | the coefficientwise conjugation, the composite of the two actions |
| $\{ \mathrm{id}, {}^{\natural}, {}^{*}, \bar{\cdot} \}$ | the group of involutions, the Klein four-group |
| $\sigma(\tilde Q_2) = e_t \star \tilde Q_2 = \tilde Q_2^{*}$ | the first row of the multiplication |
| (i) | $\sigma$ is a conjugate-linear involution of the algebra |
| (ii) | $\tilde Q_3 \star \tilde Q_2 = \tilde Q_3\,\sigma(\tilde Q_2)$ |
| $\tilde P \star \tilde Q = {}^{\natural}(\tilde P)\,\tilde Q^{*}$ | the product as the isotope of the derived operation |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}), \mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_{+}, \mathbb{M}_{-}$ | the remarkable subspaces |
| $e_t \star e_t = e_t$ | the unit candidate as the trivial idempotent of the multiplication |
| $\langle e_t \star \tilde Q\rangle_{\natural} = \overline{\langle\tilde Q\rangle_{\natural}}$ | the left action conjugates the norm |
| $\langle\tilde Q \star e_t\rangle_{\natural} = \langle\tilde Q\rangle_{\natural}$ | the right action preserves the norm |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the one-sided identity, the units of an algebra and the regular actions.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the relation between an involution and the one-sided actions it defines.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the isotopy of a multiplication by an anti-automorphism and the loss of the unit it entails.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the conjugate-linear involutions and the derived operation of an algebra with involution.
