
# __The Quaternionic Product on the Quaternion Subspace__

## Introduction

The product of this group is the **complex quaternionic bilinear product**

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q , \qquad \tilde P^{\natural} = P_0 - \mathbf P ,
$$

the second of the four products of the biquaternion algebra $\mathbb{B}$ (*The Four Biquaternion Complex Products* §*The Complex Quaternionic Bilinear Product*), whose algebra is *Biquaternions as a General Quaternionic Algebra (GQA) over $\mathbb{C}$*. The previous five articles read the product over the whole algebra; this one reads it on the four-dimensional real subspace on which the whole batch becomes classical,

$$
\mathbb{H}_{\mathbb{B}} = \mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3 ,
$$

the **quaternion subspace** (*Introduction to the Six Subspaces* §*The Quaternion Subspace*). Its elements are the real quaternions: the four coefficients are real, and the subspace is the fixed space of complex conjugation, $\bar{\tilde P} = \tilde P$ if and only if $\tilde P \in \mathbb{H}_{\mathbb{B}}$. On it the natural conjugation acts as the quaternion conjugate, $h^{\natural} = \bar h$, which fixes the real line alone; the fixed set of ${}^{\natural}$ on the whole algebra is the centre, not the subspace.

The article establishes four things. First, the subspace is closed under the product, and the restriction is the familiar operation of putting the first factor into its quaternion conjugate,

$$
h\star g = \bar h\,g ,
$$

which is the isotope of the quaternion algebra by its conjugation. Second, the restricted product is **not associative**, the triple $(i,i,j)$ of units witnessing it, so it is neither the quaternion algebra nor the opposite quaternion algebra: it is the isotope. Third, its left multiplications are the plain left multiplications by the conjugates and form a monoid isomorphic to the **opposite** of the quaternion algebra, which is the precise sense in which the opposite algebra appears on this subspace. Fourth, the whole batch restricts classically on the subspace: the square is the reduced norm $|h|^2e_0$, the reduced norm of a real quaternion is a sum of four real squares and vanishes only at the origin, so the cone of the second article meets the subspace at the origin alone and every nonzero element is a unit, and the symmetrisation is the Euclidean inner product placed on the real line.

## The Restriction of the Product

**Theorem (the subspace is closed).** For $h,g \in \mathbb{H}_{\mathbb{B}}$ the product $h\star g$ lies in $\mathbb{H}_{\mathbb{B}}$, and on real quaternions

$$
h\star g = h^{\natural}g = \bar h\,g ,
$$

where $\bar h$ is the quaternion conjugate of $h$.

**Proof.** For a real quaternion $h = h_0+h_1e_1+h_2e_2+h_3e_3$ the natural conjugation is $h^{\natural} = h_0-h_1e_1-h_2e_2-h_3e_3$, the quaternion conjugate; the conjugation is an anti-automorphism of the plain product, so $\bar h g$ is again a real quaternion, and the coefficients of $\bar h g$ are sums of products of real numbers and of the structure constants of the quaternion algebra, hence real. $\square$

**Corollary (the subspace is a real algebra with a left unit only).** $\mathbb{H}_{\mathbb{B}}$ is a four-dimensional real algebra under $\star$, with $e_0$ as a left unit, $e_0\star g = g$, and no right unit, $h\star e_0 = \bar h$, which differs from $h$ as soon as the vector part of $h$ is nonzero. In particular the subspace is closed under $\star$ but is not the quaternion algebra: the element $h = i$ gives $i\star e_0 = -i$ whereas $i e_0 = i$.

**Remark (the source of the restriction).** All four products of the chapter restrict to the quaternion subspace (*The Six Subspaces and the Four Complex Products*): on real quaternions they read $hg$, $\bar hg$, $h\bar g$ and $\bar h\bar g = \overline{gh}$. The three non-associative ones are the three isotopes of the quaternion algebra by the three nontrivial maps among the identity and the two conjugations, and only the first is associative. The product of this group is the one with the conjugation in the first slot, and its restriction $\bar hg$ is the isotope by the quaternion conjugation. The isotope reading was introduced for the whole algebra in *Biquaternions as a General Quaternionic Algebra (GQA) over $\mathbb{C}$* and used in the first three articles of this group; here it is the only reading, the twisting map being an involution of the algebra.

