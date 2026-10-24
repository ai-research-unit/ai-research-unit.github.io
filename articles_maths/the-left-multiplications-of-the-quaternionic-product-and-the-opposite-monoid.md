
# __The Left Multiplications of the Quaternionic Product and the Opposite Monoid__

## Introduction

The product of this group is the **general quaternionic bilinear product**

$$
\tilde Q_1 \star \tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2 , \qquad \tilde Q_1^{\natural} = Q_{1t} - \vec Q_1 ,
$$

the second of the four general products of the biquaternion algebra $\mathbb{B}$ (*The Four General Products and Their Relations* §*The General Quaternionic Bilinear Product*), whose algebra is *Introduction to the General Quaternionic Algebra*. The four articles before this one are negative in their outcome: the product has no nontrivial idempotent, its square-zero set is the whole zero-divisor cone, it is associative at no rung of the ladder, and its symmetrisation is no Jordan algebra. This article is the batch's one positive structure theorem, and it is about the **operators** that the product defines rather than about the elements of the algebra.

For an element $\tilde Q_1$ the **left multiplication** is the map on $\mathbb{B}$ obtained by fixing $\tilde Q_1$ in the first slot,

$$
L_{\tilde Q_1}(\tilde Q_2) = \tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2 ,
$$

a linear endomorphism of $\mathbb{B}$. For an arbitrary non-associative product the composite of two left multiplications has no reason to be a left multiplication. Here it always is.

The article establishes four things. First, the left multiplications compose by the **reversed** law

$$
L_{\tilde Q_1}\circ L_{\tilde Q_3} = L_{\tilde Q_3\tilde Q_1} ,
$$

the product on the right being the *plain* product of the algebra, so that the set of left multiplications is a monoid isomorphic to the **opposite** of the multiplicative monoid of $\mathbb{B}$ — although $\star$ is not associative. Second, the right multiplications of the product do not close under composition, and the closed family on the right is the twisted one $\tilde Q_2\mapsto\tilde Q_2\tilde Q_1^{\natural}$, whose law is the **direct** one, $\varrho_{\tilde Q_1}\circ \varrho_{\tilde Q_3} = \varrho_{\tilde Q_1\tilde Q_3}$. Third, the mixed composites $L_{\tilde Q_1}\circ \varrho_{\tilde Q_3}$ commute and span the full endomorphism algebra, the multiplication algebra of $\mathbb{B}$, of dimension sixteen. Fourth, this is exactly the row of the property table of *The Four General Products and Their Relations* on the left multiplications, which reads yes for the two bilinear products and no for the two sesquilinear ones.

## The Left Multiplications

**Theorem (the composition law).** For all $\tilde Q_1,\tilde Q_3 \in \mathbb{B}$,

$$
\boxed{\; L_{\tilde Q_1}\circ L_{\tilde Q_3} = L_{\tilde Q_3\tilde Q_1} \;},
$$

where $\tilde Q_3\tilde Q_1$ is the plain product of the algebra.

**Proof.** For every $\tilde Q_2$,

$$
L_{\tilde Q_1}\bigl(L_{\tilde Q_3}(\tilde Q_2)\bigr) = \tilde Q_1^{\natural}\bigl(\tilde Q_3^{\natural}\tilde Q_2\bigr) = \bigl(\tilde Q_1^{\natural}\tilde Q_3^{\natural}\bigr)\tilde Q_2 = \bigl(\tilde Q_3\tilde Q_1\bigr)^{\natural}\tilde Q_2 = L_{\tilde Q_3\tilde Q_1}(\tilde Q_2) ,
$$

using the associativity of the plain product in the middle step and the fact that ${}^{\natural}$ is an anti-automorphism of order two, $\tilde Q_1^{\natural}\tilde Q_3^{\natural} = (\tilde Q_3\tilde Q_1)^{\natural}$, in the third.

**Remark (why associativity of $\star$ is not needed).** The proof uses the associativity of the **plain** product twice, and never the associativity of $\star$; and it is precisely because ${}^{\natural}$ reverses the order of a plain product that the law comes out reversed. This is the sense in which the left multiplications of $\star$ form a monoid for the same reason and with the same order reversal as the left multiplications of the algebra under the conjugation: the map $\tilde Q_1\mapsto L_{\tilde Q_1}$ intertwines $\star$ with the opposite of the plain product.

