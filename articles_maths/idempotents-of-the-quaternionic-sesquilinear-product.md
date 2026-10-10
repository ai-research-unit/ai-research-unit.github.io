
# __Idempotents of the General Quaternionic Sesquilinear Product__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four general products on its underlying $\mathbb{C}$-vector space, and this article treats the fourth, the **general quaternionic sesquilinear product**

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*} ,
$$

whose rule, scalar–vector form and place among the four general products are the subject of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and whose multiplication table and sesqualgebra axioms are in *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*. The symbolism is that article's: ${}^{\natural}$ is the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$, ${}^{*}$ is the star conjugation $\tilde P^{*} = \overline{P_0} - \overline{\mathbf Q}$, the bar is the coefficientwise complex conjugation, $\mathbf P = \sum_{k=1}^{3} P_k e_k$ is the vector part, and $N(\tilde P) = \tilde P\tilde P^{\natural} = \sum_{\mu} P_\mu^{2}$ is the norm form.

The question of the article is the **idempotent problem** for this multiplication: which elements satisfy $\tilde Q \star \tilde Q = \tilde Q$. The answer is the batch's one positive surprise. The equation has the two obvious solutions $0$ and $e_0$, and beyond them a **two-parameter family** of solutions,

$$
\tilde\Pi(\mu) = -\tfrac12 e_0 + \mu , \qquad \mu \in \mathrm{Vect}(\mathbb{B})_{\mathbb{R}} , \qquad (\mu,\mu) = \tfrac34 ,
$$

each of them of norm $1$ and therefore a unit of the algebra. The family is the only positive element theory in the batch. Every other idempotent attached to the four general products is either trivial or a zero divisor: the idempotents of the plain product are the idempotents of the algebra and the nontrivial ones among them have $N = 0$; the nontrivial idempotents of the sibling general plain sesquilinear product are the rank-one Hermitian idempotents and have $N = 0$ as well; and the sibling general quaternionic bilinear product has only $0$ and $e_0$. Only this product has nontrivial idempotents, and only its nontrivial idempotents are units.

The article owns the criterion, the classification, the family and the unit property. It does not repeat the rule of the product, which is *The Four General Products of the Biquaternion $\mathbb{C}$ Space* §*The General Quaternionic Sesquilinear Product*; it uses the criterion of the plain product's idempotents, which is *Idempotents of the General Plain Algebra*, and the classification of the zero divisors, which is *Zero Divisors of the General Plain Algebra*; it cites the row of the comparison table that records the four idempotent sets, which is *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*; and it does not treat the square of a general element, the square-zero elements, or the operators of the multiplication, which are the subjects of the later articles of this group, *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* and *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*.

## The Idempotent Equation

### The Criterion

**Definition.** An element $\tilde\Pi$ is **idempotent** for the multiplication when $\tilde\Pi \star \tilde\Pi = \tilde\Pi$.

**Proposition (the criterion).** An element $\tilde Q$ is idempotent if and only if

$$
\overline{\tilde Q}\,\tilde Q = \tilde Q^{\natural} .
$$

**Proof.** The equation $\tilde Q \star \tilde Q = \tilde Q$ reads $\tilde Q^{\natural}\tilde Q^{*} = \tilde Q$. The map ${}^{\natural}$ is an involution and an anti-automorphism of the plain product, and $(\tilde Q^{*})^{\natural} = \overline{\tilde Q}$ because the two conjugations commute and ${}^{*} = \overline{\cdot} \circ {}^{\natural}$. Applying ${}^{\natural}$ to the equation therefore gives

$$
\bigl(\tilde Q^{\natural}\tilde Q^{*}\bigr)^{\natural}
= (\tilde Q^{*})^{\natural}\,(\tilde Q^{\natural})^{\natural}
= \overline{\tilde Q}\,\tilde Q = \tilde Q^{\natural} ,
$$

which is the criterion. Conversely, applying ${}^{\natural}$ to the criterion returns the original equation, so the two are equivalent. $\square$

