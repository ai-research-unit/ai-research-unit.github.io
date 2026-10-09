
# __The Left Multiplications of the Quaternionic Product and the Opposite Monoid__

## Introduction

The product of this group is the **general quaternionic bilinear product**

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q , \qquad \tilde P^{\natural} = P_0 - \mathbf P ,
$$

the second of the four general products of the biquaternion algebra $\mathbb{B}$ (*The Four General Products of the Biquaternion $\mathbb{C}$ Space* §*The General Quaternionic Bilinear Product*), whose algebra is *Introduction to the General Quaternionic Algebra of Biquaternions*. The four articles before this one are negative in their outcome: the product has no nontrivial idempotent, its square-zero set is the whole zero-divisor cone, it is associative at no rung of the ladder, and its symmetrisation is no Jordan algebra. This article is the batch's one positive structure theorem, and it is about the **operators** that the product defines rather than about the elements of the algebra.

For an element $\tilde P$ the **left multiplication** is the map on $\mathbb{B}$ obtained by fixing $\tilde P$ in the first slot,

$$
L_{\tilde P}(\tilde X) = \tilde P\star\tilde X = \tilde P^{\natural}\tilde X ,
$$

a linear endomorphism of $\mathbb{B}$. For an arbitrary non-associative product the composite of two left multiplications has no reason to be a left multiplication. Here it always is.

The article establishes four things. First, the left multiplications compose by the **reversed** law

$$
L_{\tilde P}\circ L_{\tilde R} = L_{\tilde R\tilde P} ,
$$

the product on the right being the *plain* product of the algebra, so that the set of left multiplications is a monoid isomorphic to the **opposite** of the multiplicative monoid of $\mathbb{B}$ — although $\star$ is not associative. Second, the right multiplications of the product do not close under composition, and the closed family on the right is the twisted one $\tilde X\mapsto\tilde X\tilde P^{\natural}$, whose law is the **direct** one, $\varrho_{\tilde P}\circ \varrho_{\tilde R} = \varrho_{\tilde P\tilde R}$. Third, the mixed composites $L_{\tilde P}\circ \varrho_{\tilde Q}$ commute and span the full endomorphism algebra, the multiplication algebra of $\mathbb{B}$, of dimension sixteen. Fourth, this is exactly the row of the property table of *Comparison Between the Four General Products* on the left multiplications, which reads yes for the two bilinear products and no for the two sesquilinear ones.

## The Left Multiplications

**Theorem (the composition law).** For all $\tilde P,\tilde R \in \mathbb{B}$,

$$
L_{\tilde P}\circ L_{\tilde R} = L_{\tilde R\tilde P} ,
$$

where $\tilde R\tilde P$ is the plain product of the algebra.

**Proof.** For every $\tilde X$,

$$
L_{\tilde P}\bigl(L_{\tilde R}(\tilde X)\bigr) = \tilde P^{\natural}\bigl(\tilde R^{\natural}\tilde X\bigr) = \bigl(\tilde P^{\natural}\tilde R^{\natural}\bigr)\tilde X = \bigl(\tilde R\tilde P\bigr)^{\natural}\tilde X = L_{\tilde R\tilde P}(\tilde X) ,
$$

using the associativity of the plain product in the middle step and the fact that ${}^{\natural}$ is an anti-automorphism of order two, $\tilde P^{\natural}\tilde R^{\natural} = (\tilde R\tilde P)^{\natural}$, in the third. $\square$

**Remark (why associativity of $\star$ is not needed).** The proof uses the associativity of the **plain** product twice, and never the associativity of $\star$; and it is precisely because ${}^{\natural}$ reverses the order of a plain product that the law comes out reversed. This is the sense in which the left multiplications of $\star$ form a monoid for the same reason and with the same order reversal as the left multiplications of the algebra under the conjugation: the map $\tilde P\mapsto L_{\tilde P}$ intertwines $\star$ with the opposite of the plain product.

**Theorem (the monoid of left multiplications).** The set $M_L = \{L_{\tilde P} : \tilde P \in \mathbb{B}\}$ is closed under composition and contains the identity $L_{e_0} = \mathrm{id}_{\mathbb{B}}$. The map $\tilde P\mapsto L_{\tilde P}$ is an injective anti-homomorphism of monoids from the multiplicative monoid of $\mathbb{B}$ onto $M_L$, so

$$
M_L \cong \mathbb{B}^{\mathrm{op}} ,
$$

the opposite of the multiplicative monoid of $\mathbb{B}$.