**Theorem (the monoid of left multiplications).** The set $M_L = \{L_{\tilde Q_1} : \tilde Q_1 \in \mathbb{B}\}$ is closed under composition and contains the identity $L_{e_t} = \mathrm{id}_{\mathbb{B}}$. The map $\tilde Q_1\mapsto L_{\tilde Q_1}$ is an injective anti-homomorphism of monoids from the multiplicative monoid of $\mathbb{B}$ onto $M_L$, so

$$
\boxed{\; M_L \cong \mathbb{B}^{\mathrm{opp}} \;},
$$

the opposite of the multiplicative monoid of $\mathbb{B}$.

**Proof.** Closure and the identity are read off the law: $L_{\tilde Q_1}L_{\tilde Q_3} = L_{\tilde Q_3\tilde Q_1}$ is again a left multiplication, and $L_{e_t}(\tilde Q_2) = e_t^{\natural}\tilde Q_2 = \tilde Q_2$. The law $L_{\tilde Q_1}L_{\tilde Q_3} = L_{\tilde Q_3\tilde Q_1}$ is exactly the statement that the assignment reverses the order of a product, so it is an anti-homomorphism; it is surjective onto $M_L$ by definition and injective because $L_{\tilde Q_1} = L_{\tilde Q_3}$ forces $\tilde Q_1^{\natural} = L_{\tilde Q_1}(e_t) = L_{\tilde Q_3}(e_t) = \tilde Q_3^{\natural}$ and hence $\tilde Q_1 = \tilde Q_3$.

**Corollary (the units).** The left multiplication $L_{\tilde Q_1}$ is invertible in $M_L$ exactly when $\tilde Q_1$ is a unit of the algebra, that is exactly when $\langle\tilde Q_1\rangle_{\natural} \neq 0$; the group of units of $M_L$ is therefore isomorphic to the group $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ with reversed product.

**Proof.** The operator $L_{\tilde Q_1}$ is the plain left multiplication by the element $\tilde Q_1^{\natural}$, so it is invertible exactly when $\tilde Q_1^{\natural}$ is a unit of the plain algebra, and the plain algebra is isomorphic to the matrix algebra $M_2(\mathbb{C})$, in which an element is a unit exactly when it is invertible as a matrix. The norm criterion says that $\tilde Q_1^{\natural}$ is invertible exactly when $\langle\tilde Q_1^{\natural}\rangle_{\natural} = \langle\tilde Q_1\rangle_{\natural} \neq 0$ (*Norm and Invertibility in the General Quaternionic Algebra*); since the anti-isomorphism $L$ carries the product to the reversed product and bijects $\mathbb{B}$ onto $M_L$, it carries the unit group to the unit group with the reversed law.

**Remark.** The anti-isomorphism is the boundary of what survives of associativity. For the associative product the assignment $\tilde Q_1\mapsto L_{\tilde Q_1}$ is a homomorphism of the whole algebra $\mathbb{B}$ into $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, and $\mathbb{B}$ acts on itself as an algebra of operators, with the left regular representation; for the quaternionic product only the multiplicative structure survives, and it survives reversed. The assignment is still additive and $\mathbb{C}$-linear, $L_{\tilde Q_1+\tilde Q_3}=L_{\tilde Q_1}+L_{\tilde Q_3}$ and $L_{\lambda\tilde Q_1}=\lambda L_{\tilde Q_1}$, and its failure is exactly the failure to respect $\star$: $L_{\tilde Q_1\star\tilde Q_3} = L_{\tilde Q_1^{\natural}\tilde Q_3}$ differs from $L_{\tilde Q_1}L_{\tilde Q_3} = L_{\tilde Q_3\tilde Q_1}$ in the placement of the conjugation between the two factors. What the product loses is therefore the representation of the algebra, not the monoid of its operators.

## The Right Multiplications

**Theorem (the right multiplications of the product do not close).** Let $R_{\tilde Q_1}(\tilde Q_2) = \tilde Q_2\star\tilde Q_1 = \tilde Q_2^{\natural}\tilde Q_1$ be the right multiplication of $\star$ by $\tilde Q_1$. Then the composite of two of them is

