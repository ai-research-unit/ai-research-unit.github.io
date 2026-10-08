
# __The Two One-Sided Actions and the Absence of a Unit__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four products on its underlying $\mathbb{C}$-vector space (*The Four Biquaternion Complex Products*), and the fourth of them,

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*} ,
$$

is the subject of this group. The rule, the scalar–vector form and the place of the product among the four are *The Four Biquaternion Complex Products* §*The Complex Quaternionic Sesquilinear Product*; the sesqualgebra it defines, its multiplication table and its two actions of the unit are *Biquaternions as a General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$*. The symbols are those of the group: ${}^{\natural}$ is the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$, ${}^{*}$ is the star conjugation $\tilde P^{*} = \overline{P_0} - \overline{\mathbf Q}$, the bar is the coefficientwise complex conjugation, and $\mathbf P = \sum_k P_k e_k$ is the vector part.

The subject of this article is the pair of **one-sided actions of the unit candidate** $e_0$, and the fact that they are not the identity but the two conjugations of the algebra:

$$
e_0 \star \tilde Q = \tilde Q^{*} , \qquad \tilde Q \star e_0 = \tilde Q^{\natural} .
$$

Both hold for every $\tilde Q$, and both are then read on the six distinguished subspaces. Their consequence is the group's defining negative statement: the multiplication has **no unit on either side**. There is no element $\tilde E$ with $\tilde E \star \tilde Q = \tilde Q$ for all $\tilde Q$, and none with $\tilde Q \star \tilde E = \tilde Q$ for all $\tilde Q$. The third product of the four has a right unit and no left one, the second has a left unit and no right one, and the first has a unit; the fourth has neither, and this is what separates its structure theory from the other three.

The article owns the two actions and the absence of a unit. It reads the actions off the rule, which is *The Four Biquaternion Complex Products*; it uses the two scalar rules of the category, which are *Sesqualgebras* §*The Definition*; it uses the derived-operation test with its two conditions, which is *Sesqualgebras* §*The Standard Example* as applied to $\mathbb{B}$ in *Biquaternions as a General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$* §*The Product Is Not the Derived Operation*; and it uses the reading of the two conjugations on the six subspaces, which is *Introduction to the Six Subspaces* and *Comparison of the Six Subspaces*. It does not treat the general operators of the multiplication, which are the later article of this group *The Left and Right Multiplications of the Quaternionic Sesquilinear Product*, nor the ternary product, which is *The Ternary Product and the Failure of the Jordan Triple Identity*.

## The Two Actions of the Unit

### The Left Action Is the Star

**Proposition (the left action).** For every biquaternion $\tilde Q$,

$$
e_0 \star \tilde Q = \tilde Q^{*} .
$$

**Proof.** By the rule, $e_0 \star \tilde Q = e_0^{\natural}\tilde Q^{*}$. The natural conjugation fixes the identity, $e_0^{\natural} = e_0$, and $e_0$ is the unit of the plain product, so $e_0^{\natural}\tilde Q^{*} = \tilde Q^{*}$. $\square$

**Remark.** The left action of the unit candidate is therefore not the identity but the star conjugation, which is conjugate-linear: $e_0 \star (\lambda \tilde Q) = (\lambda\tilde Q)^{*} = \bar\lambda\,\tilde Q^{*} = \bar\lambda\,(e_0 \star \tilde Q)$. This one computation already rules out a left unit, and it is the operator-level form of the second scalar rule of the category applied at $e_0$.

### The Right Action Is the Natural Conjugation

**Proposition (the right action).** For every biquaternion $\tilde Q$,

$$
\tilde Q \star e_0 = \tilde Q^{\natural} .
$$

**Proof.** By the rule, $\tilde Q \star e_0 = \tilde Q^{\natural} e_0^{*}$. The star conjugation fixes the identity, $e_0^{*} = e_0$, so $\tilde Q^{\natural}e_0^{*} = \tilde Q^{\natural}$. $\square$

**Remark.** The right action is the natural conjugation, which is $\mathbb{C}$-linear: $\tilde Q \star (\lambda e_0) = (\lambda e_0)^{\natural} = \lambda\,\tilde Q^{\natural} = \lambda\,(\tilde Q \star e_0)$. The two actions are thus a conjugate-linear one on the left and a linear one on the right, and they are the two conjugations of the group of involutions (*The Group of Involutions*, *The Involutions of a Sesqualgebra*).

### Both Actions Are Involutions

