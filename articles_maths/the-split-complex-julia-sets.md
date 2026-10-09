# __The Split-Complex Julia Sets__

## Introduction

The split-complex quadratic family $f_c(z) = z^2+c$ of *The Split-Complex Quadratic Family* is a map of the plane that is, in the idempotent coordinates $\varphi(z) = (z_+,z_-)$, the pair of one-dimensional maps $g_+(u) = u^2+c_+$ and $g_-(v) = v^2+c_-$. This article defines the Fatou and the Julia sets of such a map and proves the structure that the product decomposition forces: the Fatou set is the product $F_c = \varphi^{-1}(F_+ \times F_-)$ of the real Fatou sets, and the Julia set is the union of the two products $J_c = \varphi^{-1}\bigl((J_+ \times \mathbb{R}) \cup (\mathbb{R} \times J_-)\bigr)$ of the real Julia sets, one for each idempotent coordinate. The filled Julia set is the compact product $K_c = \varphi^{-1}(K_+ \times K_-)$ of the real filled Julia sets. The two forms of the norm, $N(z) = a^2-a'^2 = z_+z_-$, and their level sets — the hyperbolas that replace the circles of the complex case — are described, together with the degeneration of the polar decomposition on the null cone and the splitting of the Newton method.

The point of the article is honesty about what is transferred and what is new. The definition of the Fatou and Julia sets, the completeness of the invariant sets and the coding are transferred from the one-dimensional theory, applied to the two real maps; the genuinely new phenomenon is that the Julia set of the plane map is a **union of two products** and is in general unbounded, whereas the Julia set of a polynomial in $\mathbb{C}$ is compact. The complex case that the comparison uses is *The Julia Sets of a Complex Polynomial* and *The Mandelbrot Set and the Quadratic Family*; the algebra, the idempotents and the null cone are those of *Split-Complex Algebra*, *Split-Complex Idempotents and Projections* and *Split-Complex Null Quadric and Projective Geometry*; the hyperbolic geometry of the sets is the subject of *The Hyperbolic Geometry of the Split-Complex Julia Sets*; and the general theory of the real dynamics is cited to the real quadratic family. No physics is invoked.

## The Two Sets

### The Definition

**Definition.** Let $f_c(z) = z^2+c$ with $c \in \mathbb{D}$. The **Fatou set** $F_c$ is the set of points $z$ for which the family of iterates $\{f_c^n\}$ is **equicontinuous** on some neighbourhood of $z$, the plane being given the Euclidean metric and its one-point compactification; the **Julia set** is the complement

$$
J_c = \mathbb{D} \setminus F_c .
$$