**Proof.** Closure and the identity are read off the law: $L_{\tilde P}L_{\tilde R} = L_{\tilde R\tilde P}$ is again a left multiplication, and $L_{e_0}(\tilde X) = e_0^{\natural}\tilde X = \tilde X$. The law $L_{\tilde P}L_{\tilde R} = L_{\tilde R\tilde P}$ is exactly the statement that the assignment reverses the order of a product, so it is an anti-homomorphism; it is surjective onto $M_L$ by definition and injective because $L_{\tilde P} = L_{\tilde R}$ forces $\tilde P^{\natural} = L_{\tilde P}(e_0) = L_{\tilde R}(e_0) = \tilde R^{\natural}$ and hence $\tilde P = \tilde R$. $\square$

**Corollary (the units).** The left multiplication $L_{\tilde P}$ is invertible in $M_L$ exactly when $\tilde P$ is a unit of the algebra, that is exactly when $N(\tilde P) \neq 0$; the group of units of $M_L$ is therefore isomorphic to the group $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ with reversed product.

**Proof.** The operator $L_{\tilde P}$ is the plain left multiplication by the element $\tilde P^{\natural}$, so it is invertible exactly when $\tilde P^{\natural}$ is a unit of the plain algebra, and the plain algebra is isomorphic to the matrix algebra $M_2(\mathbb{C})$, in which an element is a unit exactly when it is invertible as a matrix. The norm criterion says that $\tilde P^{\natural}$ is invertible exactly when $N(\tilde P^{\natural}) = N(\tilde P) \neq 0$ (*Biquaternion Norm and Invertibility*); since the anti-isomorphism $L$ carries the product to the reversed product and bijects $\mathbb{B}$ onto $M_L$, it carries the unit group to the unit group with the reversed law. $\square$

**Remark.** The anti-isomorphism is the boundary of what survives of associativity. For the associative product the assignment $\tilde P\mapsto L_{\tilde P}$ is a homomorphism of the whole algebra $\mathbb{B}$ into $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, and $\mathbb{B}$ acts on itself as an algebra of operators, with the left regular representation; for the quaternionic product only the multiplicative structure survives, and it survives reversed. The assignment is still additive and $\mathbb{C}$-linear, $L_{\tilde P+\tilde Q}=L_{\tilde P}+L_{\tilde Q}$ and $L_{\lambda\tilde P}=\lambda L_{\tilde P}$, and its failure is exactly the failure to respect $\star$: $L_{\tilde P\star\tilde R} = L_{\tilde P^{\natural}\tilde R}$ differs from $L_{\tilde P}L_{\tilde R} = L_{\tilde R\tilde P}$ in the placement of the conjugation between the two factors. What the product loses is therefore the representation of the algebra, not the monoid of its operators.

## The Right Multiplications

**Theorem (the right multiplications of the product do not close).** Let $R_{\tilde P}(\tilde X) = \tilde X\star\tilde P = \tilde X^{\natural}\tilde P$ be the right multiplication of $\star$ by $\tilde P$. Then the composite of two of them is

$$
R_{\tilde P}\circ R_{\tilde Q}(\tilde X) = \bigl(\tilde X^{\natural}\tilde Q\bigr)^{\natural}\tilde P = \tilde Q^{\natural}\,\tilde X\,\tilde P ,
$$

which is the plain product of $\tilde Q^{\natural}$, $\tilde X$ and $\tilde P$ in that order; and it is not a right multiplication of $\star$ unless it happens to coincide with one. At $\tilde P = \tilde Q = e_1$ the composite sends $e_0$ to $e_0$ and $e_1$ to $e_1$, whereas a right multiplication $\tilde X\mapsto\tilde X^{\natural}\tilde A$ with the same value at $e_0$ has $\tilde A = e_0$ and sends $e_1$ to $-e_1$.

**Proof.** The first display is the computation $(\tilde X^{\natural}\tilde Q)^{\natural} = \tilde Q^{\natural}\tilde X$ followed by the plain product with $\tilde P$; the witness is the evaluation $R_{e_1}R_{e_1}(e_0) = e_0$ and $R_{e_1}R_{e_1}(e_1) = e_1$. $\square$

The family that does close on the right is the one with the conjugation on the side of the multiplier, the mirror of the left multiplications.

**Theorem (the twisted right multiplications).** Define $\varrho_{\tilde P}(\tilde X) = \tilde X\,\tilde P^{\natural}$, the plain right multiplication by $\tilde P^{\natural}$. Then

$$
\varrho_{\tilde P}\circ \varrho_{\tilde R} = \varrho_{\tilde P\tilde R} ,
$$

the **direct** law, and $M_R = \{\varrho_{\tilde P}\}$ is a monoid containing $\varrho_{e_0} = \mathrm{id}_{\mathbb{B}}$ and isomorphic to the multiplicative monoid $\mathbb{B}$ itself.

