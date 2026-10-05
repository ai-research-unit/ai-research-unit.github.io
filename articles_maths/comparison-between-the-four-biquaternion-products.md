# __Comparison Between the Four Biquaternion Products__

## Introduction

The four products of *The Four Biquaternion Complex Products* are four binary rules on the same space, and it is natural to ask which of them deserves the name of multiplication. In the strict sense, of an associative multiplication with a two-sided unit over the field of scalars, only the complex bilinear product does: the second is $\mathbb{C}$-bilinear but not associative and carries a unit on one side only, and the last two are not $\mathbb{C}$-bilinear at all, being conjugate-linear in their second argument. In the sense of the two objects the corpus has — an algebra in the sense of *Algebras*, and a sesquialgebra over $\mathbb{C}$ with its conjugation in the sense of *Sesquialgebras* — the four split two and two, and within the pair of sesquilinear ones the complex product is the one this series takes, being the derived operation of the algebra with the conjugate-linear involution.

This article tabulates the properties that separate the four — bilinearity, associativity, commutativity, the units, the alternative and the flexible identities, the degree-three identity, and the left multiplications — and gives the short computation that decides each entry where it is not immediate. The scalar and vector parts the four induce are not compared here; they are *Relations Between the Four Biquaternion Products*.

The article assumes the four products and their scalar–vector forms from *The Four Biquaternion Complex Products*, and it uses the identities of *Relations Between the Four Biquaternion Products* for the unit and the monoid rows. Throughout, $1=e_0$ is the unit of the algebra and $\mathbf P$ is the vector part of $\tilde P=P_0+\mathbf P$.

## The Property Table

The last two rows are the **algebra rows**, and they are the reason the comparison is made. They ask which of the four products is a multiplication of an algebra of each of the two kinds the corpus has, and each is read with the corpus's own definition of the object and with nothing added to it. **Multiplication of a bilinear $\mathbb{C}$-algebra** is the product of an algebra in the sense of *Algebras*: a $\mathbb{C}$-module with a product additive in each variable and $\mathbb{C}$-bilinear, with no associativity and no unit assumed, so $(\lambda\tilde P)\tilde Q = \lambda(\tilde P\tilde Q)$ and $\tilde P(\lambda\tilde Q) = \lambda(\tilde P\tilde Q)$. **Multiplication of a sesquialgebra over $\mathbb{C}$** is the product of an algebra in the sense of *Sesquialgebras*: additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second, so $(\lambda\tilde P)\tilde Q = \lambda(\tilde P\tilde Q)$ and $\tilde P(\lambda\tilde Q) = \bar\lambda(\tilde P\tilde Q)$, the base involution being the conjugation $\varsigma(z)=\bar z$. The bilinear case is the trivial-involution collapse of the sesquilinear one, so the two kinds overlap in general; they do not overlap here. A product of full type carries only one involution (*Sesquialgebras*, §*The Collapse at the Identity*), and $\mathbb{B}$ is faithful, its products generate it and it has no nonzero left annihilator, so each of the four products carries exactly one involution and lies in exactly one of the two rows.

| property | $\tilde P\tilde Q$ | $\tilde P^{\natural}\tilde Q$ | $\tilde P\tilde Q^{*}$ | $\tilde P^{\natural}\tilde Q^{*}$ |
|---|---|---|---|---|
| $\mathbb{C}$-linear in the first argument | yes | yes | yes | yes |
| $\mathbb{C}$-linear in the second argument | yes | yes | no | no |
| associative | yes | no | no | no |
| commutative | no | no | no | no |
| $1$ is a left identity | yes | yes | no | no |
| $1$ is a right identity | yes | no | yes | no |
| alternative | yes | no | no | no |
| flexible | yes | no | no | no |
| degree-three identity | yes | no | no | no |
| left multiplications form a monoid | yes | yes | no | no |
| multiplication of an algebra over $\mathbb{C}$ | yes | yes | no | no |
| multiplication of a sesquialgebra over $\mathbb{C}$ | no | no | yes | yes |