**Proposition.** The maps $\tilde Q \mapsto e_0 \star \tilde Q$ and $\tilde Q \mapsto \tilde Q \star e_0$ are the involutions ${}^{*}$ and ${}^{\natural}$; they are bijections of order two, they commute, and together with the identity and their composite $\overline{\cdot}$ they form the **group of involutions** $\{ \mathrm{id}, {}^{\natural}, {}^{*}, \overline{\cdot} \}$, the Klein four-group $\mathbb{Z}_2 \times \mathbb{Z}_2$ of *The Group of Involutions*.

**Proof.** The two maps are ${}^{*}$ and ${}^{\natural}$ by the propositions above. Each is an involution by the definition of the conjugations, ${}^{*2} = \mathrm{id}$ and ${}^{\natural2} = \mathrm{id}$, and they commute, so their composite is the complex conjugation $\bar{\cdot} = {}^{\natural} \circ {}^{*}$, which is also of order two. The four maps are distinct and form a group isomorphic to $(\mathbb{Z}/2)^{2}$. $\square$

**Remark.** The element $e_0$ acts on the left by one involution and on the right by the other, and the composite of the two actions is the coefficientwise complex conjugation. This is the sense in which the unit candidate acts by the *whole* involution group and not by the identity: the failure to be a unit is the failure of the two actions to collapse to $\mathrm{id}$.

## The Absence of a Unit

### No Left Unit

**Theorem.** There is no element $\tilde E$ with $\tilde E \star \tilde Q = \tilde Q$ for all $\tilde Q$.

**Proof.** Suppose $\tilde E$ is a left unit, so that $\tilde E \star \tilde Q = \tilde Q$ for every $\tilde Q$. Testing at $\tilde Q = e_0$ and using the right action of $e_0$ gives

$$
\tilde E \star e_0 = \tilde E^{\natural} = e_0 ,
$$

and applying the involution ${}^{\natural}$ gives $\tilde E = e_0$. With $\tilde E = e_0$ the left-unit equation would read $e_0 \star \tilde Q = \tilde Q^{*} = \tilde Q$ for every $\tilde Q$, which fails at $\tilde Q = e_1$, where $\tilde Q^{*} = -e_1$. Hence there is no left unit. $\square$

**Remark.** The first test at $\tilde Q = e_0$ uses the right action to force the candidate to $e_0$, and the second test at $\tilde Q = e_1$ uses the left action to reject it. The two actions are the two halves of the contradiction, and the same pair of tests settles the right-unit case with the roles of the two actions interchanged.

### No Right Unit

**Theorem.** There is no element $\tilde E$ with $\tilde Q \star \tilde E = \tilde Q$ for all $\tilde Q$.

**Proof.** Suppose $\tilde E$ is a right unit, so that $\tilde Q \star \tilde E = \tilde Q$ for every $\tilde Q$. Testing at $\tilde Q = e_0$ and using the left action of $e_0$ gives

$$
e_0 \star \tilde E = \tilde E^{*} = e_0 ,
$$

and applying the involution ${}^{*}$ gives $\tilde E = e_0$. With $\tilde E = e_0$ the right-unit equation would read $\tilde Q \star e_0 = \tilde Q^{\natural} = \tilde Q$ for every $\tilde Q$, which fails at $\tilde Q = e_1$, where $\tilde Q^{\natural} = -e_1$. Hence there is no right unit. $\square$

**Remark.** The two proofs are the same computation with the two involutions exchanged, and this is why the absence of a unit holds on both sides and not only on one: each of the two conjugations obstructs one of the two sides. The pair of tests at $e_0$ and $e_1$ is the smallest possible, and it is the one the group article records.

### No Unit and No Inverses

**Corollary.** The multiplication has no two-sided unit. Consequently no element has a left inverse or a right inverse, and the product defines no group of units.

**Proof.** A two-sided unit is a left unit and a right unit at once, and neither exists. An inverse of $\tilde A$ is an element $\tilde B$ with $\tilde A \star \tilde B = \tilde B \star \tilde A = \tilde U$ where $\tilde U$ is a unit of the multiplication; with no unit, the notion is empty. $\square$