The criterion is the form in which the equation is read on the coordinates, since the left-hand side is a plain product and the right-hand side a conjugation, and it is the form the group article uses.

### The Equation on the Coordinates

**Proposition (the coordinate equations).** Write $\tilde Q = Q_0 + \mathbf Q$ with $\mathbf Q = \mathbf a + i\mathbf b$, where $\mathbf a$ and $\mathbf b$ are vectors with real coefficients. Then $\tilde Q$ is idempotent if and only if

$$
Q_0 \in \mathbb{R} , \qquad Q_0 = \lvert Q_0\rvert^{2} - \sum_{k=1}^{3}\lvert Q_k\rvert^{2} , \qquad (2Q_0 + 1)\mathbf a = 0 , \qquad \mathbf a \times \mathbf b = -\tfrac12 \mathbf b .
$$

**Proof.** The left-hand side of the criterion is the plain product of $\overline{\tilde Q} = \overline{Q_0} + \overline{\mathbf Q}$ and $\tilde Q = Q_0 + \mathbf Q$, whose scalar–vector form is that of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*,

$$
\overline{\tilde Q}\,\tilde Q = \overline{Q_0}Q_0 - (\overline{\mathbf Q},\mathbf Q) + \overline{Q_0}\mathbf Q + Q_0\overline{\mathbf Q} + \overline{\mathbf Q}\times\mathbf Q ,
$$

the dot and cross products being the general plain bilinear ones. The right-hand side is $\tilde Q^{\natural} = Q_0 - \mathbf Q$. Equating scalar parts gives $Q_0 = \lvert Q_0\rvert^{2} - \sum_{k}\lvert Q_k\rvert^{2}$, which exhibits $Q_0$ as the difference of two real numbers and hence real; writing $Q_0 = u \in \mathbb{R}$ and $\mathbf Q = \mathbf a + i\mathbf b$, the same equation is the second displayed relation. Equating vector parts gives $\overline{Q_0}\mathbf Q + Q_0\overline{\mathbf Q} + \overline{\mathbf Q}\times\mathbf Q = -\mathbf Q$, that is

$$
u(\mathbf Q + \overline{\mathbf Q}) + \overline{\mathbf Q}\times\mathbf Q = -\mathbf Q ,
$$

using $Q_0 = u$ real. Now $\mathbf Q + \overline{\mathbf Q} = 2\mathbf a$ and $\overline{\mathbf Q}\times\mathbf Q = (\mathbf a - i\mathbf b)\times(\mathbf a + i\mathbf b) = 2i\,\mathbf a\times\mathbf b$, the two real cross terms cancelling and the two mixed terms doubling. Substituting and separating the real and the imaginary coefficients of the vector equation gives $2u\mathbf a = -\mathbf a$ and $2\mathbf a\times\mathbf b = -\mathbf b$, which are the last two displayed relations. $\square$

The two vector relations are of different kinds: the first constrains $\mathbf a$ alone, the second couples $\mathbf a$ and $\mathbf b$ through the cross product.

## The Classification

### The Two Trivial Idempotents

**Proposition.** The elements $0$ and $e_0$ are idempotent, and they are the only idempotents with vanishing vector part.

**Proof.** Directly, $0 \star 0 = 0$ and $e_0 \star e_0 = e_0^{\natural}e_0^{*} = e_0$. Conversely let $\tilde Q = Q_0 e_0$ be a scalar element, so that $\mathbf a = \mathbf b = 0$. The coordinate equations reduce to $Q_0 \in \mathbb{R}$ and $Q_0 = Q_0^{2}$, whose solutions are $Q_0 = 0$ and $Q_0 = 1$. $\square$

### The Family

**Theorem (the classification).** The idempotents of the multiplication are exactly

$$
0 , \qquad e_0 , \qquad\text{and}\qquad \tilde\Pi(\mu) = -\tfrac12 e_0 + \mu , \qquad \mu \in \mathrm{Vect}(\mathbb{B})_{\mathbb{R}} , \qquad (\mu,\mu) = \tfrac34 .
$$