**Proof.** $\varrho_{\tilde P}(\varrho_{\tilde R}(\tilde X)) = \tilde X\tilde R^{\natural}\tilde P^{\natural} = \tilde X(\tilde P\tilde R)^{\natural} = \varrho_{\tilde P\tilde R}(\tilde X)$, by the associativity of the plain product and the anti-automorphism property; the identity is $\varrho_{e_0}(\tilde X) = \tilde X e_0^{\natural} = \tilde X$, and injectivity is read at $e_0$ as before. $\square$

**Remark (why the two laws are opposite).** The asymmetry is the asymmetry of the product itself: in $\tilde P\star\tilde X = \tilde P^{\natural}\tilde X$ the conjugation sits on the **first** slot, so the left multiplication is the plain left multiplication by $\tilde P^{\natural}$ and the right multiplication of the product is not the plain right multiplication by anything. Writing both operators with the conjugation attached to the multiplier restores the mirror symmetry: the left family is $M_L = \{L^{\mathrm{plain}}_{\tilde P^{\natural}}\}$ and the right family is $M_R = \{R^{\mathrm{plain}}_{\tilde P^{\natural}}\}$, with $M_L\cong\mathbb{B}^{\mathrm{op}}$ and $M_R\cong\mathbb{B}$. The pair of laws $L_{\tilde P}L_{\tilde R} = L_{\tilde R\tilde P}$ and $\varrho_{\tilde P}\varrho_{\tilde R} = \varrho_{\tilde P\tilde R}$ is the exact form in which the two-sidedness of the plain product survives the twisting of a single slot.

## The Mixed Compositions

**Theorem (the mixed composites commute).** For all $\tilde P,\tilde Q \in \mathbb{B}$,

$$
L_{\tilde P}\circ \varrho_{\tilde Q} = \varrho_{\tilde Q}\circ L_{\tilde P} , \qquad L_{\tilde P}\circ \varrho_{\tilde Q}(\tilde X) = \tilde P^{\natural}\tilde X\tilde Q^{\natural} .
$$

**Proof.** Both sides send $\tilde X$ to $\tilde P^{\natural}\tilde X\tilde Q^{\natural}$ by the associativity of the plain product. $\square$

**Theorem (the multiplication algebra).** The complex span of the operators $\{L_{\tilde P}\circ \varrho_{\tilde Q} : \tilde P,\tilde Q \in \mathbb{B}\}$ is closed under composition and is all of the endomorphism algebra $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen.

**Proof.** Closure: $\bigl(L_{\tilde P}\varrho_{\tilde Q}\bigr)\bigl(L_{\tilde A}\varrho_{\tilde B}\bigr) = L_{\tilde P}L_{\tilde A}\varrho_{\tilde Q}\varrho_{\tilde B} = L_{\tilde A\tilde P}\varrho_{\tilde Q\tilde B}$, by the two composition laws and the commutation of the mixed pair. For the dimension, $\mathbb{B}$ is isomorphic to the matrix algebra $M_2(\mathbb{C})$, and the operators of the form $\tilde X\mapsto \tilde P\tilde X\tilde Q$ on $M_2(\mathbb{C})$ span the whole $\mathrm{End}_{\mathbb{C}}(M_2(\mathbb{C}))$, of dimension $4^2 = 16$, because the elementary matrices realise every prescribed action on a matrix unit. The twist ${}^{\natural}$ is a bijection of $\mathbb{B}$, so the family $\{L_{\tilde P}\varrho_{\tilde Q}\}$ has the same span. $\square$

**Remark.** The closure computation is the pleasant surprise of the section: the two composition laws have opposite orders, and the opposite orders cancel in the mixed composite, $L_{\tilde P}L_{\tilde A}\varrho_{\tilde Q}\varrho_{\tilde B} = L_{\tilde A\tilde P}\varrho_{\tilde Q\tilde B}$, which is again of the required form. The algebra generated is therefore not merely a monoid but a full matrix algebra, and it carries no trace of the failure of associativity of $\star$; the failure is visible on the element level, not on the level of the operators.

**Remark (which pair commutes).** What commutes is $L_{\tilde P}$ with the **twisted** right multiplication $\varrho_{\tilde Q}$, not with the right multiplication of the product: $L_{\tilde P}$ and $R_{\tilde P}$ do not commute, and at $\tilde P = e_3$ the two composites send $e_0$ to $e_0$ and to $-e_0$, since $L_{e_3}R_{e_3}(e_0) = e_0$ and $R_{e_3}L_{e_3}(e_0) = -e_0$. This is the failure of flexibility of the third article read at the level of the operators, and it is why the multiplication algebra is built from $L$ and $\varrho$ and not from $L$ and $R$.

## The Reading of the Monoid Row

