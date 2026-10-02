
# __The Involution on a Topological Tensor Product__

## Introduction

Two involutions, one on each factor of a topological tensor product, induce an involution of the product by the formula $x \otimes y \mapsto \theta x \otimes \omega y$, and this induced involution is continuous for the projective and the injective topology and extends to both completions; a single involution of $E$ acting on $E \otimes E$ commutes with the **flip** $\tau(x \otimes y) = y \otimes x$, so it preserves the symmetric and the antisymmetric parts into which $E \otimes E$ splits when $2$ is invertible, and the involution of the product has fixed and negated parts computed from the four pieces of the two factors. Without nuclearity the projective and injective completions differ, and the induced involution is carried by each of them, with the flip continuous for both topologies and the symmetric and antisymmetric parts closed in each completion.

This article develops the involution of a topological tensor product. The projective and injective topologies, the canonical map, the universal property and the completions are *Topological Tensor Products*; the nuclear case, where the two completions coincide, is *Involutive Nuclear Spaces*; the continuous involution, the splitting and the extension to the completion are *Involutive Topological Linear Spaces* and *Locally Convex Spaces with an Involution*; the closed graph and the strong dual are *Involutive Fréchet Spaces* and *Duality Theory*. The graded tensor product and the sign rule of the graded category are *The Graded Action on a Module over a Topological Vector Space* and the graded-algebra category of this Part. No form, no adjoint and no Hilbert structure is used.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $\varsigma$ is the involution of $\mathbb{K}$, $E$ and $F$ are Hausdorff locally convex spaces over $\mathbb{K}$, $\theta$ and $\omega$ are continuous $\varsigma$-semilinear involutions of $E$ and $F$, the linear case is written $T$ and $S$, the summands are $E_{+} = E^{\theta}$, $E_{-} = E^{-}$, $F_{+} = F^{\omega}$, $F_{-} = F^{-}$, the flip is $\tau$, and the completions are $E \widehat{\otimes}_\pi F$ and $E \widehat{\otimes}_\varepsilon F$.

## The Involution on the Algebraic Tensor Product

**Definition.** For continuous involutions $\theta$ of $E$ and $\omega$ of $F$ with the same scalar involution $\varsigma$, the **induced involution** is the map $\theta \otimes \omega$ on $E \otimes F$ determined by

$$
(\theta \otimes \omega)(x \otimes y) = \theta x \otimes \omega y ,
$$

extended $\varsigma$-semilinearly to the whole tensor product; it is $\varsigma$-semilinear, hence linear when both factors are linear and antilinear when both are antilinear. (The map is well defined for $\varsigma$-semilinear factors precisely because the two bilinear relations give the same image, $\varsigma(r)\theta x\otimes\omega y$.)

**Proposition (the induced map is an involution).** The map $\theta \otimes \omega$ is an involution of $E \otimes F$ of the same kind as the factors, and it is continuous for the projective and the injective topology.

**Proof.** On a decomposable tensor $(\theta \otimes \omega)^{2}(x \otimes y) = \theta^{2}x \otimes \omega^{2}y = x \otimes y$, and the decomposable tensors span; the kind is read from the semilinearity. Continuity for the projective topology follows because $\theta \otimes \omega$ is the tensor product of the continuous maps $\theta$ and $\omega$, and for the injective topology because the topology is induced by the duality with the bounded bilinear forms and the involution acts continuously on those, by *Topological Tensor Products*.

**Theorem (the signature of the product).** Let $T$ and $S$ be linear involutions. Then the induced involution of $E \otimes F$ has

$$
(E \otimes F)^{+} = (E_{+} \otimes F_{+}) \oplus (E_{-} \otimes F_{-}), \qquad
(E \otimes F)^{-} = (E_{+} \otimes F_{-}) \oplus (E_{-} \otimes F_{+}) ,
$$

and in the types $(p,q)$ of $T$ and $(r,s)$ of $S$ the type of the product is $(pr + qs,\, ps + qr)$.

**Proof.** This is the signature computation of *Involutive Nuclear Spaces*; it uses only the tensor product and does not need nuclearity.

## The Flip and the Symmetric and Antisymmetric Parts

**Definition.** The **flip** is the linear map $\tau : E \otimes F \to F \otimes E$ determined by $\tau(x \otimes y) = y \otimes x$; on $E \otimes E$ it is an involution of $E \otimes E$, and the **symmetric part** and the **antisymmetric part** are

$$
\mathrm{Sym}^{2}(E) = \ker(\tau - \mathrm{id}), \qquad \Lambda^{2}(E) = \ker(\tau + \mathrm{id}) .
$$

