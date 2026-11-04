# __The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System__

## Introduction

A single bilinear product on a vector space carries two structures at once. Its symmetrisation $x \bullet y = \tfrac12(xy + yx)$ is commutative, and its antisymmetrisation $[x,y] = \tfrac12(xy - yx)$ is anticommutative. The corpus treats the two separately: the symmetric product is the subject of *Jordan Algebras* and of the *Symmetric Algebras* of this part, and the antisymmetric bracket is the subject of *Lie Algebras* and of the *Anti-symmetric Algebras*. This article records the observation — Liu Yu-Fen's, in the source of the biquaternion dirac construction — that for the specific product built from the four generators the two structures are *both* present and *compatible*, and that the ternary product they generate is a Jordan triple system.

The setting is the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$, read as a complex four-dimensional vector space $V = \mathbb{C}^4$ with a bilinear composition whose structure constants are the source's

$$
c_{\mu\nu\lambda} = \sum_\rho\bigl(t_{\mu\nu\lambda\rho} - i\varepsilon_{\mu\nu\lambda\rho}\bigr)k_\rho,
$$

where $L_{a}R_{b}\psi=a\psi b$ are the cells, $L_{e_\mu}R_{\vec e_{\nu(\mu)}}$ is the reference cell of the $\mu$-th coordinate, with $\nu(t)=x$ and $\nu(k)=y$ for $k=1,2,3$, and $L_{e_t}R_{\vec e_z}$ is the chirality cell, so that $t_{\mu\nu\lambda\rho} = \tfrac14\mathrm{tr}(L_{e_\mu}R_{\vec e_{\nu(\mu)}}L_{e_\nu}R_{\vec e_{\nu(\nu)}}L_{e_\lambda}R_{\vec e_{\nu(\lambda)}}L_{e_\rho}R_{\vec e_{\nu(\rho)}})$ and $\varepsilon_{\mu\nu\lambda\rho} = \tfrac14\mathrm{tr}(L_{e_t}R_{\vec e_z}L_{e_\mu}R_{\vec e_{\nu(\mu)}}L_{e_\nu}R_{\vec e_{\nu(\nu)}}L_{e_\lambda}R_{\vec e_{\nu(\lambda)}})$ are the traces of four and five reference cells, the unit phases of the cells cancelling in the trace, and $k_\mu$ is a neutral vector. The reference cells are the bare cells, of square $\pm1$; the physics articles of the relativistic quantum series use the scaled cells $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ and $-iL_{e_t}R_{\vec e_z}$, and every statement below is a statement about the bare cells, in which the $i$'s are absent by construction. No single letter stands for a reference cell: the cell is written as its two multipliers. The composition

$$
(G \star H)_\lambda = \sum_{\mu,\nu}G_\mu\, c_{\mu\lambda\nu} H_\nu
$$

is associative and has $k$ as its unit; it is the biquaternion product in a particular basis. The point of this article is what that product *is*, algebraically: one bilinear map, three structures.

## The Two Halves of One Product

### Definitions

For $G, H \in V$ put

$$
G \bullet H = \tfrac12\bigl(G \star H + H \star G\bigr),
\qquad
[G, H] = \tfrac12\bigl(G \star H - H \star G\bigr).
$$

Then $G \bullet H = H \bullet G$ and $[G,H] = -[H,G]$: the symmetrisation is commutative, the antisymmetrisation anticommutative. Both are bilinear, and either, together with the other, reconstructs the product: $G \star H = G \bullet H + [G, H]$. The two are therefore not two structures on $V$ but the two halves of one structure.

### The Lie Half

The antisymmetrisation satisfies the **Jacobi identity**

$$
[G,[H,K]] + [H,[K,G]] + [K,[G,H]] = 0,
$$

so $(V,[\cdot,\cdot])$ is a Lie algebra. Because the product that defines it is associative, this is the *commutator algebra* of an associative algebra: the Lie algebra associated to $M_2(\mathbb{C})$, namely $\mathfrak{gl}(2,\mathbb{C}) \cong \mathfrak{sl}(2,\mathbb{C}) \oplus \mathbb{C}$. The corpus's *Lie Algebras* and the biquaternion Lie algebra article record the general construction; here it is the first half of the source's decomposition, and it is the half that the neutral element $j$ (the spacelike unit) leans on, since the antisymmetric symbol $\varepsilon$ is what survives the antisymmetrisation.

### The Jordan Half

The symmetrisation satisfies the **Jordan identity**