That is, $z \in F_c$ when there is a neighbourhood $U$ of $z$ on which, for every $\varepsilon > 0$, there is $\delta > 0$ with $|f_c^n(z') - f_c^n(z'')| < \varepsilon$ for all $n$ whenever $z', z'' \in U$ with $|z'-z''| < \delta$; the distance in the compactification is the spherical one.

**Remark (why the definition is the metric one).** A split-complex polynomial is not holomorphic in the sense of *Complex Analysis*, and the theory of normal families of holomorphic maps does not apply. The definition above is the real two-dimensional analogue: a family is normal exactly when it is equicontinuous in the spherical metric, and the Fatou set is the locus of normality. This is the definition used for the real dynamics of Part III, and it reduces to the holomorphic definition when the map is complex.

**Theorem (the two sets are completely invariant).** $f_c(F_c) \subseteq F_c$, $f_c^{-1}(F_c) = F_c$, and $f_c(J_c) = J_c = f_c^{-1}(J_c)$; also $J(f_c) = J(f_c^n)$ for every $n \geq 1$.

**Proof.** A polynomial is proper of degree two, hence open and finite-to-one; composing an equicontinuous family with the continuous map $f_c$ and pulling it back preserve equicontinuity locally, which gives the invariance. The invariance under the iterate follows because the subfamily $\{f_c^{kn}\}$ controls the family $\{f_c^n\}$ in the same way as in the complex case.

### The Product Structure

**Theorem (the Fatou set is a product).** For every $c \in \mathbb{D}$ the Fatou set is the preimage under the isomorphism $\varphi$ of the product of the real Fatou sets,

$$
F_c = \varphi^{-1}\bigl(F_+ \times F_-\bigr) ,
$$

where $F_\pm$ is the Fatou set of the real quadratic map $g_\pm(x) = x^2 + c_\pm$ on $\mathbb{R}$.

**Proof.** The iterates satisfy $f_c^n = \varphi^{-1}\circ(g_+^n,g_-^n)\circ\varphi$. A family of maps into the product $\mathbb{R}^2$ is equicontinuous at a point if and only if each coordinate family is equicontinuous at the corresponding coordinate of the point: if one coordinate fails, a small perturbation produces a large change in that coordinate, hence in the pair; if both hold, the product estimate controls the pair. Applying this to $f_c^n$ and using that $\varphi$ is a bi-Lipschitz linear isomorphism gives the statement.

**Corollary (the Julia set is a union of two products).** The Julia set is

$$
J_c = \varphi^{-1}\Bigl(\bigl(J_+ \times \mathbb{R}\bigr) \cup \bigl(\mathbb{R} \times J_-\bigr)\Bigr) ,
$$

since the complement of $F_+ \times F_-$ in $\mathbb{R}^2$ is $(J_+ \times \mathbb{R}) \cup (\mathbb{R} \times J_-)$. In the coordinates $z = a+ja'$ the two pieces are the vertical and the horizontal product sets $\{z_+ \in J_+\}$ and $\{z_- \in J_-\}$, each a union of lines in the idempotent coordinates.

**Remark (transferred and new).** The structure of each factor — the compactness of $J_\pm$, its perfectness when nonempty, the density of the repelling periodic points — is the one-dimensional theory, transferred. What is new in the plane is that the Julia set is the union of two products, hence **unbounded** as soon as $J_+$ or $J_-$ is nonempty, and that $J_c$ is not contained in the filled Julia set in general. In the complex case the analogous statement is simply $J = J$, the product being absent.

### The Filled Julia Set

**Definition.** The **filled Julia set** of $f_c$ is

$$
K_c = \{z \in \mathbb{D} : \text{the orbit } (f_c^n(z)) \text{ is bounded}\} ,
$$

the compactness locus of the three sets; it is compact and contains $c$ exactly when $c \in M_{\mathbb{D}}$.

**Theorem (the filled Julia set is a compact product).** For every $c \in \mathbb{D}$,

$$
K_c = \varphi^{-1}\bigl(K_+ \times K_-\bigr) ,
$$

where $K_\pm$ is the real filled Julia set of $g_\pm$, the set of real $x$ with bounded orbit.

**Proof.** Boundedness of a sequence in $\mathbb{R}^2$ is boundedness of both coordinates, and the orbit in the coordinates is the pair of real orbits.

**Theorem (the relation between the three sets).** The real Julia set contains the boundary of the real filled Julia set, $\partial K_\pm \subseteq J_\pm$; hence
$$
\partial K_c \subseteq J_c \subseteq \varphi^{-1}\bigl(K_+\times\mathbb{R}\bigr)\cup\varphi^{-1}\bigl(\mathbb{R}\times K_-\bigr) ,
$$
and the second set is strictly larger than $K_c$ in general. The Julia set is **never** the boundary of the filled Julia set: $J_c$ is unbounded whenever $J_+$ or $J_-$ is nonempty, while $\partial K_c$, being a subset of the compact $K_c$, is compact. In the plane the two sets therefore never coincide, and the boundary of the filled Julia set is a proper part of the Julia set.

**Proof.** For the one-dimensional real map, a point of $\partial K_\pm$ has a bounded orbit and is not in the interior of $K_\pm$. If it were in the real Fatou set, its component would be either an interval of escaping points, which is impossible because the orbit is bounded and the iterates near it are not equicontinuous with it, or an interval of an attracting basin, which would be contained in $K_\pm$ and make the point interior to $K_\pm$; both are contradictions, so $\partial K_\pm \subseteq J_\pm$. Transporting through $\varphi$ and using the product formula for $J_c$ gives $\partial K_c \subseteq J_c$. The unboundedness of $J_c$ is the remark above, and $\partial K_c$ is compact because $K_c$ is.

## Examples

**Example ($c = 0$, the four lines).** The real map $g(x) = x^2$ has the filled Julia set $K = [-1,1]$ and the real Julia set $J = \{-1,+1\}$: the points of modulus less than one converge to the attracting fixed point $0$, the points of modulus greater than one escape, and at $\pm 1$ the derivatives $2x$ have modulus $2$, so the family is not equicontinuous. Hence

$$
J_0 = \varphi^{-1}\bigl(\{z_+ = \pm 1\} \cup \{z_- = \pm 1\}\bigr) = \{a+a' = \pm 1\} \cup \{a-a' = \pm 1\} ,
$$

the four lines bounding the square $K_0 = \{|a+a'| \leq 1,\ |a-a'| \leq 1\}$. So $J_0$ is the union of the four **lines**, unbounded, of Hausdorff dimension one, and it strictly contains $\partial K_0$, which is the union of the four **sides** of the square, each side lying on one of the lines: the identification of the Julia set with the boundary of the filled Julia set is exactly the statement of the complex case that fails here, and it fails because the two real Julia sets are the two-point boundaries of the real intervals and the products of the points with the line are unbounded.

**Example ($c = -2$, the two strips).** The real map $g(x) = x^2-2$ is conjugate to the doubling map through $x = 2\cos(\pi \theta)$, hence is chaotic on the whole interval $[-2,2]$, and its real Julia set and filled Julia set coincide: $J = K = [-2,2]$. Hence

$$
J_{-2} = \varphi^{-1}\bigl([-2,2] \times \mathbb{R} \cup \mathbb{R} \times [-2,2]\bigr) = \{|a+a'| \leq 2\} \cup \{|a-a'| \leq 2\} ,
$$

the union of two closed strips of width four crossing at forty-five degrees; it is unbounded, has two-dimensional Lebesgue measure, and strictly contains the square filled Julia set $K_{-2} = \{|a+a'| \leq 2,\ |a-a'| \leq 2\}$. So in this case $J_{-2} \neq \partial K_{-2}$ and the split-complex Julia set is not compact.

**Example (a real parameter with an attracting cycle).** Let $c = -1$, so $c_+ = c_- = -1$ and $g_\pm(x) = x^2-1$ has the attracting two-cycle $\{0,-1\}$. The real filled Julia set $K_\pm \subseteq [-2,2]$ is the closure of the union of the basin intervals, the real Julia set $J_\pm = \partial K_\pm$ is a closed set with empty interior, and the split Julia set is the union $J_{-1} = \varphi^{-1}((J\times\mathbb{R})\cup(\mathbb{R}\times J))$ of two products of $J$ with a line. The numerical orbit of the critical point, $0 \mapsto -1 \mapsto 0$, confirms the attracting cycle. No value of the dimension of $J_\pm$ is asserted; the dimension, when it is needed, is that of the geometric measure theory of *The Hyperbolic Geometry of the Split-Complex Julia Sets*.

## The Norm, the Null Cone and the Two Forms

**Theorem (the two forms).** The norm of $\mathbb{D}$ has the two equivalent forms

$$
N(z) = a^2 - a'^2 = z_+ z_- ,
$$

indefinite of signature $(1,1)$; its zero set is the **null cone** $\mathcal{N} = \mathbb{R}\Pi_+ \cup \mathbb{R}\Pi_-$, the two null lines $z_+ = 0$ and $z_- = 0$, whose nonzero elements are the zero divisors.

**Definition.** The **level sets of the norm** are the sets $N(z) = t$: for $t > 0$ the two branches of a hyperbola crossing the real axis at $\pm\sqrt{t}$; for $t < 0$ the two branches crossing the imaginary axis at $\pm\sqrt{|t|}j$; for $t = 0$ the two null lines. In the idempotent coordinates each level set is the hyperbola $z_+z_- = t$.

**Remark (the hyperbolas replacing the circles).** In the complex case the level sets of the modulus, $|z|^2 = $ const, are circles, and they are the equipotentials of the quadratic family. In the split case the level sets of the norm are hyperbolas with the null lines as the degenerate members; they are the natural equipotentials of the split-complex plane, and their asymptotes are the null directions. The Julia set, however, is assembled from the level sets of the **coordinate functionals** $z_+$ and $z_-$, which are the two families of lines parallel to the null lines, and not from the level sets of the norm: the product formula above can be read as saying that the Julia set is a union of two families of such lines, indexed by the real Julia sets.

**Remark (the polar decomposition degenerates on the null cone).** A nonzero element admits the polar decomposition $z = |N(z)|^{1/2}u$ with $u$ a unit only off the null cone; on the null lines the norm vanishes and the decomposition is undefined. This is why the definition and the study of the two sets are carried out in the idempotent coordinates and not in the polar coordinates of *Hyperbolic Rotations*: the polar form is available exactly on the units $\mathbb{D} \setminus \mathcal{N}$, and the coordinate form everywhere.

## The Newton Method

**Theorem (the Newton map splits).** Let $p(z) = \sum_{k=0}^{d} a_k z^k$ be a polynomial with coefficients $a_k \in \mathbb{D}$, and let $N_p(z) = z - p(z)/p'(z)$ be the Newton map of $p$, defined where $p'(z)$ is a unit. Then $N_p$ commutes with the idempotent decomposition: in the coordinates,

$$
\varphi\bigl(N_p(z)\bigr) = \bigl(N_{p_+}(z_+),\ N_{p_-}(z_-)\bigr) ,
$$

where $p_\pm(x) = \sum_k a_{k\pm} x^k$ is the real polynomial obtained from the coefficients of $p$ and $N_{p_\pm}$ is its real Newton map.

**Proof.** A polynomial with coefficients in $\mathbb{D}$ splits, $\varphi(p(z)) = (p_+(z_+), p_-(z_-))$, because $\varphi$ is a ring homomorphism and $\varphi(a_k) = (a_{k+},a_{k-})$; the same holds for the derivative. The quotient of two split-complex numbers with nonzero coordinates is componentwise in the coordinates, since $\Pi_\pm$ are orthogonal idempotents; hence the Newton quotient splits, and the formula follows.

**Corollary.** The Fatou set of the Newton map is $\varphi^{-1}(F_{p_+} \times F_{p_-})$ and its Julia set is $\varphi^{-1}((J_{p_+}\times\mathbb{R})\cup(\mathbb{R}\times J_{p_-}))$, with the real Newton basins of the two factor polynomials as the factors. In particular the fractal Newton basins of a real polynomial with distinct real roots are the products of the real basins and their boundaries, and the "Newton fractal" of the split-complex plane is a union of two products of one-dimensional basins.

**Example.** Let $p(z) = z^2-1$, so that $p_\pm(x) = x^2-1$ and the Newton map is $N(z) = \tfrac12(z + z^{-1})$ on the units. The real Newton map $N(x) = \tfrac12(x + x^{-1})$ is defined for $x \neq 0$, has the two superattracting fixed points $\pm 1$, and its real Julia set on the projective line $\mathbb{R}\cup\{\infty\}$ is $\{0,\infty\}$; the two real basins are the half-lines $(0,\infty)$ and $(-\infty,0)$. The split-complex equation $z^2-1 = 0$ has the four roots $\pm1$ and $\pm j$, which are the preimages under $\varphi$ of the four sign pairs; the basin of the root with sign pair $(\epsilon,\eta)$ is $\varphi^{-1}\bigl(B_{\epsilon}\times B_{\eta}\bigr)$, the region where $z_+$ has the sign $\epsilon$ and $z_-$ the sign $\eta$, that is, one of the four quadrants of the idempotent plane. The Newton Julia set is the common boundary, the union of the two null lines and the line at infinity. The example shows that the Newton fractal of a real polynomial splits, and that its pieces are the four general products of the one-dimensional basins.

## Summary

The Fatou set of a split-complex quadratic map $f_c(z) = z^2+c$ is the locus of equicontinuity of the iterates, and the Julia set is its complement. In the idempotent coordinates $\varphi(z) = (z_+,z_-)$ the map is the pair of real quadratic maps $u \mapsto u^2+c_+$, $v \mapsto v^2+c_-$, and the two sets factor: $F_c = \varphi^{-1}(F_+ \times F_-)$ is a product, while $J_c = \varphi^{-1}((J_+ \times \mathbb{R}) \cup (\mathbb{R} \times J_-))$ is the union of two products and is unbounded in general. The filled Julia set is the compact product $K_c = \varphi^{-1}(K_+ \times K_-)$ of the real filled Julia sets, and the two sets never coincide: $J_c$ contains $\partial K_c$ and is unbounded, so it is never equal to the compact $\partial K_c$. For $c = 0$ the Julia set is the four lines $a \pm a' = \pm 1$, containing the four sides of the square; for $c = -2$ it is the union of two crossing strips while the filled Julia set is their intersection.

The norm is indefinite, with the two forms $N = a^2-a'^2 = z_+z_-$; its level sets are the hyperbolas and the two null lines, replacing the circles of the complex case, and its vanishing locus is the null cone of the zero divisors, on which the polar decomposition is undefined. The two sets are nevertheless defined everywhere, in the idempotent coordinates, and the Newton map of a split-complex polynomial splits in the same way. The general one-dimensional theory is cited to the real quadratic family; the geometry of the sets with the hyperbolic rotations is the subject of *The Hyperbolic Geometry of the Split-Complex Julia Sets*, and the complex case that the comparison uses is *The Julia Sets of a Complex Polynomial*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f_c(z) = z^2+c$ | Split-complex quadratic map |
| $\varphi(z) = (z_+,z_-) = (a+a',a-a')$ | Idempotent coordinates |
| $g_\pm(x) = x^2+c_\pm$ | The pair of real quadratic maps |
| $F_c$, $J_c$ | Fatou set, Julia set of $f_c$ |
| $F_\pm$, $J_\pm$ | Fatou and Julia sets of the real maps |
| $K_c = \varphi^{-1}(K_+\times K_-)$ | Filled Julia set, the compact product |
| $N(z) = a^2-a'^2 = z_+z_-$ | Norm, indefinite |
| $\mathcal{N} = \mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$ | Null cone, the two null lines |
| $N_p$ | Newton map, splitting as $N_{p_\pm}$ |

## Further Reading

- Robert L. Devaney, *An Introduction to Chaotic Dynamical Systems*, 2nd edition (Addison-Wesley, 1989), for the real quadratic dynamics and the Julia set of a real map.
- Pierre Fatou, "Sur les équations fonctionnelles", *Bulletin de la Société Mathématique de France* 47 (1919), 161–271; 48 (1920), 33–94, for the original equicontinuity definition of the two sets.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split-complex (hyperbolic) plane and its idempotent structure.
- John Milnor, *Dynamics in One Complex Variable*, 3rd edition (Princeton University Press, 2006), for the complex case used for comparison.
- John W. Milnor, "Remarks on iterated cubic maps", *Experimental Mathematics* 1 (1992), 5–24, for the real dynamics and the one-dimensional Julia sets.