## The Two Smaller Real Subspaces

Inside $\mathbb{H}_{\mathbb{B}}$ sit two smaller real subspaces, the real vector subspace $\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ and the real line $\mathbb{R}e_0$, and the product restricts to each in a way worth recording, because the restriction along the chain $\mathbb{R}e_0\subset\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3\subset\mathbb{H}_{\mathbb{B}}$ is what the vector part of the whole algebra sees.

**The real vector subspace.** For real pure quaternions $\mathbf u,\mathbf v$, the natural conjugation is the negation, $\mathbf u^{\natural} = -\mathbf u$, so

$$
\mathbf u\star\mathbf v = \mathbf u^{\natural}\mathbf v = -\mathbf u\mathbf v = -(\mathbf u,\mathbf v)e_0+\mathbf u\times\mathbf v .
$$

With the plain product written $\mathbf u\mathbf v = -(\mathbf u,\mathbf v)+\mathbf u\times\mathbf v$, this is the **negative of the plain product** of the two pure quaternions, and the two terms change sign together:

$$
\mathbf u\star\mathbf v = (\mathbf u,\mathbf v)e_0-\mathbf u\times\mathbf v .
$$

The value is the Euclidean dot product of the pair placed on the real line, minus the cross product; it is a real quaternion, so it stays inside $\mathbb{H}_{\mathbb{B}}$, but it does not stay inside the real vector subspace, because its scalar part $(\mathbf u,\mathbf v)$ is nonzero as soon as the two vectors are not orthogonal. The restriction is thus a map into the whole quaternion subspace, and the part of the value that returns to the real vector subspace is the pure part alone.

**The real line.** On $\mathbb{R}e_0$ the product is

$$
(ae_0)\star(be_0) = ab\,e_0 ,
$$

the ordinary product of the real coordinates, and the real line is a two-sided subalgebra of the restricted algebra, with $e_0$ as its unit.

**Remark (the sign contrast).** The middle restriction is the one that explains the sign contrasts of the batch: the plain product of two pure vectors is $-(\mathbf u,\mathbf v)+\mathbf u\times\mathbf v$, and reading the first slot through ${}^{\natural}$ multiplies by $-1$, so the restricted product is $+(\mathbf u,\mathbf v)e_0-\mathbf u\times\mathbf v$, with both terms negated. On the real line the sign is invisible, the two products agreeing there; on the real vector subspace it is visible in both terms.

## The Failure of Associativity on the Subspace

**Theorem (the restriction is not associative).** The product on $\mathbb{H}_{\mathbb{B}}$ is not associative; the triple $(h,g,k) = (i,i,j)$ of units witnesses it. With $i\star i = \bar\imath\,i = e_0$ and $i\star j = \bar\imath\, j = -ij = -k$,

$$
(i\star i)\star j = e_0\star j = j , \qquad i\star(i\star j) = i\star(-k) = \bar\imath(-k) = ik = -j ,
$$

so the two bracketings are $j$ and $-j$.

**Proof.** The computations use the multiplication table $ij = k$ and $ik = -j$ of the quaternion units and the left unit $e_0\star j = j$. $\square$

**Corollary (what the subspace is not).** The restricted product is neither the quaternion algebra nor its opposite: both are associative, and the restricted product is not. The witness $h = i$, $g = e_0$ separates it from the quaternion algebra, $i\star e_0 = -i$ against $i e_0 = i$, and the same pair separates it from the opposite algebra, whose product is $e_0 i = i$ against $-i$.

**Remark.** The failure of associativity is not visible on the triple $(i,j,k)$ of distinct units: there both bracketings give $-e_0$, since $(i\star j)\star k = (\bar\imath j)\star k = (-k)\star k = k^2 = -e_0$ and $i\star(j\star k) = i\star(\bar\jmath k) = i\star(-i) = i^2 = -e_0$, and the two agree. It is visible as soon as the first factor is repeated, and the triple $(i,i,j)$ above is the witness. The subspace thus carries a non-associative product in the same way the whole algebra does, and the associativity of the quaternion algebra is lost on restriction.

## The Norm, the Units and the Cone