The property table of *Comparison Between the Four General Products* carries the four general products against the property "the left multiplications form a monoid" (*Comparison Between the Four General Products* §*The Property Table*), and the row reads

| product | left multiplications form a monoid |
|---|---|
| $\tilde P\tilde Q$ | yes |
| $\tilde P^{\natural}\tilde Q$ | yes |
| $\tilde P\tilde Q^{*}$ | no |
| $\tilde P^{\natural}\tilde Q^{*}$ | no |

The two bilinear columns are the two this article has just settled: for the associative product the law is the direct one, $L_{\tilde P}L_{\tilde R} = L_{\tilde P\tilde R}$, and for the quaternionic product it is the reversed one, $L_{\tilde P}L_{\tilde R} = L_{\tilde R\tilde P}$, so both families are monoids. The two sesquilinear products fail the row because the composition of two of their left multiplications is linear and not sesquilinear, and therefore not one of them (*Relations Between the Four General Products* §*The Left Multiplications*); the reason has nothing to do with the associativity of the underlying product, and the comparison article records that the row is not implied by the associative row.

**Remark.** The row is the place where the quaternionic product is at its closest to the associative one. Neither is the algebra of the other, and both the element-theoretic data and the Jordan structure were changed by the twisting of the first slot; but the left multiplications, which read the product as an action of the algebra on itself, survive, and they survive as the opposite monoid. The next two articles carry the product down to the quaternion subspace, where the whole batch becomes classical, and into the matrix model, where it is read off the trace and the determinant.

## Summary

The left multiplications of the quaternionic product are $L_{\tilde P}(\tilde X) = \tilde P^{\natural}\tilde X$, and they compose by the reversed law $L_{\tilde P}\circ L_{\tilde R} = L_{\tilde R\tilde P}$, the product on the right being the plain product of the algebra; the set $M_L$ is a monoid with identity $L_{e_0}$, and $\tilde P\mapsto L_{\tilde P}$ is an isomorphism $M_L\cong\mathbb{B}^{\mathrm{op}}$ onto the opposite of the multiplicative monoid, although $\star$ is not associative. The right multiplications of $\star$ do not close, their composite being $\tilde Q^{\natural}\tilde X\tilde P$; the closed family is the twisted one $\varrho_{\tilde P}(\tilde X) = \tilde X\tilde P^{\natural}$, with the direct law $\varrho_{\tilde P}\varrho_{\tilde R} = \varrho_{\tilde P\tilde R}$ and $M_R\cong\mathbb{B}$. The mixed composites commute, $L_{\tilde P}\varrho_{\tilde Q} = \varrho_{\tilde Q}L_{\tilde P}$, are closed under composition, and span the whole endomorphism algebra, of dimension sixteen. This is the row of the property table on the left multiplications, where the two bilinear products read yes and the two sesquilinear ones read no; it is the batch's one positive structure theorem, and its content is that the associativity of the plain product, read through the anti-automorphism ${}^{\natural}$, is exactly what survives as the composition law of the operators.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2 = -e_0$ |
| $\tilde P = \sum_\mu P_\mu e_\mu$ | an element and its four complex coordinates |
| ${}^{\natural}$ | the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$ |
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product, the multiplication of this group |
| $\tilde P\tilde Q$ | the plain (associative) product of the algebra |
| $L_{\tilde P}$ | the left multiplication $\tilde X\mapsto\tilde P\star\tilde X = \tilde P^{\natural}\tilde X$ |
| $R_{\tilde P}$ | the right multiplication of the product, $\tilde X\mapsto\tilde X\star\tilde P = \tilde X^{\natural}\tilde P$ |
| $\varrho_{\tilde P}$ | the twisted right multiplication $\tilde X\mapsto\tilde X\tilde P^{\natural}$ |
| $M_L$, $M_R$ | the monoids of left and of twisted right multiplications |
| $M_L \cong \mathbb{B}^{\mathrm{op}}$, $M_R \cong \mathbb{B}$ | the two isomorphism statements |
| $N(\tilde P)$ | the norm, so that $\tilde P$ is a unit exactly when $N(\tilde P)\neq0$ |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the left and the right multiplications of a non-associative algebra and the multiplication algebra they generate.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for algebras defined by a twisting map and the way the twisting reverses the order of the composition of multiplications.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the algebra of endomorphisms generated by the left and the right multiplications of a module.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for an anti-automorphism of order two acting on an algebra and reversing the products of its multiplications.
- Pavel Etingof, Oleg Golberg, Sebastian Hensel, Tiankai Liu, Alex Schwendner, Dmitry Vaintrob and Elena Yudovina, *Introduction to Representation Theory* (American Mathematical Society, 2011), for the identification of the multiplication algebra of a full matrix algebra with the full endomorphism algebra.