**Proof.** Let $\tilde Q$ be idempotent and write $\tilde Q = u + \mathbf a + i\mathbf b$ as above. The proof splits on whether the real vector $\mathbf a$ vanishes.

Suppose first that $\mathbf a \neq 0$. The relation $(2u+1)\mathbf a = 0$ forces $u = -\tfrac12$. The relation $\mathbf a\times\mathbf b = -\tfrac12\mathbf b$ says that $\mathbf b$ lies in the kernel of the operator $\mathbf x \mapsto \mathbf a\times\mathbf x + \tfrac12\mathbf x$, that is, that $\mathbf b$ is a kernel vector of $L_{\mathbf a} + \tfrac12 I$ with $L_{\mathbf a}\mathbf x = \mathbf a\times\mathbf x$. The operator $L_{\mathbf a}$ is antisymmetric with respect to the real definite structure, since $(\mathbf a\times\mathbf x,\mathbf y) = -(\mathbf x,\mathbf a\times\mathbf y)$; an antisymmetric real operator has purely imaginary spectrum, together with the eigenvalue $0$, so $L_{\mathbf a} + \tfrac12 I$ has spectrum $\{ \tfrac12 \} \cup \{ \tfrac12 \pm i\lvert \mathbf a\rvert \}$, which does not contain $0$. Hence $L_{\mathbf a} + \tfrac12 I$ is invertible and $\mathbf b = 0$. The coordinate equation $u = u^{2} - \lvert\mathbf Q\rvert^{2}$ then gives $\lvert\mathbf Q\rvert^{2} = u^{2} - u = \tfrac14 + \tfrac12 = \tfrac34$, that is $(\mu,\mu) = \tfrac34$ for $\mu = \mathbf Q = \mathbf a$. This is the family.

Suppose next that $\mathbf a = 0$. The relation $(2u+1)\mathbf a = 0$ is vacuous, and the relation $\mathbf a\times\mathbf b = -\tfrac12\mathbf b$ reads $\mathbf b = 0$. Then $\mathbf Q = 0$ and the coordinate equation gives $u = u^{2}$, that is $u = 0$ or $u = 1$. These are the two trivial idempotents. $\square$

**Remark.** The theorem classifies the idempotents of the whole algebra. The group article *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* states the classification on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where the coefficients are real and the criterion reads $\tilde Q^{2} = \tilde Q^{\natural}$; the two statements agree, and every nontrivial idempotent lies in that subspace, since the family has real coordinates. No idempotent has a nonzero imaginary part of the scalar coordinate and none has a non-real component in the vector coordinates.

### The Norm of an Idempotent

**Proposition.** Every nontrivial idempotent has norm $1$,

$$
N\bigl(\tilde\Pi(\mu)\bigr) = \tfrac14 + (\mu,\mu) = 1 ,
$$

and hence is a unit of the algebra, with inverse its own natural conjugate, $\tilde\Pi(\mu)^{-1} = \tilde\Pi(\mu)^{\natural} = -\tfrac12 e_0 - \mu$. The two trivial idempotents have norms $N(0) = 0$ and $N(e_0) = 1$.

**Proof.** The norm of $\tilde\Pi(\mu)$ is $\lvert-\tfrac12\rvert^{2} + (\mu,\mu) = \tfrac14 + \tfrac34 = 1$. An element of norm $1$ is a unit because $\tilde P\tilde P^{\natural} = N(\tilde P)e_0 = e_0$, and $\tilde\Pi(\mu)^{\natural} = -\tfrac12e_0 - \mu$ by the linearity of ${}^{\natural}$. The values for $0$ and $e_0$ are immediate. $\square$

The proposition is the sharpest difference of this multiplication from its three companions. Among the four general products, only this one has a nontrivial idempotent, and the nontrivial idempotents of the other three are degenerate in a way the norm detects: they are zero divisors.