**Proposition (the flip is continuous and extends).** The flip is continuous for the projective and the injective topologies, it extends to a continuous involution $\widehat{\tau}$ of each of the completions $E \widehat{\otimes}_\pi F$ and $E \widehat{\otimes}_\varepsilon F$, and when $2$ is invertible the completions decompose as

$$
E \widehat{\otimes}_\bullet E = \overline{\mathrm{Sym}^{2}(E)} \oplus \overline{\Lambda^{2}(E)} ,
$$

the closures being taken in the completion.

**Proof.** The flip is the canonical isomorphism of *Topological Tensor Products*, continuous for both topologies, and its square is the identity; the averaging maps $\frac12(\mathrm{id}\pm\tau)$ are continuous linear projections when $2$ is invertible, and the completion of a topological direct sum is the direct sum of the closures.

**Theorem (the induced involution commutes with the flip).** For a continuous involution $\theta$ of $E$ the induced involution $\theta \otimes \theta$ of $E \otimes E$ commutes with the flip,

$$
(\theta \otimes \theta)\,\tau = \tau\,(\theta \otimes \theta) ,
$$

so the symmetric and antisymmetric parts are $\theta \otimes \theta$-stable; on $\mathrm{Sym}^{2}(E)$ the fixed part is $\mathrm{Sym}^{2}(E_{+}) \oplus \mathrm{Sym}^{2}(E_{-})$ and on $\Lambda^{2}(E)$ it is $\Lambda^{2}(E_{+}) \oplus \Lambda^{2}(E_{-})$, the cross terms $E_{+} \otimes E_{-}$ lying in the negated part.

**Proof.** $(\theta \otimes \theta)\tau(x \otimes y) = \theta y \otimes \theta x = \tau(\theta x \otimes \theta y) = \tau(\theta \otimes \theta)(x \otimes y)$, so the two commute; hence $\ker(\tau \mp \mathrm{id})$ is preserved. On a symmetrised product $x_{+}\otimes x_{+}' + x_{+}' \otimes x_{+}$ with both factors in $E_{+}$ the involution is the identity, and likewise for $E_{-}$; a cross term $x_{+}\otimes x_{-} + x_{-}\otimes x_{+}$ is sent to its negative, since $\theta x_{\pm} = \pm x_{\pm}$.

**Corollary (the involution on the symmetric and the antisymmetric tensor powers).** The induced involution restricts to involutions of the symmetric and the antisymmetric square, of the same kind, and their fixed and negated parts are those of the restrictions; over $\mathbb{K} = \mathbb{C}$ with an antilinear involution the restricted involutions are antilinear with the same signature, computed over $\mathbb{R}$.

**Proof.** A restriction of an involution to a stable subspace is an involution, and the kind and the signature are inherited from the theorem, the scalar involution acting as before.

## The Completions and the Tensor Algebra

**Theorem (the involution on the completions).** The induced involution extends uniquely to a continuous involution of the projective completion $E \widehat{\otimes}_\pi F$ and of the injective completion $E \widehat{\otimes}_\varepsilon F$, of the same kind, and its fixed and negated subspaces in each completion are the closures of those of the algebraic tensor product,

$$
(E \widehat{\otimes}_\bullet F)^{+} = \overline{(E_{+} \otimes F_{+}) \oplus (E_{-} \otimes F_{-})}, \qquad
(E \widehat{\otimes}_\bullet F)^{-} = \overline{(E_{+} \otimes F_{-}) \oplus (E_{-} \otimes F_{+})} .
$$

**Proof.** The induced involution is continuous on the algebraic tensor product for each topology, so it extends to the completion by *Involutive Topological Linear Spaces*, uniquely because the tensor product is dense; the fixed and negated subspaces of the extension are the closures of those of the dense subspace, by the extension theorem of *Involutive Banach Spaces*, carried over to the locally convex setting.

**Proposition (the tensor algebra).** For a continuous involution $\theta$ of $E$ the induced involutions on the tensor powers $E^{\otimes n}$ assemble into an involution of the tensor algebra $\bigotimes E$ and, by continuity, of its completion, and the flip and the involution together generate a finite group acting on each tensor power; the graded commutative structure and the sign rule are those of the graded-algebra category and are named, not used.

**Proof.** The involution on $E^{\otimes n}$ is the tensor power of $\theta$, compatible with the multiplication $E^{\otimes m} \otimes E^{\otimes n} \to E^{\otimes(m+n)}$ because the tensor product of the involutions corresponds to the induced involution on the product; the compatibility with the completion is the extension theorem, and the group statement is that $\tau$ and $\theta \otimes \theta$ commute and are involutions.

## Examples