$$
R_{\tilde Q_1}\circ R_{\tilde Q_3}(\tilde Q_2) = \bigl(\tilde Q_2^{\natural}\tilde Q_3\bigr)^{\natural}\tilde Q_1 = \tilde Q_3^{\natural}\,\tilde Q_2\,\tilde Q_1 ,
$$

which is the plain product of $\tilde Q_3^{\natural}$, $\tilde Q_2$ and $\tilde Q_1$ in that order; and it is not a right multiplication of $\star$ unless it happens to coincide with one. At $\tilde Q_1 = \tilde Q_3 = \vec e_x$ the composite sends $e_t$ to $e_t$ and $\vec e_x$ to $\vec e_x$, whereas a right multiplication $\tilde Q_2\mapsto\tilde Q_2^{\natural}\tilde Q_5$ with the same value at $e_t$ has $\tilde Q_5 = e_t$ and sends $\vec e_x$ to $-\vec e_x$.

**Proof.** The first display is the computation $(\tilde Q_2^{\natural}\tilde Q_3)^{\natural} = \tilde Q_3^{\natural}\tilde Q_2$ followed by the plain product with $\tilde Q_1$; the witness is the evaluation $R_{\vec e_x}R_{\vec e_x}(e_t) = e_t$ and $R_{\vec e_x}R_{\vec e_x}(\vec e_x) = \vec e_x$.

The family that does close on the right is the one with the conjugation on the side of the multiplier, the mirror of the left multiplications.

**Theorem (the twisted right multiplications).** Define $\varrho_{\tilde Q_1}(\tilde Q_2) = \tilde Q_2\,\tilde Q_1^{\natural}$, the plain right multiplication by $\tilde Q_1^{\natural}$. Then

$$
\boxed{\; \varrho_{\tilde Q_1}\circ \varrho_{\tilde Q_3} = \varrho_{\tilde Q_1\tilde Q_3} \;},
$$

the **direct** law, and $M_R = \{\varrho_{\tilde Q_1}\}$ is a monoid containing $\varrho_{e_t} = \mathrm{id}_{\mathbb{B}}$ and isomorphic to the multiplicative monoid $\mathbb{B}$ itself.

**Proof.** $\varrho_{\tilde Q_1}(\varrho_{\tilde Q_3}(\tilde Q_2)) = \tilde Q_2\tilde Q_3^{\natural}\tilde Q_1^{\natural} = \tilde Q_2(\tilde Q_1\tilde Q_3)^{\natural} = \varrho_{\tilde Q_1\tilde Q_3}(\tilde Q_2)$, by the associativity of the plain product and the anti-automorphism property; the identity is $\varrho_{e_t}(\tilde Q_2) = \tilde Q_2 e_t^{\natural} = \tilde Q_2$, and injectivity is read at $e_t$ as before.

**Remark (why the two laws are opposite).** The asymmetry is the asymmetry of the product itself: in $\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2$ the conjugation sits on the **first** slot, so the left multiplication is the plain left multiplication by $\tilde Q_1^{\natural}$ and the right multiplication of the product is not the plain right multiplication by anything. Writing both operators with the conjugation attached to the multiplier restores the mirror symmetry: the left family is $M_L = \{L^{\mathrm{plain}}_{\tilde Q_1^{\natural}}\}$ and the right family is $M_R = \{R^{\mathrm{plain}}_{\tilde Q_1^{\natural}}\}$, with $M_L\cong\mathbb{B}^{\mathrm{opp}}$ and $M_R\cong\mathbb{B}$. The pair of laws $L_{\tilde Q_1}L_{\tilde Q_3} = L_{\tilde Q_3\tilde Q_1}$ and $\varrho_{\tilde Q_1}\varrho_{\tilde Q_3} = \varrho_{\tilde Q_1\tilde Q_3}$ is the exact form in which the two-sidedness of the plain product survives the twisting of a single slot.

## The Mixed Compositions

**Theorem (the mixed composites commute).** For all $\tilde Q_1,\tilde Q_3 \in \mathbb{B}$,