$$
\boxed{\;G \bullet (H \bullet (G \bullet G)) = (G \bullet H) \bullet (G \bullet G)\;},
$$

so $(V, \bullet)$ is a Jordan algebra. Because the product is associative, this is the *special* Jordan algebra $M_2(\mathbb{C})^+$ — the symmetrisation of an associative algebra, which is the general source of special Jordan algebras, and which here is the corpus's $H_2(\mathbb{C})$ with the Hermitian part singled out. The corpus's *Jordan Algebras* and *Special and Exceptional Jordan Algebras* record the theory; the second half of the source's decomposition lands exactly there.

### The Compatibility

The two halves are not independent: the bracket is a *derivation* of the Jordan product,

$$
\boxed{\;[G, H \bullet K] = [G,H] \bullet K + H \bullet [G,K]\;},
$$

and the sum

$$
[G, H \bullet K] + [H, K \bullet G] + [K, G \bullet H] = 0
$$

vanishes identically. The first identity says the Lie algebra acts on the Jordan algebra by derivations; the second is the **fundamental identity** that the source names, the compatibility condition that makes the pair a *Lie–Jordan algebra* in the sense of the literature on the Kantor–Koecher construction. The three identities — Jacobi, Jordan, and this compatibility — are what the source's "revised and corrected" account of its algebra asserts; the correction it makes to its earlier formulation is exactly a sign, the sign of the $\varepsilon$ term in $c_{\mu\nu\lambda}$, without which the antisymmetric half fails Jacobi and the symmetric half fails Jordan.

## The Jordan Triple System

### The Ternary Product

The symmetrised product generates a *ternary* operation,

$$
\{G, H, K\} = (G \bullet H) \bullet K + (K \bullet H) \bullet G - (G \bullet K) \bullet H,
$$

which is the linearisation of the **quadratic representation** $U_G H = G \bullet (H \bullet G)$ of the Jordan algebra. Equivalently, and this is the form the source's construction makes natural, the ternary product of an associative algebra with an involution is

$$
\{G, H, K\} = (G \star H) \star K + (K \star H) \star G .
$$

Both forms are ternary operations on $V$, and both are symmetric in the outer two arguments, $\{G,H,K\} = \{K,H,G\}$.

### The Triple Identities

A **Jordan triple system** is a vector space with a ternary product that is linear in each argument, symmetric in the outer two, and satisfies the five-linear **Jordan triple identity**

$$
\boxed{\;\{x, y, \{u, v, w\}\}
= \{\{x,y,u\}, v, w\} - \{u, \{y,x,v\}, w\} + \{u, v, \{x,y,w\}\}\;}.
$$

Both ternary products above satisfy this identity. A Jordan triple system need not come from a Jordan algebra — the triple identity is weaker than the Jordan identity — so the ternary structure is the more general object, and the source's construction lands on it: the cubic form of the triality construction ($iA_\mu\Psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\,iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\Psi$, in the companion physics articles) is the ternary product read with the vector space as the third factor. This is why the source presents its algebra as an order-$\ell$ *ding*, of which the order-three part is the Jordan triple system.

### The Block Structure

The four-dimensional carrier has one more piece of visible structure. In the trinomial basis the units $e_\mu = i\hat e_\mu$ are $2\times2$ *block* matrices: each unit is a $2\times2$ matrix of $2\times2$ blocks, and the blocks of the three spatial units close under multiplication into the quaternion group $Q_8$ modulo its centre. The source groups these blocks under the name **periodic matrices** $J_i$; the block form itself is what the algebra supplies, and it exhibits $\mathbb{B} \cong M_2(\mathbb{C})$ directly — the algebra is a $2\times2$ matrix algebra, its symmetric part is the special Jordan algebra, and its skew part is the Lie algebra. The verified content of the block structure is exactly the quaternion relations $\hat e_\mu^2 = -I$ and $\hat{\vec e}_x \hat{\vec e}_y = \hat{\vec e}_z$; the identification of the individual blocks with the source's $J_i$ is the source's, and the corpus records it as such.

## What Is Verified and What Is the Source's

- Jacobi for the antisymmetric half;
- the Jordan identity for the symmetric half;
- the derivation identity $[G, H\bullet K] = [G,H]\bullet K + H\bullet[G,K]$;
- the fundamental identity $[G,H\bullet K] + [H,K\bullet G] + [K,G\bullet H] = 0$;
- the symmetry $\{G,H,K\} = \{K,H,G\}$ and the five-linear Jordan triple identity, for both ternary forms;
- that the composition is associative with unit $k$, and that the blocks of $\vec e_x, \vec e_y, \vec e_z$ reproduce the quaternion relations.