## The Idempotents of the Other Multiplications

### The Idempotents of the Plain Product

The idempotents of the plain product $\tilde P\tilde Q$ are the idempotents of the algebra, classified in *Idempotents of the General Plain Algebra*: the elements $\tfrac12(e_0 + \xi i)$ with $\xi$ a root of $-e_0$, that is a pure quaternion $\xi$ with $\xi^{2} = -e_0$, together with $0$ and $e_0$. They fall into the Hermitian family, where $\xi$ is a real unit vector, and the non-Hermitian family, where it is not.

**Proposition.** Every nontrivial idempotent of the plain product is a zero divisor and is not a unit.

**Proof.** Let $\tilde\Pi = \tfrac12(e_0 + \xi i)$ with $\xi^{2} = -e_0$. Its norm is

$$
N(\tilde\Pi) = \Bigl(\tfrac12\Bigr)^{2} + \sum_{k=1}^{3}\Bigl(\tfrac{i}{2}\xi_k\Bigr)^{2} = \tfrac14 - \tfrac14 \sum_{k=1}^{3}\xi_k^{2} = \tfrac14 - \tfrac14 \cdot 1 = 0 ,
$$

since $\xi$ is a unit pure quaternion and $(\xi,\xi) = 1$. The element is nonzero of norm $0$, so by the criterion of *Zero Divisors of the General Plain Algebra* it is a zero divisor and not a unit. $\square$

**Remark.** The family $\tfrac12(e_0 + \xi i)$ is therefore the exact opposite of the family of this article: it is infinite and it consists entirely of zero divisors, whereas the family is infinite and consists entirely of units. The plain product and this one have their idempotents disjoint except for the two trivial ones, and the difference is carried by the sign of the vector contribution to the norm.

### The Idempotents of the Sibling Sesquilinear Product

The sibling general plain sesquilinear product $\tilde P\tilde Q^{*}$ is the derived operation of the algebra with its star conjugation (*Introduction to the General Plain Sesqualgebra of Biquaternions*). Its idempotents are exactly the Hermitian idempotents of the algebra,

$$
\tilde\Pi_1(\hat\mu) = \tfrac12\bigl(e_0 + i\hat\mu\bigr) , \qquad \hat\mu \in \mathbb{R}^{3} , \quad \lvert\hat\mu\rvert = 1 ,
$$

the pure states of *Idempotents of the General Plain Algebra*.

**Proposition.** Every nontrivial idempotent of the sibling sesquilinear product is isotropic for this multiplication,

$$
\tilde\Pi_1(\hat\mu) \star \tilde\Pi_1(\hat\mu) = 0 .
$$

**Proof.** Let $\tilde H = \tfrac12(e_0 + i\hat\mu)$ with $\hat\mu$ a real unit vector; it is Hermitian, $\tilde H^{*} = \tilde H$, and its coordinates are $H_0 = \tfrac12$, $H_k = \tfrac{i}{2}\hat\mu_k$. Its norm is $N(\tilde H) = \tfrac14 - \tfrac14\sum_k\hat\mu_k^{2} = 0$, as for the plain product. For a Hermitian element $\overline{\tilde H} = \tilde H^{\natural}$, and the square of the multiplication is $(\overline{\tilde H}\tilde H)^{\natural}$ up to the identity of the next article of this group, *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*; here the direct computation is closed: $\tilde H \star \tilde H = \tilde H^{\natural}\tilde H^{*} = \tilde H^{\natural}\tilde H = N(\tilde H)e_0 = 0$, the $\natural$-product of an element with its conjugate being the central scalar $N(\tilde H)e_0$ (*Introduction to the General Quaternionic Algebra of Biquaternions* §*The Square and the Elements It Distinguishes*). $\square$

**Remark.** The sibling's idempotents are therefore not idempotents here, and they fail in the strongest possible way: their square in the multiplication vanishes. The two families of idempotents are the two fixed points of the same involution rule read in the two sesquilinear products, and the insertion of the natural conjugation in the first slot transposes them into square-zero elements.