$$
L_{\tilde Q_1}\circ \varrho_{\tilde Q_3} = \varrho_{\tilde Q_3}\circ L_{\tilde Q_1} , \qquad L_{\tilde Q_1}\circ \varrho_{\tilde Q_3}(\tilde Q_2) = \tilde Q_1^{\natural}\tilde Q_2\tilde Q_3^{\natural} .
$$

**Proof.** Both sides send $\tilde Q_2$ to $\tilde Q_1^{\natural}\tilde Q_2\tilde Q_3^{\natural}$ by the associativity of the plain product.

**Theorem (the multiplication algebra).** The complex span of the operators $\{L_{\tilde Q_1}\circ \varrho_{\tilde Q_3} : \tilde Q_1,\tilde Q_3 \in \mathbb{B}\}$ is closed under composition and is all of the endomorphism algebra $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen.

**Proof.** Closure: $\bigl(L_{\tilde Q_1}\varrho_{\tilde Q_3}\bigr)\bigl(L_{\tilde Q_5}\varrho_{\tilde Q_4}\bigr) = L_{\tilde Q_1}L_{\tilde Q_5}\varrho_{\tilde Q_3}\varrho_{\tilde Q_4} = L_{\tilde Q_5\tilde Q_1}\varrho_{\tilde Q_3\tilde Q_4}$, by the two composition laws and the commutation of the mixed pair. For the dimension, $\mathbb{B}$ is isomorphic to the matrix algebra $M_2(\mathbb{C})$, and the operators of the form $\tilde Q_2\mapsto \tilde Q_1\tilde Q_2\tilde Q_3$ on $M_2(\mathbb{C})$ span the whole $\mathrm{End}_{\mathbb{C}}(M_2(\mathbb{C}))$, of dimension $4^2 = 16$, because the elementary matrices realise every prescribed action on a matrix unit. The twist ${}^{\natural}$ is a bijection of $\mathbb{B}$, so the family $\{L_{\tilde Q_1}\varrho_{\tilde Q_3}\}$ has the same span.

**Remark.** The closure computation is the pleasant surprise of the section: the two composition laws have opposite orders, and the opposite orders cancel in the mixed composite, $L_{\tilde Q_1}L_{\tilde Q_5}\varrho_{\tilde Q_3}\varrho_{\tilde Q_4} = L_{\tilde Q_5\tilde Q_1}\varrho_{\tilde Q_3\tilde Q_4}$, which is again of the required form. The algebra generated is therefore not merely a monoid but a full matrix algebra, and it carries no trace of the failure of associativity of $\star$; the failure is visible on the element level, not on the level of the operators.

**Remark (which pair commutes).** What commutes is $L_{\tilde Q_1}$ with the **twisted** right multiplication $\varrho_{\tilde Q_3}$, not with the right multiplication of the product: $L_{\tilde Q_1}$ and $R_{\tilde Q_1}$ do not commute, and at $\tilde Q_1 = \vec e_z$ the two composites send $e_t$ to $e_t$ and to $-e_t$, since $L_{\vec e_z}R_{\vec e_z}(e_t) = e_t$ and $R_{\vec e_z}L_{\vec e_z}(e_t) = -e_t$. This is the failure of flexibility of the third article read at the level of the operators, and it is why the multiplication algebra is built from $L$ and $\varrho$ and not from $L$ and $R$.

## The Interpretation of the Monoid Row

The property table of *The Four General Products and Their Relations* carries the four general products against the property "the left multiplications form a monoid" (*The Four General Products and Their Relations* §*The Property Table*), and the row reads

| product | left multiplications form a monoid |
|---|---|
| $\tilde Q_1\tilde Q_2$ | yes |
| $\tilde Q_1^{\natural}\tilde Q_2$ | yes |
| $\tilde Q_1\tilde Q_2^{*}$ | no |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | no |

The two bilinear columns are the two this article has just settled: for the associative product the law is the direct one, $L_{\tilde Q_1}L_{\tilde Q_3} = L_{\tilde Q_1\tilde Q_3}$, and for the quaternionic product it is the reversed one, $L_{\tilde Q_1}L_{\tilde Q_3} = L_{\tilde Q_3\tilde Q_1}$, so both families are monoids. The two sesquilinear products fail the row because the composition of two of their left multiplications is linear and not sesquilinear, and therefore not one of them (*The Four General Products and Their Relations* §*The Left Multiplications*); the reason has nothing to do with the associativity of the underlying product, and the comparison article records that the row is not implied by the associative row.