**The source's**, transcribed and not independently derivable from the identities above: the naming of the block matrices $J_i$ and the claim that the "revised" account corrects an earlier formulation by a sign; the identification of the ternary product with the source's order-three ding; and the general definition of an order-$\ell$ ding. The identities themselves are the definitional ones for Lie, Jordan and Jordan-triple structures; what the source adds is the observation that the *same* product carries all three, and the explicit construction that shows it.

**A caution.** That Jacobi and Jordan hold is, for an associative algebra, automatic: the commutator of an associative algebra is always a Lie bracket and its symmetrisation always a Jordan algebra. The content of the article is therefore not the *holding* of the identities but the *identification* of the algebra: the structure constants $c_{\mu\nu\lambda}$ with the normed condition are those of $M_2(\mathbb{C})$, so the Lie half is $\mathfrak{gl}(2,\mathbb{C})$, the Jordan half is $M_2(\mathbb{C})^+$, and the triple system is the Jordan triple system of the same matrix algebra. The source's correction matters because a wrong sign in the $\varepsilon$ term produces a *different* product — one that is neither associative nor normed — and then none of the three structures is the standard one.

## Open Questions

1. **The Kantor–Koecher construction.** A Lie–Jordan algebra with a compatibility condition is the input to the Kantor–Koecher construction, which builds a Lie algebra (and hence a graded Lie algebra) from a Jordan algebra. Is the source's algebra a Kantor pair, and is the resulting Lie algebra $\mathfrak{sl}(2,\mathbb{C})$ itself, or a larger one?

2. **The order-three structure.** The algebra carries an order-three automorphism (the triality of the companion physics articles). Does that automorphism act on the Lie half, the Jordan half and the triple system in the way the $S_3$ outer automorphism acts on the three representations of $\mathrm{Spin}(8)$? The triple structure — one Lie algebra, one Jordan algebra, one Jordan triple — is suggestive, and the question is whether the suggestion is a theorem.

3. **The exceptional case.** The biquaternion algebra is 4-dimensional, and its Jordan half is special. The first exceptional Jordan algebra, the Albert algebra, needs 27 dimensions and the octonions. Does the order-$\ell$ ding construction have an octonionic lifting, and does the lifting land on the exceptional structures of *Special and Exceptional Jordan Algebras*?

4. **The grading.** The compatibility identity is the germ of a $\mathbb{Z}/2$-graded Lie algebra structure, with the bracket as the odd part acting on the even part. The corpus's *Superalgebras and Graded Structures* treats the $\mathbb{Z}/2$ grading directly; whether the source's Lie–Jordan pair is best read as a graded Lie algebra is open.

These questions are open.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}R_{\vec e_x},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5[\mathbb{M}_-]$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5[\mathbb{M}_-]$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5[\mathbb{M}_-]^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5[\mathbb{M}_-]\}=0,
$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu[\mathbb{M}_-]=-\varepsilon_\mu\gamma_\mu[\mathbb{M}_-]$, so that $\sum_\mu\gamma^\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-4I_4$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-]$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$.
## Summary

A bilinear product on a vector space has two halves: its symmetrisation $G\bullet H = \tfrac12(G\star H + H\star G)$ and its antisymmetrisation $[G,H] = \tfrac12(G\star H - H\star G)$. For the product built from the four generators, $c_{\mu\nu\lambda} = \sum_\rho(t_{\mu\nu\lambda\rho} - i\varepsilon_{\mu\nu\lambda\rho})k_\rho$, the antisymmetric half satisfies the Jacobi identity and is the Lie algebra $\mathfrak{gl}(2,\mathbb{C})$, and the symmetric half satisfies the Jordan identity and is the special Jordan algebra $M_2(\mathbb{C})^+$. The two halves are compatible: the bracket is a derivation of the Jordan product, $[G,H\bullet K] = [G,H]\bullet K + H\bullet[G,K]$, and the fundamental identity $[G,H\bullet K] + [H,K\bullet G] + [K,G\bullet H] = 0$ holds. The symmetrised product generates a ternary operation $\{G,H,K\} = (G\bullet H)\bullet K + (K\bullet H)\bullet G - (G\bullet K)\bullet H$, symmetric in its outer arguments and satisfying the five-linear Jordan triple identity; the source's order-three ding is this triple system. The block structure of the units $e_\mu$ exhibits the matrix algebra directly, with the four blocks of each unit being the source's periodic matrices $J_i$.