**Theorem (the square is the reduced norm).** For $h \in \mathbb{H}_{\mathbb{B}}$,

$$
h\star h = \bar h h = N(h)e_0 = |h|^2e_0 ,
$$

the reduced norm of the real quaternion $h$, a non-negative real number that vanishes only at $h = 0$.

**Proof.** The square lemma of *Idempotents of the Quaternionic Product* gives $h\star h = N(h)e_0$, and on real quaternions $N(h) = \bar h h$ is the sum of the four real squares $h_0^2+h_1^2+h_2^2+h_3^2$, which is real, non-negative and zero only at the origin. $\square$

**Corollary (the element theory of the subspace is classical).** On $\mathbb{H}_{\mathbb{B}}$: the only idempotents are $0$ and $e_0$; the only square-zero element is $0$; every nonzero element is a unit, the inverse of $h$ being $\bar h/|h|^2$. In particular the nilpotent cone of the second article meets the subspace at the origin alone, and the zero-divisor theory of the algebra has no content on the real quaternions.

**Proof.** An idempotent satisfies $|h|^2e_0 = h$, so $h$ lies in the real line and $h_0^2 = h_0$, giving $0$ and $1$; a square-zero element has $|h|^2 = 0$, giving $h = 0$; the inverse formula is checked directly, $\bar h h = h\bar h = |h|^2\neq0$. $\square$

**Remark.** This is the classical contrast of the batch. On the real quaternion subspace the product is a non-associative operation with a left unit only, and its element theory is as good as it can be: no nontrivial idempotent, no nilpotent, and every element invertible. On the whole algebra the same product has a nonzero cone of zero divisors, of real dimension six. The two statements are the same statement read on different subspaces: the norm form is positive definite on $\mathbb{H}_{\mathbb{B}}$ and indefinite on $\mathbb{B}$, and the cone $\{N = 0\}$ is the origin on the former and a six-dimensional cone on the latter.

## The Left Multiplications on the Subspace

**Theorem (the restricted left multiplications).** For $h \in \mathbb{H}_{\mathbb{B}}$ the left multiplication $L_h$ of the product preserves $\mathbb{H}_{\mathbb{B}}$, and it is the plain left multiplication by the conjugate,

$$
L_h = L^{\mathrm{plain}}_{\bar h} , \qquad L_h(g) = \bar h g .
$$

**Theorem (the monoid of the subspace is the opposite quaternion algebra).** For $h,g \in \mathbb{H}_{\mathbb{B}}$,

$$
L_h\circ L_g = L_{gh} ,
$$

and the monoid $\{L_h : h \in \mathbb{H}_{\mathbb{B}}\}$ is isomorphic to the **opposite** of the quaternion algebra, $\mathbb{H}^{\mathrm{op}}$.

**Proof.** $L_h(L_g(k)) = \bar h(\bar g k) = (\bar h\bar g)k = \overline{gh}\,k = L_{gh}(k)$ by the associativity of the quaternion product and the anti-automorphism property $\bar h\bar g = \overline{gh}$. The monoid is therefore the quaternion algebra with its product reversed, and $\mathbb{H}^{\mathrm{op}}\cong\mathbb{H}$ as an abstract algebra because the conjugation is an isomorphism onto the opposite. $\square$

**Remark (the precise sense in which the opposite algebra appears).** The restricted product **is not** the opposite quaternion algebra — the opposite of the quaternion algebra is associative, and the restricted product is not. What coincides with the opposite quaternion algebra is its family of left multiplications: the monoid they form is $\mathbb{H}^{\mathrm{op}}$, by the theorem just proved and by the general theorem of the previous article, $M_L\cong\mathbb{B}^{\mathrm{op}}$, restricted to the real quaternions. Equivalently, the restricted product $\bar hg$ is the isotope of the quaternion algebra by the conjugation; the conjugation is an isomorphism of the quaternion algebra onto its opposite, since $\bar h\bar g = \overline{gh}$, so the isotope sits in the isotopy class of the opposite algebra. Isotopy and not isomorphism is the exact relation: an isomorphism with the opposite quaternion algebra would carry its associativity back to the restricted product, and the restricted product is not associative (*A Taste of Jordan Algebras* §*Isotopes and Homotopes*).

