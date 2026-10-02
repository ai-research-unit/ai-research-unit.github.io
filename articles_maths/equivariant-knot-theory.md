
# __Equivariant Knot Theory__

## Introduction

A knot is **periodic** when it admits a periodic symmetry: an action of the cyclic group $\mathbb{Z}/n$ on the three-sphere preserving the knot, with an axis disjoint from the knot. The symmetry gives the knot a second, equivariant layer of invariants — the equivariant Seifert surface, the equivariant Seifert form, the equivariant signature, the equivariant Alexander module — and it produces a **quotient knot** whose invariants constrain those of the periodic knot. This article is the equivariant knot theory: the periodic knots, their quotients, and the invariants that live on the equivariant layer.

The subject is the meeting point of two theories already in the corpus: the knot theory of *Knot Theory*, which supplies the Seifert surfaces, the Alexander polynomial, the signatures and the branched covers, and the structure theory of *Involutions on Manifolds and Equivariant Surgery*, which supplies the fixed set, the equivariant neighbourhoods and the equivariant surgery. The outcome of the equivalence is the **equivariant Seifert form**, whose Wall class is the complete equivariant invariant of the knot's periodicity up to the usual surgery considerations.

**The article assumes** the Seifert surfaces, the Seifert form, the Alexander polynomial and the signature of *Knot Theory*, the double branched cover and the Goeritz matrix, the integral group ring and its involutions, and the equivariant surgery obstruction of *Involutions on Manifolds and Equivariant Surgery*.

**The boundaries of the article.** The knot theory without symmetries is *Knot Theory*; the chirality and the mirror are *Amphichiral Knots and the Orientation-Reversing Involution*, the previous article; the periodic maps of a general manifold are *Periodic Maps and the Smith Theory*, and the free involutions and the lens spaces are *Free Involutions and Lens Spaces*. The equivariant signature in its analytic form is *Hermitian Pairings and the Equivariant Signature*; the knot Floer and the $\rho$-invariants are *Floer Homology*. The equivariant homotopy theory of knots and the mapping class group of a knot complement are *Knot Theory* and *Low-Dimensional Topology*.

## Periodic Knots and their Quotients

**Definition.** A knot $K\subseteq S^3$ is **$n$-periodic** if there is an action of $\mathbb{Z}/n$ on $S^3$ by homeomorphisms preserving $K$ whose fixed set contains a circle **axis** $A$ disjoint from $K$, and such that the action on $S^3\setminus A$ has no other fixed points. The quotient of $S^3\setminus A$ by the action is again a three-sphere (the quotient of the solid torus is a solid torus), and the image of $K$ in the quotient is the **quotient knot** $\bar K$, which is a knot in $S^3$; the pair $(K,\bar K)$ with the integer $n$ is the **periodic knot datum**.

**Proposition (Smith theory constraints).** The fixed set of a nontrivial action of $\mathbb{Z}/p$ with $p$ prime on $S^3$ is a mod $p$ homology sphere of dimension at most three; for $p$ odd the fixed set is a circle, for $p = 2$ it is a circle, a two-sphere or two points. Consequently the periodic knot datum with axis a circle exists for every $n$, and the fixed set of the action generating the period is exactly the axis when the period is odd.

**Proof.** The statement is the Smith theory of *Periodic Maps and the Smith Theory*: the fixed set of a $\mathbb{Z}/p$ action on a mod $p$ homology sphere is a mod $p$ homology sphere, and on $S^3$ the possibilities for $p$ odd reduce to a circle because a two-dimensional mod $p$ homology sphere fixed set would separate and force a contradiction with the complementary free action; the case $p=2$ adds the two-sphere of a reflection and the two-point fixed set. The construction of the periodic data for the axis case is the periodic map fixing the axis.