The identities Jacobi, Jordan, the derivation identity, the fundamental identity and the Jordan triple identity are all verified. The content of the construction is the identification: one product, the structure constants of $M_2(\mathbb{C})$, carries three compatible algebraic structures at once.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V = \mathbb{C}^4$ | Carrier of the algebra, $\mathbb{B} \cong M_2(\mathbb{C})$ |
| $G, H, K$ | Elements of $V$ |
| $G \star H$ | The composition, $(G\star H)_\lambda = \sum_{\mu,\nu}G_\mu c_{\mu\lambda\nu}H_\nu$ |
| $c_{\mu\nu\lambda} = \sum_\rho(t_{\mu\nu\lambda\rho} - i\varepsilon_{\mu\nu\lambda\rho})k_\rho$ | Structure constants |
| $t_{\mu\nu\lambda\rho} = \tfrac14\mathrm{tr}(L_{e_\mu}R_{\vec e_{\nu(\mu)}}L_{e_\nu}R_{\vec e_{\nu(\nu)}}L_{e_\lambda}R_{\vec e_{\nu(\lambda)}}L_{e_\rho}R_{\vec e_{\nu(\rho)}})$ | Symmetric trace of four reference cells |
| $\varepsilon_{\mu\nu\lambda\rho} = \tfrac14\mathrm{tr}(L_{e_t}R_{\vec e_z}L_{e_\mu}R_{\vec e_{\nu(\mu)}}L_{e_\nu}R_{\vec e_{\nu(\nu)}}L_{e_\lambda}R_{\vec e_{\nu(\lambda)}})$ | Totally antisymmetric symbol, the trace of five reference cells |
| $L_{e_\mu}R_{\vec e_{\nu(\mu)}}$, $L_{e_t}R_{\vec e_z}$ | The reference cells of the four coordinates and of the chirality, in the units $e_t,\vec e_x,\vec e_y,\vec e_z$ of $\mathbb{B}$; $L_{a}R_{b}\psi=a\psi b$, and $\nu(t)=x$, $\nu(k)=y$ |
| $k_\mu$ | Neutral vector, the unit of the composition |
| $G \bullet H = \tfrac12(G\star H + H\star G)$ | Jordan (symmetric) product |
| $[G,H] = \tfrac12(G\star H - H\star G)$ | Lie (antisymmetric) bracket |
| $\{G,H,K\}$ | Ternary (Jordan triple) product |
| $e_\mu = i\hat e_\mu$ | Units of the trinomial basis, $\hat e_\mu^2 = -I$ |
| $J_i$ | The source's name for the four $2\times2$ blocks of the units |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](../articles_physics/why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Liu Yu-Fen, "Triality, Biquaternion and Vector Representation of the Dirac Equation," arXiv:math-ph/0109008 (2001), §1 and §2, for the structure constants $c_{\mu\nu\lambda}$, the normed condition, the Lie and Jordan halves, the fundamental identity, the Jordan triple system, and the four $2\times2$ periodic matrices.
- Liu Yu-Fen, "Triality and Dual Equivalence Between Dirac Field and Topologically Massive Gauge Field," arXiv:hep-th/0602275 (2006), for the order-$\ell$ ding and the ternary structure.
- N. Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society Colloquium Publications 39, Providence, 1968), for Jordan algebras, their triple systems, and the quadratic representation.
- K. McCrimmon, *A Taste of Jordan Algebras* (Universitext, Springer, New York, 2004), for the Jordan triple identities and the classification of special and exceptional Jordan algebras.
- O. Loos, *Jordan Pairs* (Lecture Notes in Mathematics 460, Springer, Berlin, 1975), for Jordan triples, Jordan pairs and the Kantor–Koecher construction.
- M. Koecher, "Imbedding of Jordan algebras into Lie algebras I, II," *American Journal of Mathematics* **89** (1967) 787–816 and **90** (1968) 476–510, for the Kantor–Koecher construction.
- The companion corpus articles: [Jordan Algebras](jordan-algebras.html), [Special and Exceptional Jordan Algebras](special-and-exceptional-jordan-algebras.html), *Lie Algebras*, [Automorphisms and Derivations of Algebras](automorphisms-and-derivations-of-algebras.html), [Superalgebras and Graded Structures](superalgebras-and-graded-structures.html), and [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html).