**Caution.** The words *unit* and *inverse* must be used with the multiplication of this group and not with the plain product of the algebra. The algebra $\mathbb{B}$ has a group of units, the elements of nonzero norm $N(\tilde P) \neq 0$, and its unit group is $GL_2(\mathbb{C})$ through the matrix realization, with the norm-one subgroup $SL_2(\mathbb{C})$ (*Biquaternion 2×2 Matrix Element Representation*, *Biquaternion Ideals and Peirce Decomposition*); that group belongs to the plain product and to the algebra, not to $\star$. An element such as an idempotent $\tilde\Pi(\mu)$ of *Idempotents of the Quaternionic Sesquilinear Product* is a unit of the algebra and not a unit of the multiplication, and it satisfies $\tilde\Pi \star \tilde\Pi = \tilde\Pi$ all the same.

## The Two Actions and the Derived-Operation Test

### The First Row of the Product

**Definition.** The **first row** of the multiplication is the map

$$
\sigma(\tilde Y) = e_0 \star \tilde Y = \tilde Y^{*} ,
$$

obtained by holding the first argument at $e_0$, in the notation of *Sesqualgebras* §*The Standard Example*.

By the first proposition above, the first row of the multiplication is the star conjugation.

### The Two Conditions

The general theory asks whether a sesquilinear product is the **derived operation** $x \star y = xy^{*}$ of an associative algebra with a conjugate-linear involution. It is exactly then that the first row is such an involution and rebuilds the product; stated as in *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$* §*Which of the Four Is a Sesquilinear Multiplication* and in *Sesqualgebras* §*The Standard Example*, the two conditions are:

(i) $\sigma$ is a conjugate-linear involution of the algebra: $\sigma(\lambda\tilde Y) = \bar\lambda\,\sigma(\tilde Y)$, $\sigma^{2} = \mathrm{id}$, $\sigma(\tilde X\tilde Y) = \sigma(\tilde Y)\sigma(\tilde X)$ and $\sigma(e_0) = e_0$;

(ii) $\sigma$ rebuilds the product: $\tilde X \star \tilde Y = \tilde X\,\sigma(\tilde Y)$ for all $\tilde X, \tilde Y$.

**Theorem (the first row passes one condition and fails the other).** For the complex quaternionic sesquilinear product, $\sigma = {}^{*}$ satisfies condition (i) and fails condition (ii); consequently the product is not the derived operation of the algebra with any involution.

**Proof.** Condition (i): the star conjugation is conjugate-linear, involutive, anti-multiplicative and fixes $e_0$, which is the statement that it is the involution of the derived operation (*The Group of Involutions*, *Biquaternions as a General Plain Algebra (GPA) over $\mathbb{C}$*). So (i) holds. Condition (ii) with $\sigma = {}^{*}$ would read $\tilde X^{\natural}\tilde Y^{*} = \tilde X\tilde Y^{*}$ for all $\tilde X, \tilde Y$; at $\tilde Y = e_0$ this is $\tilde X^{\natural} = \tilde X$ for every $\tilde X$, which fails at $\tilde X = e_1$, where the two sides are $-e_1$ and $e_1$. So (ii) fails. $\square$

**Remark.** The failure of (ii) is the absence of a right unit, read in the second slot: with $\tilde Y = e_0$, condition (ii) says $\tilde X \star e_0 = \tilde X\sigma(e_0) = \tilde X$, that is $\tilde X^{\natural} = \tilde X$ for every $\tilde X$, which is exactly the statement that $e_0$ is a right unit of the multiplication. The two forms of the same failure are the derived-operation test and the right-unit test, and the theorem is their equivalence for this product.

### The Isotope Reading

**Corollary.** The product is the **isotope** of the derived operation by the natural conjugation,

$$
\tilde P \star \tilde Q = {}^{\natural}(\tilde P)\,\tilde Q^{*} = \tilde P^{\natural}\tilde Q^{*} ,
$$

the insertion being in the first slot and the derived operation being $\tilde P\tilde Q^{*}$ with its star involution.

**Proof.** The formula is the rule. The map ${}^{\natural}$ is a $\mathbb{C}$-linear anti-automorphism and a bijection of $\mathbb{B}$, and an isotope of an operation by a bijection $\varphi$ is the operation $(x,y) \mapsto \varphi(x)\,y$; here $\varphi = {}^{\natural}$. $\square$

**Remark.** The two sesquilinear products of the four are the derived operation and its ${}^{\natural}$-isotope, exactly as the two bilinear products of the four are the plain multiplication and its ${}^{\natural}$-isotope; in each pair the second is the first with the $\mathbb{C}$-linear insertion the derived-operation test rejects (*Comparison Between the Four Biquaternion Products* §*Which of the Four Is a Multiplication*, *Biquaternions as a General Quaternionic Sesqualgebra (GQS) over $\mathbb{C}$* §*The Isotope Reading*). The absence of a unit in the second member of each pair is the price of the insertion: the derived operation keeps the right unit $e_0$, and its isotope loses it in the first slot.