**Remark (the cases and the terminology).** The case in which the fixed set is a circle disjoint from $K$ is the **cyclic** or **classical periodic** case treated here. The case in which the fixed set meets $K$, or is a two-sphere, gives the **strongly invertible** and the **amphichiral** symmetries of *Amphichiral Knots and the Orientation-Reversing Involution* and *Knot Theory*; the general treatment of the symmetries of a knot, including the periodic ones with the axis meeting the knot, is *Knot Theory* and *Low-Dimensional Topology*.

**Proposition (the branched cover and the quotient).** The $n$-fold cyclic branched cover $\Sigma_n(S^3,K)$ carries an action of $\mathbb{Z}/n$ with quotient $S^3$ branched over $\bar K$, and the deck transformation of the cover commutes with the action; the double branched cover $\Sigma_2(S^3,K)$ of the periodic knot is an $n$-fold cover of the double branched cover of the quotient knot, with deck group $\mathbb{Z}/n$.

**Proof.** The branched cover is constructed from the action on $S^3\setminus K$ by the representation of $\pi_1$ onto $\mathbb{Z}/n$; the symmetry of the pair descends to an action on the cover, and the compositions of the covering projections give the stated quotient maps and deck groups.

## The Equivariant Seifert Form

**Definition.** An **equivariant Seifert surface** for the periodic knot $(K,n)$ is a Seifert surface $\Sigma$ for $K$ invariant under the action, chosen so that the action restricts to $\Sigma$ with the same period; its invariant part $\Sigma_0 = \Sigma^{\mathbb{Z}/n}$ is a Seifert surface for the quotient knot $\bar K$ (with possibly several components before the quotient), and $\Sigma$ is a cyclic cover of $\Sigma_0$ branched at the fixed points of the action on $\Sigma$.

**Proposition (the equivariant Seifert form).** The Seifert form of an equivariant Seifert surface,
$$
V : H_1(\Sigma;\mathbb{Z})\times H_1(\Sigma;\mathbb{Z})\longrightarrow \mathbb{Z}, \qquad V(x,y) = \mathrm{lk}(x,y^+) ,
$$
is equivariant for the action of $\mathbb{Z}/n$ in the sense that $V(gx,gy) = V(x,y)$, and it extends to a sesquilinear form over the group ring
$$
V^{\mathbb{Z}/n} : H_1(\Sigma;\mathbb{Z})\times H_1(\Sigma;\mathbb{Z})\longrightarrow \mathbb{Z}[\mathbb{Z}/n], \qquad V^{\mathbb{Z}/n}(x,y) = \sum_{g\in\mathbb{Z}/n} V(x,gy)\,g ,
$$
whose class in the Witt group of $\mathbb{Z}[\mathbb{Z}/n]$ with the involution $g\mapsto g^{-1}$ is an invariant of the periodic knot datum. The invariant part $\Sigma_0$ gives the ordinary Seifert form of the quotient knot as the "trivial character" component of $V^{\mathbb{Z}/n}$.

**Proof.** The linking form is invariant under the action because the action preserves the orientations and the linking numbers, and the sum over the group is the standard passage from an equivariant form to a form over the group ring. The decomposition of $\mathbb{Z}[\mathbb{Z}/n]\otimes\mathbb{C}$ into characters of $\mathbb{Z}/n$ decomposes the form into the twisted forms $V_{\zeta}$ of the next section, of which the component at the trivial character is the Seifert form of the quotient.

**Remark (the equivariant Witt class and the surgery obstruction).** The class of the equivariant Seifert form in the Witt group of $\mathbb{Z}[\mathbb{Z}/n]$ is the algebraic home of the periodicity invariants: it is the analogue, for the periodic knot, of the Seifert form as a concordance invariant, and it is the algebraic input to the equivariant surgery of the knot complement. The Wall group $L_{2k+1}(\mathbb{Z}[\mathbb{Z}/n])$ and the equivariant surgery obstruction of *Involutions on Manifolds and Equivariant Surgery* are the framework; the algebraic computations are in the literature cited below.