## The Algebra It Is Not

The restricted product is a four-dimensional real algebra. Three other four-dimensional real algebra structures live on the same space, and the article closes by separating them.

**Not the quaternion algebra, and not its opposite.** Both are associative, and the restricted product is not; the witnesses are in the section above.

**Not the symmetric bilinear form.** The symmetrisation of the restricted product is

$$
h\circ g = \tfrac12\bigl(\bar h g + \bar g h\bigr) = \langle h,g\rangle\,e_0 ,
$$

the Euclidean inner product placed on the real line, a commutative operation with no vector part. It is not a Jordan algebra: at $h = g = e_1$ its two sides in the Jordan identity are $e_0$ and $0$, which is the failure computed for the whole algebra in *The Symmetrised Quaternionic Product and the Hermitian Subspace* and recorded for the subspace in *The Six Subspaces and the Four Complex Products*.

**Not a Lie algebra.** The antisymmetrisation $[h,g]_{\star} = \bar hg-\bar gh$ stays inside the subspace, but it fails the Jacobi identity; at the triple $(e_0,e_1,e_2)$ the cyclic sum of the three brackets is a nonzero multiple of $e_3$ (*The Six Subspaces and the Four Complex Products*, and *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* for the whole algebra).

**What it is.** The restricted product is the isotope of the quaternion division algebra by its conjugation: closed, with a left unit and no right one, non-associative, with the classical positive element theory of the division algebra, and with the opposite quaternion algebra as the monoid of its left multiplications. It is the classical picture of the batch, and the article that follows reads the same product in the matrix model.

## Summary

The quaternion subspace $\mathbb{H}_{\mathbb{B}}$, of real dimension four, is the fixed space of complex conjugation, and it is closed under the quaternionic product: on real quaternions the product reads $h\star g = \bar hg$, the isotope of the quaternion algebra by its conjugation. The restriction is not associative, the triple $(i,i,j)$ of units being a witness, so it is neither the quaternion algebra nor the opposite quaternion algebra; the opposite appears instead as the monoid of left multiplications, $L_h\circ L_g = L_{gh}$, and as the isotopy class of the isotope. The square of a real quaternion is its reduced norm $|h|^2e_0$, a sum of four real squares, so the only idempotents are $0$ and $e_0$, the only square-zero element is $0$, every nonzero element is a unit, and the nilpotent cone of the whole algebra meets the subspace at the origin alone. The symmetrisation restricts to the Euclidean inner product on the real line and fails the Jordan identity; the antisymmetrisation stays inside the subspace and fails Jacobi. The subspace is thus the classical picture of the batch: the same product, with the element theory of a division algebra, on the four-dimensional real form on which the norm is positive definite.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2 = -e_0$ |
| $\mathbb{H}_{\mathbb{B}}$ | the quaternion subspace $\mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ |
| $h = h_0+h_1e_1+h_2e_2+h_3e_3$ | a real quaternion, all four coefficients real |
| $\bar h = h_0-h_1e_1-h_2e_2-h_3e_3$ | the quaternion conjugate, the restriction of ${}^{\natural}$ |
| ${}^{\natural}$ | the natural conjugation $\tilde P^{\natural} = P_0-\mathbf P$ |
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q$ | the complex quaternionic bilinear product, the multiplication of this group |
| $\tilde P\tilde Q$ | the plain (associative) product of the algebra |
| $N(h) = \bar hh = |h|^2$ | the reduced norm of a real quaternion |
| $L_h$ | the left multiplication of the product, $L_h(g) = \bar hg$ |
| $\mathbb{H}^{\mathrm{op}}$ | the opposite quaternion algebra, the monoid of the left multiplications |
| $\langle h,g\rangle$ | the Euclidean inner product of the four real coordinates |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for isotopes and homotopes, the equivalence that survives a change of product, and the isotope by an anti-automorphism.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the restriction of a product to a subalgebra and the failure of associativity on a subalgebra of an associative algebra.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the quaternion division algebra, the reduced norm and the positivity of its norm form.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion conjugation, the inner product and the multiplication table of the units.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the conjugation as an anti-automorphism of order two and the opposite algebra it defines.