### The Idempotents of the Sibling Bilinear Product

The sibling general quaternionic bilinear product $\tilde P^{\natural}\tilde Q$ has the two trivial idempotents alone,

$$
\tilde Q \star \tilde Q = \tilde Q \iff \tilde Q = 0 \ \text{or}\ \tilde Q = e_0 ,
$$

because its square is the central scalar $\bigl(\sum_\mu Q_\mu^{2}\bigr)e_0$ (*Introduction to the General Quaternionic Algebra of Biquaternions* §*The Square and the Elements It Distinguishes*). This is the smallest idempotent set of the four, and it is the one that agrees with the second row of the comparison table.

### The Comparison

**Theorem (the four idempotent sets).** The four general products have four different idempotent sets, and only the fourth has nontrivial idempotents that are units:

| product | idempotents | nontrivial idempotents are |
|---|---|---|
| $\tilde P\tilde Q$ | $0$, $e_0$, and $\tfrac12(e_0 + \xi i)$ for a root $\xi$ of $-e_0$ | zero divisors |
| $\tilde P^{\natural}\tilde Q$ | $0$ and $e_0$ | — |
| $\tilde P\tilde Q^{*}$ | $0$, $e_0$, and the Hermitian idempotents $\tfrac12(e_0 + i\hat\mu)$ | zero divisors |
| $\tilde P^{\natural}\tilde Q^{*}$ | $0$, $e_0$, and the family $-\tfrac12 e_0 + \mu$ with $(\mu,\mu) = \tfrac34$ | units, of norm $1$ |

**Proof.** The four rows are the propositions above and the statement of the classification theorem; the last column is the norm computation for each family, $N = 0$ for the nontrivial idempotents of the plain and of the sibling sesquilinear product and $N = 1$ for the family. The table is the idempotent row of *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*, read with the norm attached to each entry. $\square$

**Remark.** The table is the reason the idempotent problem is the sharpest of the four element problems. The zero divisors are one set for all four general products (*The Annihilating Elements of the Four General Products*, being written in parallel), and the square-zero elements are already two different problems for the four; but the idempotents are four sets, no two of which agree beyond $0$ and $e_0$, and the fourth alone is a family of units.

## The Family of Idempotents

### The Parametrisation

The family of idempotents is the affine translate by $-\tfrac12 e_0$ of the set $(\mu,\mu)=\tfrac34$ in the real three-dimensional vector subspace. Writing a real unit vector as

$$
\hat\mu = \sin\theta\cos\varphi\, e_1 + \sin\theta\sin\varphi\, e_2 + \cos\theta\, e_3 , \qquad \theta \in [0,\pi] , \quad \varphi \in [0,2\pi) ,
$$

every nontrivial idempotent is

$$
\tilde\Pi(\theta,\varphi) = -\tfrac12 e_0 + \tfrac{\sqrt3}{2}\Bigl( \sin\theta\cos\varphi\, e_1 + \sin\theta\sin\varphi\, e_2 + \cos\theta\, e_3 \Bigr) .
$$

The three coordinate-axial idempotents are the elements with $\mu$ along one basis vector:

$$
-\tfrac12 e_0 \pm \tfrac{\sqrt3}{2} e_1 , \qquad -\tfrac12 e_0 \pm \tfrac{\sqrt3}{2} e_2 , \qquad -\tfrac12 e_0 \pm \tfrac{\sqrt3}{2} e_3 .
$$

They are the six intersection points of the family with the coordinate axes, and they are the simplest nonrational elements of the family.

### Worked Elements

**Example.** Let $\tilde\Pi = -\tfrac12 e_0 + \tfrac{\sqrt3}{2} e_1$. Its square in the plain product is

$$
\tilde\Pi^{2} = \Bigl(\tfrac14 - \tfrac34\Bigr) e_0 + 2\cdot\Bigl(-\tfrac12\Bigr)\cdot\tfrac{\sqrt3}{2} e_1 = -\tfrac12 e_0 - \tfrac{\sqrt3}{2} e_1 = \tilde\Pi^{\natural} ,
$$