## The Actions on the Six Subspaces

The six distinguished subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_{+}$ and the anti-Hermitian subspace $\mathbb{M}_{-}$ (*Introduction to the Six Subspaces*). Each of the two conjugations preserves each of the six (*The Six Subspaces and the Four Complex Products* §*The four products have the same value set*), so each action of $e_0$ restricts to each subspace, and the two restrictions are computed below.

**Theorem (the two actions on the six subspaces).**

| subspace | left action $e_0 \star \cdot = {}^{*}$ | right action $\cdot \star e_0 = {}^{\natural}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $A e_0 \mapsto \bar A e_0$ | identity |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbf Q \mapsto -\overline{\mathbf Q}$ | $\mathbf Q \mapsto -\mathbf Q$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\tilde Q \mapsto \tilde Q^{\natural}$ | $\tilde Q \mapsto \tilde Q^{\natural}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\tilde Q \mapsto -\tilde Q^{\natural}$ | $\tilde Q \mapsto \tilde Q^{\natural}$ |
| $\mathbb{M}_{+}$ | identity | $\tilde Q \mapsto \tilde Q^{\natural}$ |
| $\mathbb{M}_{-}$ | $-\mathrm{id}$ | $\tilde Q \mapsto \tilde Q^{\natural}$ |

**Proof.** The left column is the star conjugation, $Q^{*}_0 = \overline{Q_0}$ and $Q^{*}_k = -\overline{Q_k}$; the right column is the natural conjugation, $\tilde Q^{\natural} = Q_0 - \mathbf Q$.

- On the centre, $\mathbf Q = 0$, so ${}^{*}$ is the coefficientwise conjugation of the single coordinate and ${}^{\natural}$ fixes the element.
- On the vector subspace, $Q_0 = 0$, so ${}^{*}$ sends $\mathbf Q$ to $-\overline{\mathbf Q}$ and ${}^{\natural}$ sends it to $-\mathbf Q$.
- On the quaternion subspace the coordinates are real, so the coefficientwise conjugation is the identity and the two conjugations coincide, both negating the vector part: this is the quaternionic conjugation of the real quaternion subspace.
- On the anti-quaternion subspace write $\tilde Q = i\tilde K$ with $\tilde K$ in the quaternion subspace, so that $\tilde K^{*} = \tilde K^{\natural}$ there and the star is conjugate-linear while ${}^{\natural}$ is $\mathbb{C}$-linear: $\tilde Q^{*} = (i\tilde K)^{*} = -i\,\tilde K^{*} = -i\,\tilde K^{\natural} = -(i\tilde K)^{\natural} = -\tilde Q^{\natural}$, while the right action is $\tilde Q^{\natural}$.
- On the Hermitian subspace, ${}^{*}$ is the identity by definition, and ${}^{\natural}$ fixes the real scalar coordinate and negates the imaginary vector coordinate, $\tilde Q = a_0 + i\mathbf p \mapsto a_0 - i\mathbf p$, which stays in $\mathbb{M}_{+}$.
- On the anti-Hermitian subspace, ${}^{*}$ is $-\mathrm{id}$ by definition, and ${}^{\natural}$ fixes the imaginary scalar coordinate and negates the real vector coordinate, $\tilde Q = i b_0 + \mathbf q \mapsto i b_0 - \mathbf q$, which stays in $\mathbb{M}_{-}$. $\square$

**Remark.** Two entries are the identity, and each is instructive. The left action is the identity on the Hermitian subspace, because that is the fixed space of ${}^{*}$; the right action is the identity on the centre, because the natural conjugation does not touch a scalar element; and no action is the identity on all of $\mathbb{B}$, which is the absence of a unit in its subspace form. The table also shows where the two actions agree, on $\mathbb{H}_{\mathbb{B}}$, and where they differ by a sign, on $i\mathbb{H}_{\mathbb{B}}$ and on $\mathbb{M}_{\pm}$.

## The Unit Candidate as an Idempotent

### The Element $e_0$ Is an Idempotent of the Multiplication

**Proposition.** The unit candidate is an idempotent of the multiplication, $e_0 \star e_0 = e_0$, and both actions fix it.

