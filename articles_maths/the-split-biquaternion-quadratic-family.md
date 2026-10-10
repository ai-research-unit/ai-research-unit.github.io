# __The Split-Biquaternion Quadratic Family__

## Introduction

The split-biquaternion quadratic family is the map $\tilde Q\mapsto\tilde Q^2+\tilde C$ in the split-biquaternion algebra $\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$, and it differs from the biquaternion family in one structural respect that decides everything: the idempotents of $\mathbb{H}_{\mathbb{D}}$ are central, so they decompose the algebra, the map and the parameter at once, and the family is the product of two ordinary quaternion quadratic families. The biquaternion algebra, with its non-central idempotents, splits the dynamics only on a slice and couples the two halves through the off-diagonal blocks; the split-biquaternion algebra has no coupling at all. The whole of the split-biquaternion fractal theory is therefore the quaternion theory of the preceding thread, read on two factors, and the article states the reduction, the escape dichotomy, the filled Julia set and the Julia set as products, the norm and the zero divisors in the product picture, and the symmetry of the family.

The split-biquaternion algebra, its conjugations, its central idempotents and its isomorphism with $\mathbb{H}\oplus\mathbb{H}$ are *Split-Biquaternion Algebra*, *Split-Biquaternion Idempotents and Projections* and *Split-Biquaternion Ideals and Peirce Decomposition*; the $\mathbb{D}$-valued norm and the units are *Split-Biquaternion Norm and Invertibility*; the zero divisors are *Split-Biquaternion Zero Divisors*; the Clifford description is *Complex Split-Biquaternions and the Clifford Algebra Cl(3)*. The quaternion quadratic family and its theory are *The Quaternion Quadratic Map and Its Julia Sets*, *The Escape Radius and the Green's Function for Quaternions* and *The Quaternion Mandelbrot Set*; the indefinite four-dimensional neighbour is *The Split-Quaternion Quadratic Map and Its Julia Sets*. No physics is invoked.

The article owns the idempotent splitting of the family, the transport of the orbit to a pair of quaternion orbits, the escape dichotomy in product form, the filled Julia set and the Julia set of the split-biquaternion family, the critical orbit and the connectedness reduction, the norm and the zero divisors, and the symmetry. It does not re-derive the quaternion theory it quotes.

**Standing convention.** $\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ with central split unit $j$, $j^2=+1$, $\tilde\Pi_{1,2}=\tfrac12(e_0\pm j)$, and

$$
\tilde Q=\tilde Q_+\tilde\Pi_1+\tilde Q_-\tilde\Pi_2, \qquad \tilde Q_\pm=\tilde Q\tilde\Pi_{1,2}\in\mathbb{H} .
$$

The quadratic family is $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$ in the split-biquaternion product, $\tilde C_\pm=\tilde C\tilde\Pi_{1,2}$, and $\|\cdot\|_E$ is the Euclidean norm of $\mathbb{H}_{\mathbb{D}}\cong\mathbb{R}^8$.

## The Idempotent Splitting

**Proposition (the splitting of the family).** The central idempotents give an algebra isomorphism $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$, $\tilde Q\mapsto(\tilde Q_+,\tilde Q_-)$, which is an isometry in the scaled sense

$$
\|\tilde Q\|_E^2=\tfrac12\bigl(\|\tilde Q_+\|^2+\|\tilde Q_-\|^2\bigr) ,
$$

and conjugates the quadratic family to the product of two quaternion quadratic families,

$$
F_{\tilde C}\;\longleftrightarrow\; (\tilde Q_+,\tilde Q_-)\longmapsto\bigl(\tilde Q_+^2+\tilde C_+,\ \tilde Q_-^2+\tilde C_-\bigr) .
$$