and $\tilde\Pi^{2} = -\tfrac12 e_0 - \tfrac{\sqrt3}{2} e_1$ is not $\tilde\Pi$, so the element is not idempotent for the plain product. For the multiplication of this article it is: the coordinates are real, so $\overline{\tilde\Pi} = \tilde\Pi$ and the criterion reads $\overline{\tilde\Pi}\tilde\Pi = \tilde\Pi^{2} = \tilde\Pi^{\natural}$, which is satisfied. Directly, $\tilde\Pi \star \tilde\Pi = \tilde\Pi^{\natural}\tilde\Pi^{*} = \bigl(\tilde\Pi^{\natural}\bigr)^{2} = \tilde\Pi$, since $\tilde\Pi^{*} = \tilde\Pi^{\natural}$ for a real element and the square of the natural conjugate returns the element. Its norm is $N = \tfrac14 + \tfrac34 = 1$.

**Example.** Let $\tilde\Pi = -\tfrac12 e_0 + \tfrac{\sqrt3}{2}\hat\mu$ with $\hat\mu = \tfrac{3}{5}e_1 + \tfrac{4}{5}e_2$ a real unit vector. Then $\tilde\Pi^{2} = \tilde\Pi^{\natural} = -\tfrac12 e_0 - \tfrac{\sqrt3}{2}\hat\mu$, and the same reading shows the idempotence. The example is the general one: idempotence depends only on $\hat\mu$ and not on the choice of the two transversal directions.

### The Automorphisms of the Family

**Proposition.** The group of unit quaternions acts transitively on the family of idempotents by conjugation.

**Proof.** Let $\tilde U$ be a unit of the quaternion subspace, $\tilde U \in \mathbb{H}_{\mathbb{B}}$ with $N(\tilde U) = 1$; conjugation by $\tilde U$ in the quaternion division algebra is a rotation $\rho$ of the real vector subspace. Conjugation is a $\mathbb{C}$-algebra automorphism of the plain product, it commutes with both conjugations ${}^{\natural}$ and ${}^{*}$, and it therefore commutes with the multiplication $\star$ by the rule $\tilde U(\tilde X \star \tilde Y)\tilde U^{-1} = (\tilde U\tilde X\tilde U^{-1}) \star (\tilde U\tilde Y\tilde U^{-1})$. Reading this on the criterion shows that it preserves the idempotent set and maps $\tilde\Pi(\mu)$ to $\tilde\Pi(\rho\mu)$. Since the rotations act transitively on the set $(\mu,\mu) = \tfrac34$, the action on the idempotent family is transitive. $\square$

**Remark.** The idempotent family is therefore a single orbit of the rotation group, and the homomorphism from the unit quaternions onto $SO(3)$ of *Quaternion Rotations and Reflections* is its structure group. The two trivial idempotents are the fixed points of the action, since a $\mathbb{C}$-algebra automorphism fixes $0$ and $e_0$.

## The Hermitian Subspace and the Family

The family lies in the quaternion subspace and outside the Hermitian subspace, and this is worth isolating because it is the source of the contrast with the sibling product.

**Proposition.** A nontrivial idempotent is not Hermitian,

$$
\tilde\Pi(\mu)^{*} = -\tfrac12 e_0 - \mu \neq -\tfrac12 e_0 + \mu = \tilde\Pi(\mu)
$$

for $\mu \neq 0$, and it is not skew-Hermitian either.

**Proof.** The element $\tilde\Pi(\mu)$ has real coordinates, so $\overline{\tilde\Pi(\mu)} = \tilde\Pi(\mu)$ and $\tilde\Pi(\mu)^{*} = \tilde\Pi(\mu)^{\natural} = -\tfrac12 e_0 - \mu$. This differs from $\tilde\Pi(\mu)$ exactly when $\mu \neq 0$, and it differs from $-\tilde\Pi(\mu) = \tfrac12 e_0 - \mu$ because the scalar coordinates $\pm\tfrac12$ do not vanish. $\square$