**Proof.** By the rule, $e_0 \star e_0 = e_0^{\natural}e_0^{*} = e_0e_0 = e_0$, the two conjugations fixing the identity and the identity being the unit of the plain product. The two actions fix $e_0$ by the same computation. $\square$

**Remark.** The element $e_0$ is the **trivial** idempotent of the multiplication, the one the nontrivial idempotents of *Idempotents of the Quaternionic Sesquilinear Product* are contrasted with; unlike them it is central, and it is the unit of the plain product. It is therefore the cleanest single witness that the two notions of unit differ: it is a unit of the algebra, and it is not a unit of $\star$ because it acts by the two conjugations.

### The Two Actions and the Norm

**Proposition.** For every biquaternion $\tilde Q$,

$$
N\bigl(e_0 \star \tilde Q\bigr) = N(\tilde Q^{*}) = \overline{N(\tilde Q)} , \qquad N\bigl(\tilde Q \star e_0\bigr) = N(\tilde Q^{\natural}) = N(\tilde Q) .
$$

The left action conjugates the norm and the right action preserves it; both preserve its modulus $\lvert N\rvert$ and hence the zero-divisor cone $\{N = 0\}$.

**Proof.** The norm is multiplicative for the plain product with $N(e_0) = 1$; it is invariant under the natural conjugation, $N(\tilde Q^{\natural}) = N(\tilde Q)$, because ${}^{\natural}$ negates an even number of coordinates with the square; and it transforms by the coefficientwise conjugation under ${}^{*}$, $N(\tilde Q^{*}) = \overline{N(\tilde Q)}$, because ${}^{*}$ conjugates each coordinate and $N$ is a quadratic form in the coordinates with real coefficients. The two actions are ${}^{*}$ and ${}^{\natural}$. $\square$

**Remark.** The two transforms are the numerical trace of the two parities of the actions: the conjugate-linear action conjugates the quadratic form and the linear action fixes it, and the composite, the coefficientwise conjugation, is the Galois action of $\mathbb{C}$ over $\mathbb{R}$ that distinguishes them. The preservation of the modulus is the reason the two actions are symmetries of the zero-divisor cone $N = 0$, the set on which the element theory of the product is read, and it is why an element and its two conjugates are zero divisors together.

## The Consequences of the Absence

### The Notions That Have to Be Replaced

With no unit, the derived vocabulary of an algebra has to be replaced, and the group names the replacements as they are used.

- **The group of units** does not exist for the multiplication; the algebra's group of units is a different group, belonging to the plain product, and is the subject of *Biquaternion Ideals and Peirce Decomposition*. The elements of the multiplication that are units of the algebra are distinguished by the norm, and for the idempotents this is *Idempotents of the Quaternionic Sesquilinear Product*.
- **The inverse** is replaced by the involution: the closest substitute for an inverse, given that $\tilde P\tilde P^{\natural} = N(\tilde P)e_0$ and the product twists each slot by a conjugation, is the operation of the two conjugations themselves. Each nontrivial idempotent, for example, has inverse its own natural conjugate in the algebra, $\tilde\Pi^{-1} = \tilde\Pi^{\natural}$, although that inverse is not an inverse of the multiplication.
- **One-sided identities** are not available, and the binary structure has to be replaced by the **ternary product**, which is the later article of this group *The Ternary Product and the Failure of the Jordan Triple Identity*. The definition of that ternary product, $\{ \tilde P,\tilde Q,\tilde R \} = (\tilde P \star \tilde Q) \star \tilde R^{*}$, itself uses the star conjugation in the third slot, so the involution that obstructs the unit is the involution that builds the ternary structure.
- **The left multiplications** do not form a monoid, and the composition laws are the later article *The Left and Right Multiplications of the Quaternionic Sesquilinear Product*; the present article supplies the negative statement that makes those laws necessary.

### The Comparison with the Sibling Products

**Theorem (the unit row of the four products).**

| product | left unit | right unit |
|---|---|---|
| $\tilde P\tilde Q$ | $e_0$ | $e_0$ |
| $\tilde P^{\natural}\tilde Q$ | $e_0$ | none |
| $\tilde P\tilde Q^{*}$ | none | $e_0$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | none | none |