**Remark.** The row is the place where the quaternionic product is at its closest to the associative one. Neither is the algebra of the other, and both the element-theoretic data and the Jordan structure were changed by the twisting of the first slot; but the left multiplications, which read the product as an action of the algebra on itself, survive, and they survive as the opposite monoid. The next two articles carry the product down to the quaternion subspace, where the whole batch becomes classical, and into the matrix model, where it is read off the trace and the determinant.

## Summary

The left multiplications of the quaternionic product are $L_{\tilde Q_1}(\tilde Q_2) = \tilde Q_1^{\natural}\tilde Q_2$, and they compose by the reversed law $L_{\tilde Q_1}\circ L_{\tilde Q_3} = L_{\tilde Q_3\tilde Q_1}$, the product on the right being the plain product of the algebra; the set $M_L$ is a monoid with identity $L_{e_t}$, and $\tilde Q_1\mapsto L_{\tilde Q_1}$ is an isomorphism $M_L\cong\mathbb{B}^{\mathrm{opp}}$ onto the opposite of the multiplicative monoid, although $\star$ is not associative. The right multiplications of $\star$ do not close, their composite being $\tilde Q_3^{\natural}\tilde Q_2\tilde Q_1$; the closed family is the twisted one $\varrho_{\tilde Q_1}(\tilde Q_2) = \tilde Q_2\tilde Q_1^{\natural}$, with the direct law $\varrho_{\tilde Q_1}\varrho_{\tilde Q_3} = \varrho_{\tilde Q_1\tilde Q_3}$ and $M_R\cong\mathbb{B}$. The mixed composites commute, $L_{\tilde Q_1}\varrho_{\tilde Q_3} = \varrho_{\tilde Q_3}L_{\tilde Q_1}$, are closed under composition, and span the whole endomorphism algebra, of dimension sixteen. This is the row of the property table on the left multiplications, where the two bilinear products read yes and the two sesquilinear ones read no; it is the batch's one positive structure theorem, and its content is that the associativity of the plain product, read through the anti-automorphism ${}^{\natural}$, is exactly what survives as the composition law of the operators.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity, $\vec e_k^2 = -e_t$ |
| $\tilde Q = \sum_\mu Q_\mu e_\mu$ | an element and its four complex coordinates |
| ${}^{\natural}$ | the natural conjugation $\tilde Q^{\natural} = Q_t - \vec Q$ |
| $\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2$ | the general quaternionic bilinear product, the multiplication of this group |
| $\tilde Q_1\tilde Q_2$ | the plain (associative) product of the algebra |
| $L_{\tilde Q_1}$ | the left multiplication $\tilde Q_2\mapsto\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2$ |
| $R_{\tilde Q_1}$ | the right multiplication of the product, $\tilde Q_2\mapsto\tilde Q_2\star\tilde Q_1 = \tilde Q_2^{\natural}\tilde Q_1$ |
| $\varrho_{\tilde Q_1}$ | the twisted right multiplication $\tilde Q_2\mapsto\tilde Q_2\tilde Q_1^{\natural}$ |
| $M_L$, $M_R$ | the monoids of left and of twisted right multiplications |
| $M_L \cong \mathbb{B}^{\mathrm{opp}}$, $M_R \cong \mathbb{B}$ | the two isomorphism statements |
| $\langle\tilde Q\rangle_{\natural}$ | the norm, so that $\tilde Q$ is a unit exactly when $\langle\tilde Q\rangle_{\natural}\neq0$ |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the left and the right multiplications of a non-associative algebra and the multiplication algebra they generate.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for algebras defined by a twisting map and the way the twisting reverses the order of the composition of multiplications.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the algebra of endomorphisms generated by the left and the right multiplications of a module.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for an anti-automorphism of order two acting on an algebra and reversing the products of its multiplications.
- Pavel Etingof, Oleg Golberg, Sebastian Hensel, Tiankai Liu, Alex Schwendner, Dmitry Vaintrob and Elena Yudovina, *Introduction to Representation Theory* (American Mathematical Society, 2011), for the identification of the multiplication algebra of a full matrix algebra with the full endomorphism algebra.