**Remark.** The Hermitian subspace $\mathbb{M}_{+}$ is where the sibling product finds its idempotents and where this product finds none beyond the centre; the family of this product is cut out of the quaternion subspace instead, the fixed space of the other conjugation. This is the element-theoretic form of the fact that the two products differ by which slot carries the conjugation, and it is developed into the reading of the two halves in the next article of the group, *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*.

## Summary

The idempotents of the general quaternionic sesquilinear multiplication $\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*}$ are the solutions of $\overline{\tilde Q}\tilde Q = \tilde Q^{\natural}$, equivalently of the four coordinate equations $Q_0 = u \in \mathbb{R}$, $u = u^{2} - \lvert\mathbf Q\rvert^{2}$, $(2u+1)\mathbf a = 0$ and $\mathbf a\times\mathbf b = -\tfrac12\mathbf b$ for $\mathbf Q = \mathbf a + i\mathbf b$. Their complete list is the two trivial idempotents $0$ and $e_0$ together with the family

$$
\tilde\Pi(\mu) = -\tfrac12 e_0 + \mu , \qquad \mu \in \mathrm{Vect}(\mathbb{B})_{\mathbb{R}} , \qquad (\mu,\mu) = \tfrac34 ,
$$

and each non-trivial idempotent has norm $1$, so that it is a unit of the algebra with inverse its own natural conjugate $-\tfrac12 e_0 - \mu$. The family is a single orbit of the rotation group of the quaternion subspace, and it lies outside the Hermitian subspace, since a nontrivial idempotent is neither Hermitian nor skew-Hermitian. The idempotent sets of the four general products are four different sets: the plain product and the sibling sesquilinear product have infinite families of zero divisors, the sibling bilinear product has only the two trivial idempotents, and this product alone has a family of units. The idempotents of the sibling sesquilinear product are isotropic for this multiplication, each of them having square zero, so the two infinite families are disjoint beyond $0$ and $e_0$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear multiplication |
| $\tilde\Pi$ | an idempotent, $\tilde\Pi \star \tilde\Pi = \tilde\Pi$ |
| $\overline{\tilde Q}\tilde Q = \tilde Q^{\natural}$ | the criterion for idempotence |
| $Q_0 = u \in \mathbb{R}$, $u = u^{2} - \lvert\mathbf Q\rvert^{2}$ | the scalar coordinate equations |
| $(2u+1)\mathbf a = 0$, $\mathbf a\times\mathbf b = -\tfrac12\mathbf b$ | the vector coordinate equations, $\mathbf Q = \mathbf a + i\mathbf b$ |
| $\tilde\Pi(\mu) = -\tfrac12 e_0 + \mu$ | a nontrivial idempotent |
| $\mu \in \mathrm{Vect}(\mathbb{B})_{\mathbb{R}}$, $(\mu,\mu) = \tfrac34$ | the parameter and its constraint: a two-dimensional family |
| $\hat\mu = \mu / \lvert\mu\rvert$ | the real unit direction |
| $N(\tilde\Pi(\mu)) = 1$ | every nontrivial idempotent is a unit |
| $\tilde\Pi(\mu)^{-1} = \tilde\Pi(\mu)^{\natural} = -\tfrac12 e_0 - \mu$ | the inverse of a nontrivial idempotent |
| $\tilde\Pi_1(\hat\mu) = \tfrac12(e_0 + i\hat\mu)$ | the idempotents of the sibling sesquilinear product, isotropic here |
| $\rho$ | the rotation of the vector subspace induced by conjugation by a unit quaternion |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for idempotents, units and the relation between the two in a ring.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for idempotents that are fixed by an involution and the projections of a ring with involution.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the idempotent refinement of a ring and the Peirce decomposition it induces.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the classification of idempotents and the role of the fixed ring of an involution.