**Example (the tensor square of the plane).** On $E = \mathbb{R}^{2}$ with $T = \mathrm{diag}(1,-1)$ the involution $T \otimes T$ of $\mathbb{R}^{2}\otimes\mathbb{R}^{2}$ has fixed part $E_{+}\otimes E_{+} \oplus E_{-}\otimes E_{-}$ of dimension $2$ and negated part $E_{+}\otimes E_{-} \oplus E_{-}\otimes E_{+}$ of dimension $2$, so the type of $T \otimes T$ is $(2,2)$, in agreement with $(pr + qs, ps + qr)$ for the type $(1,1)$; the flip commutes with $T \otimes T$ and the symmetric part is split into the symmetric squares of the two axes in the fixed part.

**Example (the tensor product of two spaces with a grading).** For $E = E_{0}\oplus E_{1}$ and $F = F_{0}\oplus F_{1}$ with the linear involutions $\pm\mathrm{id}$ on the pieces, the induced involution of $E\otimes F$ is the grading $E\otimes F = (E_{0}\otimes F_{0}\oplus E_{1}\otimes F_{1}) \oplus (E_{0}\otimes F_{1}\oplus E_{1}\otimes F_{0})$, the standard tensor product of gradings; the flip exchanges the two cross terms, and a single involution of $E$ acts on $E\otimes E$ preserving the symmetric and antisymmetric parts.

**Example (the antilinear case).** On $\mathbb{C}^{n}\otimes\mathbb{C}^{m}$ with the componentwise conjugations, the induced involution is antilinear, the conjugation of the complex tensor product with respect to the real form $\mathbb{R}^{n}\otimes_{\mathbb{R}}\mathbb{R}^{m}$; its fixed subspace over $\mathbb{R}$ is that real tensor product, of real dimension $nm$, its negated subspace is $i$ times it, and the two pieces $E_{+}\otimes F_{+}$ and $E_{-}\otimes F_{-}$ of the signature formula coincide, because $E_{-} = iE_{+}$ and $F_{-} = iF_{+}$.

## Summary

Two continuous involutions of the factors of a topological tensor product induce an involution $\theta \otimes \omega$ of the algebraic tensor product, of the same kind as the two factors, continuous for the projective and the injective topology and extending uniquely to both completions; the product of two linear involutions has fixed part $(E_{+}\otimes F_{+})\oplus(E_{-}\otimes F_{-})$ and negated part $(E_{+}\otimes F_{-})\oplus(E_{-}\otimes F_{+})$, of type $(pr+qs, ps+qr)$, while for a pair of antilinear involutions the induced map is antilinear with real fixed part $E_{+}\otimes F_{+}$ and negated part $i(E_{+}\otimes F_{+})$, the two pieces of the linear formula coinciding because $E_{-} = iE_{+}$. The flip $\tau$ is a continuous involution of $E \otimes E$, extends to the completions, and decomposes each completion into the closures of the symmetric and antisymmetric parts when $2$ is invertible; a single involution $\theta$ of $E$ induces $\theta \otimes \theta$, which commutes with the flip, so the symmetric and antisymmetric parts are stable, their fixed parts being the symmetric and antisymmetric squares of the summands and the cross terms negated. The induced involutions on the tensor powers assemble into an involution of the tensor algebra and of its completion. The tensor square of the plane with the diagonal involution, the tensor product of two gradings and the antilinear case of two conjugations are the standard examples. When a factor is nuclear the two completions coincide, and the account of *Involutive Nuclear Spaces* applies.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$, $F$ | Hausdorff locally convex spaces over $\mathbb{K}$ |
| $\theta$, $\omega$, $T$, $S$ | Continuous involutions of the factors |
| $\theta \otimes \omega$ | Induced involution of $E \otimes F$ |
| $E_{+}$, $E_{-}$ | Fixed and negated summands of $E$ |
| $(E\otimes F)^{+} = (E_{+}\otimes F_{+})\oplus(E_{-}\otimes F_{-})$ | Fixed part of the product |
| $(E\otimes F)^{-} = (E_{+}\otimes F_{-})\oplus(E_{-}\otimes F_{+})$ | Negated part of the product |
| $\tau(x \otimes y) = y \otimes x$ | Flip |
| $\mathrm{Sym}^{2}(E)$, $\Lambda^{2}(E)$ | Symmetric and antisymmetric parts, $\ker(\tau \mp \mathrm{id})$ |
| $E \widehat{\otimes}_\pi F$, $E \widehat{\otimes}_\varepsilon F$ | Projective and injective completions |

## Further Reading

- Alexander Grothendieck, "Produits tensoriels topologiques et espaces nucléaires", *Memoirs of the AMS* **16** (1955), for the projective and injective tensor products and their completions.
- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the tensor product topologies and the symmetric and antisymmetric parts.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the tensor products, the flip and the graded structures.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the symmetric and antisymmetric parts and the tensor algebra.
- François Trèves, *Topological Vector Spaces, Distributions and Kernels* (Academic Press, 1967), for the completed tensor products and their involutions.