**Proof.** The plain product is the associative product of the algebra and has the two-sided unit $e_0$. For the sibling bilinear product, $e_0 \star \tilde Y = e_0^{\natural}\tilde Y = \tilde Y$ because ${}^{\natural}$ fixes $e_0$, so $e_0$ is a left unit, and there is no right one (*Biquaternions as a General Quaternionic Algebra (GQA) over $\mathbb{C}$* §*The Unit*). For the sibling sesquilinear product, $\tilde Y \star e_0 = \tilde Y\tilde e_0^{*} = \tilde Y$, so $e_0$ is a right unit, and there is no left one (*Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$* §*The Right Unit*). The fourth row is the two theorems of this article, in the form that both actions of $e_0$ are conjugations and neither is the identity. $\square$

**Remark.** The four rows are the sharpest reading of the two slots. Each of the four products makes one of the two slots the identity and the other slot the twist: the two bilinear products put the twist in the first slot and the identity in the second, one of them losing the right unit and the other the left; the sibling sesquilinear product has the twist in the second slot and the identity in the first, keeping the right unit; and this product puts a twist in both slots, keeping neither. The table is the unit row of the comparison of the four products, *Comparison Between the Four Biquaternion Products*, read with the two actions of this article.

## Summary

The two one-sided actions of $e_0$ under the complex quaternionic sesquilinear multiplication $\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*}$ are the two conjugations of the algebra: the left action is the star, $e_0 \star \tilde Q = \tilde Q^{*}$, and the right action is the natural conjugation, $\tilde Q \star e_0 = \tilde Q^{\natural}$. Both actions are involutions of $\mathbb{B}$, they commute, and together with the identity and their composite, the coefficientwise conjugation, they form the group of involutions, the Klein four-group. Their consequence is that the multiplication has no unit on either side: a left-unit candidate is forced by the right action to $e_0$ and then rejected by the left action at $e_1$, and a right-unit candidate is forced by the left action to $e_0$ and then rejected by the right action at $e_1$; hence there is no two-sided unit, no inverse and no group of units of the multiplication, and the group of units of the algebra is a different group belonging to the plain product. On the derived-operation test the first row of the multiplication is the star conjugation, which satisfies condition (i) and fails condition (ii), so the multiplication is the isotope of the derived operation by the natural conjugation and not the derived operation itself. On the six distinguished subspaces the two actions restrict to the coefficientwise conjugation, the negation with a conjugation, the quaternionic conjugation, a sign, the identity and a reflection, and no one of them is the identity on all of $\mathbb{B}$. The unit candidate is itself the trivial idempotent of the multiplication, $e_0 \star e_0 = e_0$, and its two actions transform the norm by the character of their parity, $N(e_0 \star \tilde Q) = \overline{N(\tilde Q)}$ and $N(\tilde Q \star e_0) = N(\tilde Q)$, so that both preserve the modulus and the zero-divisor cone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*}$ | the multiplication of this group |
| $e_0 \star \tilde Q = \tilde Q^{*}$ | the left action of $e_0$, the star conjugation |
| $\tilde Q \star e_0 = \tilde Q^{\natural}$ | the right action of $e_0$, the natural conjugation |
| $\bar{\cdot} = {}^{\natural} \circ {}^{*}$ | the coefficientwise conjugation, the composite of the two actions |
| $\{ \mathrm{id}, {}^{\natural}, {}^{*}, \bar{\cdot} \}$ | the group of involutions, the Klein four-group |
| $\sigma(\tilde Y) = e_0 \star \tilde Y = \tilde Y^{*}$ | the first row of the multiplication |
| (i) | $\sigma$ is a conjugate-linear involution of the algebra |
| (ii) | $\tilde X \star \tilde Y = \tilde X\,\sigma(\tilde Y)$ |
| $\tilde P \star \tilde Q = {}^{\natural}(\tilde P)\,\tilde Q^{*}$ | the product as the isotope of the derived operation |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}), \mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_{+}, \mathbb{M}_{-}$ | the six distinguished subspaces |
| $e_0 \star e_0 = e_0$ | the unit candidate as the trivial idempotent of the multiplication |
| $N(e_0 \star \tilde Q) = \overline{N(\tilde Q)}$ | the left action conjugates the norm |
| $N(\tilde Q \star e_0) = N(\tilde Q)$ | the right action preserves the norm |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the one-sided identity, the units of an algebra and the regular actions.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the relation between an involution and the one-sided actions it defines.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the isotopy of a multiplication by an anti-automorphism and the loss of the unit it entails.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the conjugate-linear involutions and the derived operation of an algebra with involution.