## The Equivariant Alexander Module and Signature

**Definition.** Let $\zeta$ be a complex $n$-th root of unity and let $\mathbb{C}_\zeta$ be the complex numbers with the action of $\mathbb{Z}/n$ by $\zeta$. The **twisted homology** of the knot complement is
$$
H_*^{\zeta}(S^3\setminus K;\mathbb{C}) = H_*\bigl((S^3\setminus K)\times_{\mathbb{Z}/n}\mathbb{C}_\zeta\bigr) = H_*(S^3\setminus K;\mathbb{C}_\zeta) ,
$$
the homology with coefficients in the "twisted" module $\mathbb{C}_\zeta$, a module over $\mathbb{Z}[t^{\pm1}]$ through the action of the meridian.

**Proposition (decomposition of the equivariant Alexander module).** The equivariant Alexander module $H_1(S^3\setminus K;\mathbb{Z}[\mathbb{Z}/n][t^{\pm1}])$ decomposes, after tensoring with $\mathbb{C}$, into the sum of the twisted modules
$$
H_1(S^3\setminus K;\mathbb{C})_{\mathbb{Z}/n}\otimes\mathbb{C} = \bigoplus_{\zeta^n=1} H_1^{\zeta}(S^3\setminus K;\mathbb{C}),
$$
the component at the trivial character being the ordinary Alexander module of $K$ and the component at $\zeta\neq1$ being the twisted module. The twisted **equivariant Alexander polynomial** $\Delta_K(t,\zeta)$ generates the order ideal of the twisted module, and it satisfies the symmetry and the congruence of the periodic knot theory; at $\zeta = 1$ it is the Alexander polynomial of $K$, and the module of the quotient knot appears in the trivial-character and in the linking-form components.

**Proof sketch.** The group ring $\mathbb{Z}[\mathbb{Z}/n]$ becomes a sum of copies of $\mathbb{C}$ indexed by the characters after tensoring with $\mathbb{C}$; the module structure of the Alexander module over $\mathbb{Z}[\mathbb{Z}/n][t^{\pm1}]$ therefore decomposes into the twisted pieces, and the order ideals give the twisted polynomials. The detailed relation between $\Delta_K(t,\zeta)$ and the Alexander polynomial of the quotient knot $\bar K$ is the content of Murasugi's congruence; the statement and its applications are in the sources, and the present article records the module structure.

**Definition (the equivariant signature).** For each $n$-th root of unity $\zeta$ the **equivariant signature** $\sigma(K,\zeta)$ is the signature of the Hermitian form obtained from the equivariant Seifert form by the character $\zeta$,
$$
\sigma(K,\zeta) = \operatorname{sign}\bigl((1-\zeta)^{-1}V_{\zeta} + ((1-\zeta)^{-1}V_{\zeta})^{*}\bigr),
$$
the twisted analogue of the Tristram–Levine signature; for $\zeta = -1$ it is the ordinary signature.

**Theorem (the equivariant signature is an invariant of the periodic datum).** The numbers $\sigma(K,\zeta)$ depend only on the periodic knot datum $(K,n)$ and the character, are constant on the components of the complement of the unit circle of the $\zeta$-variable, and satisfy the equivariant sum formulas
$$
\sum_{\zeta^n = 1}\sigma(K,\zeta) = \sigma(K,\bar{\ }) + \text{(contributions of the axis)},
$$
so that the periodicity imposes congruences on the signatures of $K$ and of the quotient $\bar K$; these are the classical "periodic" signature conditions.

**Proof sketch.** The Hermitian form is the twisted symmetrisation of the Seifert form; its signature is constant as long as $\zeta$ stays in a component of $\mathbb{C}\setminus(\text{roots of the Alexander polynomial})$, by the continuity of the eigenvalues, and the sum formula is the decomposition of the equivariant form into characters. The precise formulas for the axis contributions and the resulting congruences are in the literature.