**Proof.** $\tilde\Pi_{1,2}$ are central idempotent orthogonal projectors with $\tilde\Pi_1+\tilde\Pi_2=e_0$ and $\tilde\Pi_1\tilde\Pi_2=0$, so the Chinese-remainder decomposition $\tilde Q=\tilde Q_+\tilde\Pi_1+\tilde Q_-\tilde\Pi_2$ is an algebra isomorphism onto $\mathbb{H}\oplus\mathbb{H}$ (*Split-Biquaternion Ideals and Peirce Decomposition*). Writing $\tilde Q=\tilde A+j\tilde B$ with $\tilde A,\tilde B\in\mathbb{H}$ gives $\tilde Q_\pm=\tilde A\pm\tilde B$, a Hadamard change of coordinates, whence the norm identity. Squaring is componentwise because the idempotents are central: $\tilde Q^2=\tilde Q_+^2\tilde\Pi_1+\tilde Q_-^2\tilde\Pi_2$ since the cross terms carry $\tilde\Pi_1\tilde\Pi_2=0$.

**Corollary (the orbit is a pair of quaternion orbits).** $F_{\tilde C}^{\,n}(\tilde Q)$ corresponds to the pair $(f_{\tilde C_+}^{\,n}(\tilde Q_+),f_{\tilde C_-}^{\,n}(\tilde Q_-))$, the iterates of the quaternion quadratic maps $f_{\tilde c}(\tilde q)=\tilde q^2+\tilde c$ of the two parameters $\tilde C_\pm$.

**Proof.** Induction on $n$ from the proposition.

**Remark (no coupling).** In the biquaternion algebra the idempotents are non-central and the splitting survives only on the idempotent plane, with a coupling given by the off-diagonal entries (*The Idempotent Decomposition and the Split Fractal*). In the split-biquaternion algebra the idempotents are central, the splitting is of the algebra and of the family, and there is no coupling. **The split-biquaternion fractal theory is the only one of the two in which the dynamics is exactly a product, and every simplification of the subject follows from this single fact.**

## The Escape Lemma and the Filled Julia Set

**Lemma (escape).** Let $\tilde C\in\mathbb{H}_{\mathbb{D}}$ and put $r_\pm=1+|\tilde C_\pm|$, where $|\cdot|$ is the quaternion modulus. If $\|\tilde Q_+^{(n)}\|\geq r_+$ for some $n$, then $|\tilde Q_+^{(k)}|\to\infty$; the same with the minus sign.

**Proof.** The quaternion escape lemma applied to the factor $\tilde Q_+$, whose orbit is $\tilde Q_+^{(n+1)}=(\tilde Q_+^{(n)})^2+\tilde C_+$ (*The Quaternion Quadratic Map and Its Julia Sets*, §*The Escape Lemma*).

**Theorem (the filled Julia set is a product).** The filled Julia set of the split-biquaternion family is the product of the two quaternion filled Julia sets,

$$
K_{\tilde C}=K_{\tilde C_+}\times K_{\tilde C_-},
$$

under the isomorphism $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$, and the orbit of $\tilde Q$ is bounded in the Euclidean norm if and only if both quaternion orbits are bounded.

**Proof.** The orbit is the pair of the quaternion orbits, and the Euclidean norm is comparable to the pair of the quaternion moduli by the norm identity of the proposition, so the orbit is bounded exactly when both quaternion orbits are; the filled Julia set is the set of bounded orbits, hence the product of the two.

**Corollary (the escape criterion).** A point escapes the ball $B_{r_+}\times B_{r_-}$ of $\mathbb{H}_{\mathbb{D}}$ (in the idempotent coordinates) only if its orbit escapes; equivalently, every bounded orbit remains in the product of the two quaternion escape balls.