The alternative row is satisfied automatically by the complex bilinear product, which is associative, and it is the three other columns that the row decides. The degree-three row records the identity $\tilde P(\tilde P\tilde P)=(\tilde P\tilde P)\tilde P$ for the operation in question, which is how power associativity is tested for a product of this kind; in this and the two rows above it, juxtaposition stands for the operation of the row. The last two rows ask which of the four products is a multiplication of an algebra of the two kinds the corpus has, with the definitions of the paragraph above the table and with nothing added to them. The test is the scalar rules alone, and it is decided by the second slot. When the second slot is read without a conjugation, as in $\tilde P\tilde Q$ and in $\tilde P^{\natural}\tilde Q$, the product is $\mathbb{C}$-bilinear and belongs to the bilinear row; when it carries the star, as in $\tilde P\tilde Q^{*}$ and in $\tilde P^{\natural}\tilde Q^{*}$, the product is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second and belongs to the sesquilinear row. The witness for each exclusion is one scalar, $\lambda = i$, and one pair, $\tilde P = \tilde Q = e_0$: for the two bilinear products $\tilde P(i\tilde Q) = ie_0$ while $\bar\imath(\tilde P\tilde Q) = -ie_0$, so they are not $\varsigma$-sesquilinear for the conjugation; and for the two star-products $\tilde P(i\tilde Q) = -ie_0$ while $i(\tilde P\tilde Q) = ie_0$, so they are not $\mathbb{C}$-bilinear. The four therefore split two and two by the involution each carries, the bilinear row reading yes, yes, no, no and the sesquilinear row no, no, yes, yes. Neither row separates the third column from the fourth, and none should: the two star-products differ only in the first slot, and ${}^{\natural}$ is $\mathbb{C}$-linear, so both are sesquilinear for the same conjugation. What separates them is the unit, and it is the row "$1$ is a right identity" above: the complex sesquilinear product has $e_0$ on the right and the complex quaternionic one has not. Equivalently, only the complex sesquilinear product is the **derived operation** $\tilde X\star\tilde Y = \tilde X\tilde Y^{*}$ of $\mathbb{B}$ with its conjugate-linear involution, the standard example of *Sesquialgebras* and the structure of *Biquaternions as a Sesquialgebra over $\mathbb{C}$*. The bilinear row is weakened in the same way by the absence of a qualifier: the sharper statement, that exactly one of the four is the multiplication of an **associative unital** $\mathbb{C}$-algebra, is in *Biquaternions as an Algebra over $\mathbb{C}$*, and it holds because the ${}^{\natural}$-product is neither associative nor two-sidedly unital.

## Bilinearity and Sesquilinearity

The first two rows are read off the definitions. Each of the four products is $\mathbb{C}$-linear in the first argument: the first factor is either untouched or conjugated by the $\mathbb{C}$-linear map ${}^{\natural}$, and the rest of the computation is linear in it. In the second argument, the complex bilinear product and the ${}^{\natural}$-product are $\mathbb{C}$-linear, while the two products carrying the star are conjugate-linear, since ${}^{*}$ conjugates the coefficients of the second factor before the multiplication.

The distinction is not a technicality of the definitions: it separates the two rows of the scalar and vector tables of *The Four Biquaternion Complex Products* that involve $\overline{\mathbf Q}$, and it is the reason the fourth column carries no unit and no monoid. It also settles what the four can be used for. A $\mathbb{C}$-bilinear operation on $\mathbb{B}$ defines on $\mathbb{B}$ the structure of an algebra over $\mathbb{C}$, associative or not; a conjugate-linear operation defines no such thing, and the two sesquilinear products are the multiplications of a sesquialgebra over $\mathbb{C}$ instead. The first of the two is nonetheless the multiplication of a sesquialgebra over $\mathbb{C}$ with its conjugation, being the derived operation of the algebra with the star, and that is a multiplication in the second sense the corpus admits (*Biquaternions as a Sesquialgebra over $\mathbb{C}$*); the second is not, since it reads the first factor through the $\mathbb{C}$-linear ${}^{\natural}$ as well. The four remain binary operations of the same kind, with the same two-step rule for their computation.

## The Failure of Associativity

The complex bilinear product is associative, being the complex-linear extension of the associative quaternion product. The other three products fail it, and each fails it on a triple of basis elements:

$$
(\tilde P^{\natural}\tilde Q)^{\natural}\tilde R\neq\tilde P^{\natural}(\tilde Q^{\natural}\tilde R)
\quad\text{for}\quad \tilde P=\tilde Q=-e_2,\ \tilde R=e_2 ,
$$