## Classical Periodic Invariants

**Theorem (Murasugi's congruence, statement).** Let $K$ be $n$-periodic with quotient knot $\bar K$ and axis $A$. Then the Alexander polynomials satisfy a congruence relating $\Delta_K$ to the twisted polynomials of the characters and to the Alexander polynomials of $\bar K$ and of the axis; in particular the quotient knot's Alexander polynomial is recovered from the characters, and the congruence is the classical necessary condition for an $n$-periodic knot with a given quotient.

**Proof sketch.** The congruence is read off the decomposition of the equivariant Alexander module and the identification of the trivial character component with the module of the quotient; the axis contributes the linking form, and its Alexander polynomial is the "twisted" factor. The full statement, with the conventions for the variable and the root of unity, is Murasugi's theorem.

**Theorem (the equivariant genus inequality, statement).** Let $K$ be $n$-periodic with quotient knot $\bar K$. Then
$$
g(K)\;\geq\; n\,g(\bar K),
$$
where $g$ is the Seifert genus, and more generally the equivariant minimal genus satisfies the corresponding inequality with the axis contribution; the inequality is sharp for the torus knots.

**Proof sketch.** An equivariant minimal Seifert surface covers the quotient surface with degree $n$ and with the fixed points of the action as the branch points; counting the Euler characteristics gives the inequality. The equivalence of the minimal equivariant genus and the ordinary minimal genus, and the resulting inequality, are the equivariant genus theorem; the sharpness for the torus knots is the example below.

**Remark (detection and non-detection).** The classical polynomial and signature invariants detect periodicity only partially: there are knots with all the classical periodic congruences satisfied that are not periodic, and there are periodic knots not detected by the Alexander polynomial alone; the finer detection is by the equivariant Seifert form, by the twisted Alexander modules and, in the modern theory, by the knot Floer homology with its equivariant structure. The latter is *Floer Homology*.

## Examples

**Example (the torus knots are periodic).** The torus knot $T(p,q)$ is invariant under the periodic map of $S^3$ about the core of the torus with period $p$ (and with period $q$), with the axis disjoint from the knot near the core; the quotient knot is the torus knot $T(1,q)$, that is, the unknot, and more generally the quotient of the $p$-periodic structure is the unknot with the axis winding $q$ times. The genus of $T(p,q)$ is $(p-1)(q-1)/2$, and the equivariant genus inequality is an equality for these knots; the example is the standard one for the periodicity of a knot.

**Example (the trefoil is $3$-periodic).** The trefoil $T(2,3)$ is $3$-periodic with the quotient knot the unknot; its Alexander polynomial $\Delta(t) = t-1+t^{-1}$ satisfies the Murasugi congruence for $n=3$, and the periodic structure is visible in the standard diagram with three-fold symmetry. The trefoil is also $2$-periodic in the strongly invertible sense, with the axis meeting the knot; the two structures are different and illustrate the dependence of the periodicity on the fixed set.

**Example (the connected sum and the divisor).** If $K_1$ is $n$-periodic and $K_2$ is arbitrary, the connected sum $K_1\#K_2$ is not periodic in general, because the symmetry of the first summand does not extend across the summing sphere; and the connected sum of two $n$-periodic knots with compatible axes is $n$-periodic. The additivity and the obstruction to it are *Knot Theory* and the equivariant theory here.

**Example (the double of a knot).** The $n$-fold cyclic branched cover of $S^3$ branched over a knot, with its deck transformation, is the standard source of periodic knots: a knot in the quotient covered by a knot in the cover is periodic with the deck group as its period. The construction is the double branched cover of *Amphichiral Knots and the Orientation-Reversing Involution*, read with $\mathbb{Z}/n$ in place of $\mathbb{Z}/2$, and the free case is *Free Involutions and Lens Spaces*.

## Summary

A knot is $n$-periodic when a cyclic group of order $n$ acts on the three-sphere preserving it with an axis disjoint from the knot; the quotient is a knot $\bar K$ in the quotient sphere, and the threefold of the knot, its quotient and the axis is the periodic datum. Smith theory forces the fixed set of a prime-order action on $S^3$ to be a circle for odd periods, so the periodic datum exists for every period, and the branched covers of $K$ are cyclic covers of those of $\bar K$. The equivariant invariants are assembled from an equivariant Seifert surface: the equivariant Seifert form takes values in the group ring $\mathbb{Z}[\mathbb{Z}/n]$ and its Witt class is the algebraic invariant of the periodic datum, its character decomposition gives the twisted Alexander modules with their twisted polynomials and the twisted signatures $\sigma(K,\zeta)$, and the trivial character recovers the quotient knot. The classical consequences are Murasugi's congruence for the Alexander polynomial, the equivariant signature congruences with their axis contributions, and the equivariant genus inequality $g(K)\geq n\,g(\bar K)$, sharp for the torus knots; the conditions are necessary and the finer detection is by the equivariant Seifert form and the Floer-theoretic refinements. The torus knots and the trefoil are the standard examples.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $n$, $\mathbb{Z}/n$ | the period and the cyclic group acting on $S^3$ |
| $A$ | the axis, the fixed circle of the action, disjoint from $K$ |
| $K$, $\bar K$ | the periodic knot and its quotient knot |
| $\Sigma$, $\Sigma_0 = \Sigma^{\mathbb{Z}/n}$ | an equivariant Seifert surface and its invariant part |
| $V^{\mathbb{Z}/n}(x,y) = \sum_g V(x,gy)g \in \mathbb{Z}[\mathbb{Z}/n]$ | the equivariant Seifert form |
| $\zeta$, $\Delta_K(t,\zeta)$ | an $n$-th root of unity and the twisted Alexander polynomial |
| $H_1^{\zeta}(S^3\setminus K;\mathbb{C})$ | the twisted homology, a summand of the equivariant Alexander module |
| $\sigma(K,\zeta)$ | the equivariant signature; $\sigma(K,-1)$ is the ordinary signature |
| $g(K)\geq n\,g(\bar K)$ | the equivariant genus inequality |
| $\Sigma_2(S^3,K)$, $\Sigma_n(S^3,K)$ | the double and the $n$-fold cyclic branched covers |
| $T(p,q)$ | the torus knot, $p$- and $q$-periodic with unknot quotient |

## Further Reading

- Kunio Murasugi, "On Periodic Knots", *Commentarii Mathematici Helvetici* 46 (1971), 162–174, for the congruence of the Alexander polynomials of a periodic knot and its quotient.
- Kunio Murasugi, "On Periodic Knots II", *Journal of the Mathematical Society of Japan* 25 (1973), 405–416, for the signatures and the periodicity conditions.
- Richard Hartley, "The Conway Potential Function for Links", *Commentarii Mathematici Helvetici* 58 (1983), 365–378, for the equivariant and twisted invariants of periodic knots.
- Charles Livingston and Paul Kirk, "Twisted Alexander Invariants, Reidemeister Torsion, and Casson–Gordon Invariants", *Topology* 38 (1999), 635–661, for the twisted Alexander polynomials and their use.
- Allan Edmonds, "Least Area Seifert Surfaces and Periodic Maps", *Topology* 18 (1979), 17–25, for the equivariant genus inequality and the symmetric minimal surfaces.
- Akio Kawauchi, *A Survey of Knot Theory* (Birkhäuser, 1996), for the symmetries, the periodic knots and their classical invariants.
- Peter Ozsváth and Zoltán Szabó, "Knot Floer Homology and the Four-Ball Genus", *Annals of Mathematics* 159 (2004), 1159–1245, for the Floer-theoretic equivariant refinements, developed in *Floer Homology*.