**Remark (the contrast with the biquaternion case).** The biquaternion escape radius fails for a non-real central parameter because the square can collapse towards the cone (*The Escape Radius and the Green's Function for the Biquaternions*). The split-biquaternion algebra has zero divisors as well, but they lie in the coordinate hyperplanes $\tilde Q_+=0$ or $\tilde Q_-=0$, and a zero divisor has a *coordinate* equal to zero, not a *collapse of the square*; the pair of quaternion escape lemmas is unaffected. **The zero divisors of the split-biquaternion algebra do not obstruct the escape radius in the Euclidean norm, and this is the technical difference between the two algebras.**

**Remark (the failure of a single radius in the $\mathbb{D}$-valued norm).** The norm $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$ is a split complex number, $\mathbb{R}$-valued only on the quaternion subspace and its translate $j\mathbb{H}$ and not comparable to the Euclidean norm elsewhere; its real part is $\|\tilde Q\|_E^2$ and its split part is $2j\sum_\mu\operatorname{Re}Q_\mu\operatorname{Im}Q_\mu$, which is indefinite. Because $\mathbb{D}$ is not ordered, there is no single number $R$ with a condition $N(\tilde Q)>R^2$ forcing escape, and no single escape radius exists in the $\mathbb{D}$-valued norm; the escape criterion of the family is the *pair* of the quaternion Euclidean radii $r_\pm=1+|\tilde C_\pm|$. **The single escape radius exists in the Euclidean norm and fails in the split-complex-valued norm, and the honest statement of the escape theory here is the pair of componentwise criteria.**

## The Julia Set

**Theorem (the Julia set of the product).** The Julia set of the split-biquaternion family is the boundary of the product,

$$
J_{\tilde C}=\bigl(J_{\tilde C_+}\times K_{\tilde C_-}\bigr)\cup\bigl(K_{\tilde C_+}\times J_{\tilde C_-}\bigr),
$$

and it is non-empty whenever one of the two quaternion Julia sets is non-empty.

**Proof.** The boundary of a product is the union of the products with one factor a boundary, $\partial(A\times B)=(\partial A\times B)\cup(A\times\partial B)$ for closed $A,B$ with the product topology; apply the previous theorem.

**Remark (the fractal is a product, not a new object).** Every property of the split-biquaternion Julia set that is a product property — connectedness, local connectedness, the dimension of the product, the Hausdorff measure of a product — follows from the corresponding property of the quaternion factors. **The split-biquaternion thread of the category is a reduction, and the article states the reduction rather than reproving the quaternion theory.** The genuinely split-biquaternion questions are the ones the product structure does not answer: the behaviour with respect to the $\mathbb{D}$-valued norm, the Clifford grading and the two-sided structure of an iterated function system, treated in the companion articles.

## The Norm, the Zero Divisors and the Critical Orbit

**Proposition (units and zero divisors).** A split biquaternion is a unit if and only if both $\tilde Q_\pm$ are non-zero quaternions; the zero divisors are the union of the two ideals

$$
\mathbb{H}\tilde\Pi_1\cup\mathbb{H}\tilde\Pi_2 =\{\tilde Q_-=0\}\cup\{\tilde Q_+=0\} ,
$$

each of real dimension four. The $\mathbb{D}$-valued norm is $\tilde Q\tilde Q^{\natural}=\tilde Q_+\tilde Q_+^{\natural}\tilde\Pi_1+\tilde Q_-\tilde Q_-^{\natural}\tilde\Pi_2$.

**Proof.** $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ is a product of division algebras; an element of a product is a unit if and only if both components are, and it is a zero divisor if and only if one component is zero (*Split-Biquaternion Zero Divisors*). The norm computation is the idempotent-basis form of the norm (*Split-Biquaternion Norm and Invertibility*).

**Proposition (the derivative and the critical orbit).** The derivative of the split-biquaternion family is the block-diagonal pair of the derivatives of the two quaternion factors, so the family is a local diffeomorphism exactly where both quaternion factors are, that is, off the union of the two hyperplanes $\{\operatorname{Re}\tilde Q_+=0\}$ and $\{\operatorname{Re}\tilde Q_-=0\}$ (*The Quaternion Quadratic Map and Its Julia Sets*, §*The Critical Point*). The critical orbit used for the connectedness locus is the orbit of $\tilde Q=0$, which is the pair of the quaternion critical orbits $0,\tilde C_\pm,(\tilde C_\pm)^2+\tilde C_\pm,\dots$.

**Proof.** The derivative of a componentwise map is block-diagonal in the idempotent coordinates, with the two quaternion derivatives as blocks; a block-diagonal map is invertible exactly when both blocks are, and the quaternion quadratic map is a local diffeomorphism off the hyperplane of the pure vectors, so the product is a local diffeomorphism off the union of the two hyperplanes. The critical orbit of each factor is the orbit of $0$ by the convention of the quaternion thread, in which the orbit of $0$ is the critical orbit of the invariant complex slice; the orbit of the pair $(0,0)$ is therefore the pair of the quaternion critical orbits (*The Quaternion Mandelbrot Set*).

**Theorem (the connectedness locus is a square).** Define the connectedness locus of the split-biquaternion family by the boundedness of its critical orbit,

$$
\mathcal{M}_{\mathbb{H}_{\mathbb{D}}}=\{\tilde C : \text{the orbit of } 0 \text{ under } F_{\tilde C} \text{ is bounded}\} ,
$$

in agreement with the quaternion convention (*The Quaternion Mandelbrot Set*). Then it is the product of the two quaternion connectedness loci,

$$
\mathcal{M}_{\mathbb{H}_{\mathbb{D}}}=\mathcal{M}_{\mathbb{H}}\times\mathcal{M}_{\mathbb{H}} ,
$$

identified with the pairs $(\tilde C_+,\tilde C_-)$. Separately, the filled Julia set $K_{\tilde C}=K_{\tilde C_+}\times K_{\tilde C_-}$ is connected if and only if both quaternion filled Julia sets $K_{\tilde C_\pm}$ are.

**Proof.** The orbit of $0$ is the pair of the quaternion orbits of $0$ under the two factors, so it is bounded exactly when both are, that is to $\tilde C_\pm\in\mathcal{M}_{\mathbb{H}}$. The connectedness statement is the product topology: a product of two non-empty compacta is connected if and only if both factors are.

**Remark (the critical orbit is not a critical value).** The critical point $0$ is not in general a critical value in the real sense; the family is not a holomorphic endomorphism with a single ramification value, and the connectedness criterion is the pair of critical-orbit criteria of the two quaternion factors. **The article uses the critical orbit only through the two quaternion criteria, and the local theory of each factor is left to the quaternion thread.**

## The Symmetry of the Family

**Proposition (equivariance and the automorphisms).** Every automorphism $g$ of the split-biquaternion algebra satisfies $g\circ F_{\tilde C}=F_{g(\tilde C)}\circ g$, and the family with $\tilde C$ fixed by $g$ has $g$ as a symmetry of its Julia set. The automorphism group contains the inner automorphisms of each factor, the swap of the two factors, and the anti-automorphism given by the quaternion conjugation.

**Proof.** An algebra automorphism commutes with the polynomial $x^2$ and is isometric for the Euclidean norm, so the equivariance and the invariance follow as in the biquaternion case (*The Three Conjugations and the Symmetric Biquaternion Fractals*); the group statement is the structure of the automorphism group of $\mathbb{H}\oplus\mathbb{H}$.

**Remark (the larger symmetry).** The split-biquaternion family has the product symmetry $\mathrm{Aut}(\mathbb{H})\times\mathrm{Aut}(\mathbb{H})\rtimes\mathbb{Z}/2$ acting on the pairs, where the factor swap and the two independent rotation groups are available; the biquaternion family has only the diagonal symmetry of the conjugations. **The product structure enlarges the symmetry as it enlarges the simplification, and the symmetric split-biquaternion fractals are exactly the pairs of symmetric quaternion fractals.**

## The Readings of the Square and the Open Questions

**Remark (the reading of the square).** The formula $\tilde Q\mapsto\tilde Q^2$ is read here with the split-biquaternion algebra product, the associative product of the algebra and the only reading under which the idempotents are central and the family factors into two quaternion families. The other bilinear products carried by the underlying real space give different maps, whose reading is the subject of the biquaternion thread and is not the family of this article; **the split-biquaternion family is defined by the algebra product, and the statement is the product decomposition proved above.**

**Remark (the open questions).** The split-biquaternion thread is the least developed of the eight fractal threads of the corpus, and the article records what is open: the monogenic and regular function theory of the split-biquaternion maps, which would play the role of holomorphy for the biquaternion family; the Fatou theory of the family away from the two ideals; the exact dimension of the product fractal at a non-scalar parameter, which needs the dimension of the quaternion Julia sets; and the extension of the systems and the pluripotential theory to the split case, where the $\mathbb{D}$-valued norm replaces the complex norm.

## Summary

The split-biquaternion quadratic family is, by the centrality of the idempotents $\tilde\Pi_{1,2}=\tfrac12(e_0\pm j)$, exactly the product of two quaternion quadratic families, with the norm identity $\|\tilde Q\|_E^2=\tfrac12(\|\tilde Q_+\|^2+\|\tilde Q_-\|^2)$; the orbit is the pair of the quaternion orbits and there is no coupling. The escape lemma of the quaternion factors gives the escape dichotomy for the product, the filled Julia set is the product $K_{\tilde C_+}\times K_{\tilde C_-}$, the Julia set is the boundary of the product $(J_+\times K_-)\cup(K_+\times J_-)$, and every product property of the fractal is inherited. The units are the pairs of non-zero quaternions and the zero divisors are the two four-dimensional ideals, so the zero divisors of the split-biquaternion algebra do not obstruct the escape radius, in contrast with the biquaternion case. The critical orbit is the pair of the quaternion critical orbits and the connectedness locus is the square $\mathcal{M}_{\mathbb{H}}\times\mathcal{M}_{\mathbb{H}}$ of the quaternion connectedness locus. The symmetry group is the product of the automorphism groups of the two factors together with the swap.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}}=\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | the split-biquaternion algebra |
| $j$, $j^2=+1$ | the central split unit |
| $\tilde\Pi_{1,2}=\tfrac12(e_0\pm j)$ | the central idempotents |
| $\tilde Q_\pm=\tilde Q\tilde\Pi_{1,2}\in\mathbb{H}$ | the two quaternion components |
| $\tilde C_\pm=\tilde C\tilde\Pi_{1,2}$ | the two quaternion parameters |
| $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$ | the quadratic family |
| $K_{\tilde C_+}\times K_{\tilde C_-}$ | the filled Julia set |
| $\mathcal{M}_{\mathbb{H}}\times\mathcal{M}_{\mathbb{H}}$ | the connectedness locus |
| $\mathbb{H}\tilde\Pi_{1,2}$ | the two ideals of zero divisors |

## Further Reading

- *Split-Biquaternion Algebra* (`articles_maths/split-biquaternion-algebra.md`) and *Split-Biquaternion Idempotents and Projections* (`articles_maths/split-biquaternion-idempotents-and-projections.md`), for the algebra and the central idempotents.
- *Split-Biquaternion Norm and Invertibility* (`articles_maths/split-biquaternion-norm-and-invertibility.md`) and *Split-Biquaternion Zero Divisors* (`articles_maths/split-biquaternion-zero-divisors.md`), for the norm and the ideals.
- *The Quaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-quaternion-quadratic-map-and-its-julia-sets.md`), *The Escape Radius and the Green's Function for Quaternions* (`articles_maths/the-escape-radius-and-the-greens-function-for-quaternions.md`) and *The Quaternion Mandelbrot Set* (`articles_maths/the-quaternion-mandelbrot-set.md`), for the quaternion theory read here on two factors.
- *The Split-Biquaternion Julia Sets* (`articles_maths/the-split-biquaternion-julia-sets.md`), for the fractal structure of the product.
- *The Idempotent Decomposition and the Split Fractal* (`articles_maths/the-idempotent-decomposition-and-the-split-fractal.md`), for the biquaternion contrast in which the splitting is only a slice.