where the left-hand side is $e_2$ and the right-hand side is $-e_2$; and

$$
(\tilde P\tilde Q^{*})\tilde R^{*}\neq\tilde P(\tilde Q\tilde R^{*})^{*}
\quad\text{for}\quad \tilde P=-e_3,\ \tilde Q=\tilde R=e_2 ,
$$

where the left-hand side is $e_3$ and the right-hand side is $-e_3$. For the fourth product,

$$
(\tilde P^{\natural}\tilde Q^{*})^{\natural}\tilde R^{*}\neq\tilde P^{\natural}(\tilde Q^{\natural}\tilde R^{*})^{*}
\quad\text{for}\quad \tilde P=-e_3,\ \tilde Q=e_3,\ \tilde R=e_0 ,
$$

with left-hand side $e_0$ and right-hand side $-e_0$. In each case the two sides differ by the sign of a single basis element, and the reason is the same in all three: associativity of the complex bilinear product lets the parentheses be dropped, and the operation then conjugates a factor and so transposes two of them. For the ${}^{\natural}$-product, for instance, $(\tilde P^{\natural}\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P$, so the two sides of the associative identity read $\tilde Q^{\natural}\tilde P\tilde R$ and $\tilde P^{\natural}\tilde Q^{\natural}\tilde R$, which differ by the transposition of $\tilde P$ and $\tilde Q^{\natural}$ alone.

The failure is not repaired by the symmetry of the scalar parts, because that symmetry is a statement about the scalar parts alone. In the first two counterexamples the two sides have the same scalar part, namely zero, and differ in the vector part, and in the third the scalar part changes sign; associativity is a statement about elements, and it is decided on the vector parts.

## Identities and Units

The unit $1=e_0$ of the algebra is a unit for the complex bilinear product on both sides. For the other three the two sides must be asked separately: ${}^{\natural}$ and ${}^{*}$ both fix the unit, $1^{\natural}=1^{*}=1$, but each of the three operations conjugates the other factor.

For the ${}^{\natural}$-product, $1^{\natural}\tilde Q=\tilde Q$, so $1$ is a left identity; and $\tilde P^{\natural}1=\tilde P^{\natural}$, which equals $\tilde P$ only when $\tilde P$ is fixed by ${}^{\natural}$, so $1$ is not a right identity, and there is no right identity, since a right identity $E$ would give $\tilde P^{\natural}E=\tilde P$ for all $\tilde P$, hence $E=1$ on taking $\tilde P=1$ and then $\tilde P^{\natural}=\tilde P$ for all $\tilde P$, which is false.

For the ${}^{*}$-product the two sides exchange roles. Here $\tilde P\tilde Q^{*}$ leaves the first factor untouched, so $\tilde P1^{*}=\tilde P$ and $1$ is a right identity, while $1\tilde Q^{*}=\tilde Q^{*}$ is not $\tilde Q$ in general, so $1$ is not a left identity and there is no left identity. This is the one entry of the naive table that is easy to get wrong: because $\tilde Q^{*}=\overline{Q_0}e_0-\overline{\mathbf Q}$, the unit is conjugated to itself, and the star product is unital on the right and not on the left.

For the fourth product neither $1^{\natural}\tilde Q^{*}=\tilde Q^{*}$ nor $\tilde P^{\natural}1=\tilde P^{\natural}$ returns its argument, and the same argument as above shows there is no identity on either side.

## Alternative, Flexible and Power Associative

The three remaining rows record weaker forms of associativity, and each is settled by a short computation on basis elements, recorded below.

The **left alternative** identity is $\tilde P(\tilde P\tilde Q)=(\tilde P\tilde P)\tilde Q$, and a single failure of either the left or the right law denies alternativity, so it settles the row; it fails for the ${}^{\natural}$-product at $\tilde P=e_3$, $\tilde Q=-e_3$, where the left-hand side is $e_3$ and the right-hand side is $-e_3$, for the ${}^{*}$-product at $\tilde P=-e_3$, $\tilde Q=e_3$, with the same two values, and for the fourth product at $\tilde P=e_0$, $\tilde Q=ie_0$, where the two sides are $ie_0$ and $-ie_0$. The **flexible** identity is $(\tilde P\tilde Q)\tilde P=\tilde P(\tilde Q\tilde P)$; it fails for the ${}^{\natural}$-product at $\tilde P=e_3$, $\tilde Q=e_0$, the two sides being $-e_0$ and $e_0$, for the ${}^{*}$-product at $\tilde P=-e_2$, $\tilde Q=e_0$, the two sides being $e_0$ and $-e_0$, and for the fourth product at $\tilde P=ie_0$, $\tilde Q=e_0$, with the same two values. The **degree-three** identity $\tilde P(\tilde P\tilde P)=(\tilde P\tilde P)\tilde P$ fails for all three products: for the ${}^{\natural}$-product and for the ${}^{*}$-product at $\tilde P=e_3$, where the two sides are $-e_3$ and $e_3$ in the first case and $e_3$ and $-e_3$ in the second, and for the fourth product at $\tilde P=ie_3$, where the two sides are $ie_3$ and $-ie_3$.

The complex bilinear product satisfies all three, being associative, and it is the only one of the four that does. The pattern is the one the table shows: the four products have the four displayed scalar parts and are told apart by their vector parts, and every one of these identities is an identity of elements, hence decided on the vector parts.

## The Left Multiplications

The left multiplication by $\tilde P$ is the map sending $\tilde X$ to the value of the operation on the pair $(\tilde P,\tilde X)$. For the complex bilinear product the left multiplications compose by $L_{\tilde P}\circ L_{\tilde R}=L_{\tilde P\tilde R}$, which is associativity, and they form a monoid. For the ${}^{\natural}$-product the same composition law holds in reversed order, $L^{\natural}_{\tilde P}\circ L^{\natural}_{\tilde R}=L^{\natural}_{\tilde R\tilde P}$, so the left multiplications form a monoid again, isomorphic to the opposite of the multiplicative monoid of $\mathbb{B}$; this is why the row of the table on the left multiplications reads yes, yes, no, no, the two sesquilinear products being excluded by the computation of *Relations Between the Four Biquaternion Products*, where the composition of two of their left multiplications is shown to be linear and hence not one of them.

The row is not implied by the associative row. The ${}^{\natural}$-product is not associative, and its left multiplications still form a monoid, because the composition law holds in reversed order, by the anti-automorphism property of ${}^{\natural}$; and the two sesquilinear products fail the row for the reason given above, namely that the composition of two of their left multiplications leaves the class, which has nothing to do with the associativity of the underlying product.

## Which of the Four Is a Multiplication

Only the complex bilinear product is a multiplication in the sense of algebra. It is $\mathbb{C}$-bilinear in both arguments, associative, commutative in its scalar part alone, and unital with a two-sided unit; it is the product that makes $\mathbb{B}$ an associative algebra with unit over $\mathbb{C}$, and it is the one whose associated structures — the six distinguished subspaces, the Jordan and the Lie structures of *Decomposition of the Biquaternion Complex Products*, the zero divisors and the idempotents — the rest of the category develops.

The ${}^{\natural}$-product is $\mathbb{C}$-bilinear, and that is all: it is not associative and it is unital on the left only. It defines on the underlying vector space a non-associative algebra structure in the weak sense, one that agrees with the complex bilinear product on the centre and disagrees on the vector parts; it is the product whose scalar part is the signless sum $\sum_\mu P_\mu Q_\mu$.

The two products carrying the star are not multiplications of a bilinear $\mathbb{C}$-algebra at all: being conjugate-linear in their second argument they cannot be. Both are multiplications of a sesquialgebra over the conjugation, and within the pair they are separated by the unit. The complex sesquilinear product is the derived operation $\tilde X\star\tilde Y = \tilde X\tilde Y^{*}$ of $\mathbb{B}$ with its conjugate-linear involution, that is the standard example of the category, and $e_0$ is a right unit of it; the complex quaternionic sesquilinear product reads the first factor through the $\mathbb{C}$-linear ${}^{\natural}$ as well and has no right unit, so it is a sesquilinear multiplication that is not the derived one (*Biquaternions as a Sesquialgebra over $\mathbb{C}$*). The classification of the four is therefore: one multiplication of an associative unital algebra, one bilinear product that fails associativity and two-sidedness, and two multiplications of a sesquialgebra, of which the complex one is the derived operation with the right unit and the complex quaternionic one is not the derived operation and has no right unit.

The order of the four products matches the order of the objects. The complex bilinear product is the multiplication of the associative unital algebra; the complex sesquilinear product is the derived operation, the multiplication the sesquialgebra takes; the two $\natural$-products are the same two products read with the $\mathbb{C}$-linear conjugation ${}^{\natural}$ inserted in the first slot, and the insertion of a $\mathbb{C}$-linear map changes the product without changing its sesquilinearity type.

Each of the four is read as a multiplication in an article of its own: the complex bilinear product in *Biquaternions as an Algebra over $\mathbb{C}$*, the complex quaternionic bilinear product in *Biquaternions as a Quaternionic Algebra over $\mathbb{C}$*, the complex sesquilinear product in *Biquaternions as a Sesquialgebra over $\mathbb{C}$*, and the complex quaternionic sesquilinear product in *Biquaternions as a Quaternionic Sesquialgebra over $\mathbb{C}$*; the entries of the table above are the statements those four articles prove or quote.

## The Squares, the Idempotents and the Roots

The four products are told apart on a single element by the **square**, and the idempotent and the root problems follow from it. Writing $\tilde P = P_0e_0 + \mathbf P$ and $(\mathbf P,\mathbf P) = P_1^2 + P_2^2 + P_3^2$, the scalar part of the square is

$$
\mathrm{Sc}\bigl(\tilde P\tilde P\bigr) = P_0^2 - (\mathbf P,\mathbf P), \qquad
\mathrm{Sc}\bigl(\tilde P^{\natural}\tilde P\bigr) = P_0^2 + (\mathbf P,\mathbf P) = N(\tilde P),
$$

$$
\mathrm{Sc}\bigl(\tilde P\tilde P^{*}\bigr) = \sum_\mu\lvert P_\mu\rvert^2, \qquad
\mathrm{Sc}\bigl(\tilde P^{\natural}\tilde P^{*}\bigr) = \lvert P_0\rvert^2 - \sum_k\lvert P_k\rvert^2 .
$$

These are the four diagonals of *Four Forms but One Topology on the Biquaternion Algebra*, and the same four expressions are the scalar parts of the four products of *Relations Between the Four Biquaternion Products*. Two of them decide the two problems on the spot. The $\natural$-square lies in the centre for every element, being $N(\tilde P)e_0$, so its roots of a central value are the single equation $N(\tilde P) = \lambda$. The complex sesquilinear square has the **non-negative** scalar part $\sum_\mu\lvert P_\mu\rvert^2$, so that product has no root of a negative value at all. The remaining two squares are elements, and their scalar parts are the indefinite complex bilinear and Krein values.

| problem | $\tilde P\tilde P = \tilde P$ | $\tilde P^{\natural}\tilde P = \tilde P$ | $\tilde P\tilde P^{*} = \tilde P$ | $\tilde P^{\natural}\tilde P^{*} = \tilde P$ |
|---|---|---|---|---|
| idempotents | $0$, $e_0$, and $\tfrac12(e_0 + \xi i)$ for a root $\xi$ of $-e_0$ | $0$ and $e_0$ alone | $0$, $e_0$, and the Hermitian idempotents $\tfrac12(e_0 + i\hat\mu)$ with $\hat\mu$ a real unit vector | $0$, $e_0$, and $-\tfrac12 e_0 + \mu$ for a real $\mu$ of the vector subspace with $(\mu,\mu) = \tfrac34$ |

The four columns are four different sets. The first is infinite and is the one the rest of the category uses; the second is the smallest possible, the two trivial idempotents; the third is the family of the pure states of *Biquaternion Idempotents and Projections*; the fourth is a family of a different kind, lying in the real vector subspace.

The square roots of a central value differ in the same way and by the same two structural facts.

| square roots | $\tilde P\tilde P = \lambda e_0$ | $\tilde P^{\natural}\tilde P = \lambda e_0$ | $\tilde P\tilde P^{*} = \lambda e_0$ | $\tilde P^{\natural}\tilde P^{*} = \lambda e_0$ |
|---|---|---|---|---|
| of $-e_0$ | $P_0 = 0$ with $(\mathbf P,\mathbf P) = 1$, and $P_0 = \pm i$ | the solutions of $N(\tilde P) = -1$ | none | the solutions of $\tilde P^{\natural}\tilde P^{*} = -e_0$, among them every real pure $\mathbf P$ with $(\mathbf P,\mathbf P) = 1$ |
| of $0$ | $P_0 = 0$ with $(\mathbf P,\mathbf P) = 0$, the nilpotents | the solutions of $N(\tilde P) = 0$, the zero divisors together with $0$ | $\tilde P = 0$ alone | the solutions of $\tilde P^{\natural}\tilde P^{*} = 0$, among them $e_0 + ie_1$ |

The three families of *Biquaternion Square Roots of Minus One, Zero and Plus One* are therefore the three parts of one column of this table, the column of the complex bilinear product, and not a classification of the square of the algebra in general. The other three columns are the same three equations read in the other products, and each of the other three has its reading in the article of that product.

## Summary

The four products of *The Four Biquaternion Complex Products* are compared in the table above. Each is $\mathbb{C}$-linear in the first argument; the complex bilinear product and the ${}^{\natural}$-product are $\mathbb{C}$-linear in the second, the two products carrying the star are conjugate-linear there. The complex bilinear product is associative, has the two-sided unit $1$, is alternative, flexible and satisfies the degree-three identity, and its left multiplications form a monoid; the ${}^{\natural}$-product is $\mathbb{C}$-bilinear and has the left unit $1$ alone, and it fails associativity, the alternative identities, flexibility and the degree-three identity, as do the two sesquilinear products, which have no identity at all and whose left multiplications do not even form a monoid. Counterexamples are given in each case on the basis elements $e_0$, $e_1$, $e_2$, $e_3$ and on $ie_0$ and $ie_3$.

Both products without the star are multiplications of a bilinear $\mathbb{C}$-algebra, and exactly one of them is a multiplication of an associative unital one, the complex bilinear product: the ${}^{\natural}$-product is $\mathbb{C}$-bilinear but neither associative nor two-sidedly unital. Both products carrying the star are multiplications of a sesquialgebra over $\mathbb{C}$ with the conjugation. Among the two, the complex sesquilinear product is the derived operation of $\mathbb{B}$ with its conjugate-linear involution and has $e_0$ as a right unit, and the complex quaternionic sesquilinear product is neither. The identities that link the four are *Relations Between the Four Biquaternion Products*, and the split of the complex bilinear product into a symmetric and an antisymmetric half, with the Jordan and the Lie structure the halves carry, is *Decomposition of the Biquaternion Complex Products*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q^{*}$ | the four products, defined in *The Four Biquaternion Complex Products* |
| $1=e_0$ | the unit of the algebra, fixed by ${}^{\natural}$ and by ${}^{*}$ |
| $e_1$, $e_2$, $e_3$ | the quaternion units, with $e_1^2=e_2^2=e_3^2=-e_0$ |
| $L_{\tilde P}$, $L^{\natural}_{\tilde P}$, $L^{*}_{\tilde P}$, $L^{\natural*}_{\tilde P}$ | the left multiplications of the four products |
| $\mathbf P$ | the vector part of $\tilde P=P_0+\mathbf P$ |

## Further Reading

- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the four definitions and their scalar–vector forms.
- *Relations Between the Four Biquaternion Products* (`articles_maths/relations-between-the-four-biquaternion-products.md`), for the identities that link the four and for the left multiplications.
- *Decomposition of the Biquaternion Complex Products* (`articles_maths/decomposition-of-the-biquaternion-complex-products.md`), for the symmetric and the antisymmetric part of each of the four products, and the Jordan and the Lie structure the two parts of the complex bilinear product carry.
- *The Six Subspaces and the Four Complex Products* (`articles_maths/the-six-subspaces-and-the-four-complex-products.md`), for the four products on the six distinguished subspaces, and for the Jordan and the Lie algebra each of the six carries and with which product.
- *Biquaternions as a Sesquialgebra over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-sesquialgebra-over-c.md`), for the sesquilinear reading of the complex sesquilinear product and the algebra it defines.
- *Sesquialgebras* (`articles_maths/sesquialgebras.md`), for the two scalar rules, the collapse theorem and the standard example that the sesquilinear row of the table tests.
