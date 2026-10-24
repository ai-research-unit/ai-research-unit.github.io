# __Biquaternion Representations and the Lorentz Group__

## Introduction

The group of units of the biquaternion algebra is $GL_2(\mathbb{C})$ through the matrix model, and the identity component $SO^+(1,3)$ of the Lorentz group is its norm-one subgroup modulo $\{\pm e_t\}$. This article reads the representations of the two groups: the algebraic representations of the unit group, the finite-dimensional representations of the Lorentz group, the defining representation with its two Weyl spinors, the tensor products and the Clebsch–Gordan rule, and the unitary representations with the principal series. The groups themselves, their double covers and the sandwich action are *Biquaternion Rotations and Lorentz Transformations*; the matrix model is *Biquaternion Objects and Their Matrix Correspondences*; the simple module is *Modules over the Biquaternion Algebra*; the Clifford module and the Weyl spinors are *Spin Representations and Clifford Modules with Inner Conjugation*; the compact unitary group is *The Unitary Group of the Biquaternion Algebra*; the Lie algebra is *Symmetric and Antisymmetric Decomposition of the Four General Products*; and the induced representations are *Induced Representations of Locally Compact Groups*. Nothing of those articles is reproved here.

The article is the representation-theoretic companion of the Geometry group. It owns the highest-weight classification for $GL_2(\mathbb{C})$, the classification $(m,n)$ of the finite-dimensional Lorentz representations, the identification of the Weyl and Dirac spinors, the Clebsch–Gordan decomposition and the principal series. The geometric action of the same groups on the algebra and on the quadric remains in the Geometry articles.

## The Group of Units

The group of units is $\mathbb{B}^{\times} = \{\tilde{Q} : \langle\tilde{Q}\rangle_{\natural} \neq 0\}$, which under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ is the group of invertible matrices, since the biquaternion norm is the determinant (*Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*):

$$
\mathbb{B}^{\times} \cong GL_2(\mathbb{C}),
$$

a connected non-compact complex Lie group of complex dimension $4$ and real dimension $8$, with centre $\mathbb{C}^{\times}$. The unit-norm subgroup is $\mathbb{B}^{\times}_1 \cong SL(2,\mathbb{C})$, of complex dimension $3$ and real dimension $6$, the double cover of the proper orthochronous Lorentz group (*Biquaternion Rotations and Lorentz Transformations*). The unitary biquaternions $\tilde{Q}^{*}\tilde{Q} = e_t$ form $\mathrm{U}(2)$, the maximal compact subgroup of $\mathbb{B}^{\times}$ (*The Unitary Group of the Biquaternion Algebra*), and the unit quaternions form $SU(2) = \mathbb{B}^{\times}_1 \cap \mathrm{U}(2)$, the maximal compact subgroup of $SL(2,\mathbb{C})$ and the double cover of $SO(3)$.

## Representations of the Group of Units

As a reductive group, $GL_2(\mathbb{C})$ has finite-dimensional algebraic (rational) representations parameterised by highest weights $(\lambda_1, \lambda_2) \in \mathbb{Z}^2$ with $\lambda_1 \geq \lambda_2$; the irreducible one is $\operatorname{Sym}^{\lambda_1 - \lambda_2}(\mathbb{C}^2) \otimes (\det)^{\lambda_2}$, of dimension $\lambda_1 - \lambda_2 + 1$, with central character $A \mapsto A^{\lambda_1 + \lambda_2}$. Restriction to $SL(2,\mathbb{C})$ forgets the determinant twist, leaving the highest weight $2j = \lambda_1 - \lambda_2 \geq 0$, that is, the irreducible $V_j$ below with spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$.

## Finite-Dimensional Representations of the Lorentz Group

Let $G = SL(2,\mathbb{C})$, with real Lie algebra the traceless $2\times2$ complex matrices (*Symmetric and Antisymmetric Decomposition of the Four General Products*). Its complexification is a sum of two copies of the special linear algebra, the complexified Lorentz algebra:

$$
\mathrm{so}(1,3)\otimes_{\mathbb{R}}\mathbb{C} \cong \mathrm{sl}(2,\mathbb{C}) \oplus \mathrm{sl}(2,\mathbb{C}),
$$

the two summands corresponding to the self-dual and anti-self-dual parts. Every finite-dimensional smooth complex representation of $G$ is completely reducible, and its irreducible summands are the outer tensor products $(m,n) = V_m \boxtimes V_n$ with $m, n \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$, where $V_j$ denotes the irreducible $\mathrm{SU}(2)$-module of dimension $2j+1$, equivalently the $\mathrm{SL}(2,\mathbb{C})$-module $\operatorname{Sym}^{2j}(\mathbb{C}^2)$ of highest weight $2j$; thus $\dim_{\mathbb{C}}(m,n) = (2m+1)(2n+1)$. The defining representation is $(\tfrac{1}{2}, 0)$ and its complex conjugate is $(0, \tfrac{1}{2})$.

**Polynomial representations.** Relative to a Cartan subalgebra spanned by $h = \operatorname{diag}(1,-1)$, the irreducible $SL(2,\mathbb{C})$-modules are the symmetric powers $V_j \cong \operatorname{Sym}^{2j}(\mathbb{C}^2)$, with spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$, highest weight $2j$ and dimension $2j+1$. These are exactly the **polynomial** (equivalently holomorphic, equivalently algebraic) finite-dimensional representations of the complex group $G$: their matrix entries are polynomial functions of the entries of $g \in G$, and every finite-dimensional holomorphic representation of $G$ is a direct sum of the $V_j$, hence is parameterised by its highest weight $2j$, that is, by its spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$. Not every continuous finite-dimensional representation is polynomial: the complex conjugates of the $V_j$ are antiholomorphic and belong to the $(0, j)$ family.

**The unitary trick.** Restriction to the maximal compact subgroup $SU(2)$ is an equivalence of categories

$$
\left\{\text{f.d. polynomial representations of } SL(2,\mathbb{C})\right\} \simeq \left\{\text{f.d. unitary representations of } SU(2)\right\},
$$

so the finite-dimensional polynomial representations of $SL(2,\mathbb{C})$ are obtained from those of $SU(2)$ by complexifying the Lie algebra and exponentiating, and both are parameterised by the same highest weights $2j$, $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$. What complexification does not preserve is unitarity, a point taken up in §*Unitary Representations*.

## The Defining Representation and the Weyl Spinors

The defining representation of $SL(2,\mathbb{C})$ is $V_{1/2} = \mathbb{C}^2$, the polynomial representation of highest weight $1$. It is the same space that appears in *Modules over the Biquaternion Algebra* as the unique simple module of the algebra $\mathbb{B}$, and the isomorphism $\mathbb{B} \cong \operatorname{End}_{\mathbb{C}}(V_{1/2})$ is the content of the matrix realization (*Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*): choosing a basis of $V_{1/2}$ writes each element of the algebra as a $2 \times 2$ matrix, and the choice of basis is the only freedom in doing so. Under the Lorentz group the defining representation and its conjugate are the two **Weyl spinors**: $V_{1/2} = (\tfrac{1}{2}, 0)$ is the left-handed one and $\overline{V_{1/2}} = (0, \tfrac{1}{2})$ is the right-handed one; they are not isomorphic as complex representations, and parity exchanges them. Their direct sum is the **Dirac spinor**

$$
\Delta = V_{1/2} \oplus \overline{V_{1/2}} = (\tfrac{1}{2},0) \oplus (0,\tfrac{1}{2}), \qquad \dim_{\mathbb{C}} \Delta = 4,
$$

and their tensor product is the **vector representation** $(\tfrac{1}{2}, \tfrac{1}{2}) = V_{1/2} \otimes \overline{V_{1/2}}$, of complex dimension $4$, whose real form is the Lorentz action on the four-dimensional vector space (*The Four-Vector Element Representation of Biquaternions*). The adjoint representation of the Lorentz algebra is $(1,0) \oplus (0,1)$, of dimension $3 + 3$.

Two dualities must be distinguished. The defining module is **self-dual** as a representation of $SL(2,\mathbb{C})$: since $\det = 1$, the alternating form $\varepsilon(u,v) = u_x v_2 - u_y v_1$ is invariant and identifies $V_{1/2}^{*}$ with $V_{1/2}$, so $V_{1/2}^{*} \cong V_{1/2}$. The **conjugate** $\overline{V_{1/2}}$, by contrast, is not isomorphic to $V_{1/2}$; it is the other chirality. Finally, since $-e_t$ acts as $-1$ on $V_{1/2}$, the defining representation, and every $(m,n)$ with $m+n$ half-integral, does not descend to $SO^+(1,3)$. This is the representation-theoretic form of the statement that the Lorentz group itself has no two-dimensional spin representation: the spin representation is a representation of its double cover.

## Tensor Products and the Clebsch–Gordan Rule

Group representations tensor with the diagonal action $g \cdot (v \otimes w) = (gv) \otimes (gw)$. For the polynomial representations of $SL(2,\mathbb{C})$ the Clebsch–Gordan rule is

$$ V_j \otimes V_k \cong \bigoplus_{l=|j-k|}^{j+k} V_l, \qquad j, k \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}. $$

The tensor square of the spinor is the simplest nontrivial case:

$$
V_{1/2} \otimes V_{1/2} \cong \operatorname{Sym}^2 V_{1/2} \oplus \Lambda^2 V_{1/2} \cong V_1 \oplus V_0, \qquad \dim_{\mathbb{C}} V_1 = 3, \quad \dim_{\mathbb{C}} V_0 = 1.
$$

The summand $V_1$ is the symmetric square and is the adjoint representation of the special linear algebra, that is, the complexification of the adjoint representation of the compact algebra $\mathrm{su}(2) \cong \mathrm{so}(3)$; the summand $V_0 = \Lambda^2 V_{1/2} \cong \mathbb{C}$ is the **scalar**, spanned by the invariant alternating form $\varepsilon$. Thus the tensor square of the spinor splits as the complexified adjoint representation plus a scalar. This is the three-dimensional rotation algebra; the adjoint representation of the six-dimensional Lorentz algebra is instead $(1,0) \oplus (0,1)$.

For the two-parameter family the rule applies to each factor:

$$
\boxed{\;(m,n) \otimes (m',n') \cong \bigoplus_{k=0}^{\min(m,m')} \bigoplus_{k'=0}^{\min(n,n')} (m+m'-2k,\ n+n'-2k')\;}.
$$

For example, $(\tfrac{1}{2},\tfrac{1}{2}) \otimes (\tfrac{1}{2},\tfrac{1}{2}) \cong (0,0) \oplus (1,0) \oplus (0,1) \oplus (1,1)$, of dimension $1 + 3 + 3 + 9 = 16 = 4 \times 4$.

**Tensor powers of the defining representation.** Iterating the rule gives the complete decomposition of the $N$-fold tensor power of the spinor,

$$
V_{1/2}^{\otimes N} \cong \bigoplus_{k=0}^{\lfloor N/2 \rfloor} \left[ \binom{N}{k} - \binom{N}{k-1} \right] V_{N/2-k}, \qquad \binom{N}{-1} = 0,
$$

the multiplicity of $V_{N/2-k}$ being the ballot (Catalan-triangle) number $\binom{N}{k} - \binom{N}{k-1}$. For example $V_{1/2}^{\otimes 2} \cong V_1 \oplus V_0$ and $V_{1/2}^{\otimes 3} \cong V_{3/2} \oplus 2V_{1/2}$. Since every finite-dimensional polynomial representation is completely reducible, the composition factors of a tensor power are exactly its direct summands, with these multiplicities.

## Unitary Representations

A representation $\rho$ on $W$ is **unitary** if $W$ carries an invariant positive-definite Hermitian form $\langle \cdot, \cdot \rangle$. On $V_{1/2} = \mathbb{C}^2$ the standard form $\langle u,v \rangle = u_x^{*}v_1 + u_y^{*}v_2$ is invariant under $SU(2)$, so $V_{1/2}$ is unitary for the compact form $SU(2)$. It is **not** unitary for $SL(2,\mathbb{C})$: the non-compact one-parameter subgroups of hyperbolic rotations do not preserve it. More generally a non-compact simple Lie group has no nontrivial finite-dimensional unitary representation, since the image would lie in a compact group; hence only the trivial representation is finite-dimensional and unitary for $SL(2,\mathbb{C})$, and the defining representation is not unitarisable for the complex group. Unitarity of the compact form $SU(2)$, not of $SL(2,\mathbb{C})$, is what complexification preserves.

**The principal series.** The infinite-dimensional unitary representations are built by induction (*Induced Representations of Locally Compact Groups*). Let $P$ be the Borel subgroup of upper triangular matrices, with $P = MAN$,

$$
M = \{\operatorname{diag}(u,u^{-1}) : |u| = 1\} \cong \mathrm{U}(1), \qquad A = \{\operatorname{diag}(\exp(t/2), \exp(-t/2)) : t \in \mathbb{R}\},
$$

and $N$ the upper unitriangular matrices. For $m \in \mathbb{Z}$ and $\nu \in \mathbb{R}$ define a character of $P$ by $\chi_{m,\nu}(man) = u^{m} \exp((i\nu+\tfrac12)t)$; the factor $\exp(t/2)$ is the square root of the modulus of $P$, and the **principal series** representation is the unitarily induced representation

$$
\pi_{m,\nu} = \operatorname{Ind}_{P}^{G}(\chi_{m,\nu}),
$$

realised on $L^2(G/P) = L^2(S^2)$ in the case $m = 0$, where $G/P \cong SU(2)/\mathrm{U}(1) \cong S^2$, and on the sections of the associated line bundle in general. Each $\pi_{m,\nu}$ is unitary by construction; it is irreducible for generic parameters, and for $\nu \in \mathbb{R}$ it is tempered. The parameter $m$ is discrete and $\nu$ is continuous. The principal series is not the whole unitary dual: there are also the **complementary series**, for which the continuous parameter is purely imaginary and bounded rather than real, and the trivial representation. The finite-dimensional polynomial representations are not unitary for $SL(2,\mathbb{C})$, except for the trivial representation $V_0$; only their restrictions to $SU(2)$ are unitary.

**The unitary dual is not the complexification of the compact one.** The unitary dual of the maximal compact subgroup $SU(2)$ is discrete, the family $\{V_j\}_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}$. Passing to $SL(2,\mathbb{C})$ replaces the discrete highest-weight parameter by a continuous one; the unitary representations are the principal series, with parameter on the unitary axis, together with the complementary series and the trivial representation. The polynomial representations of $SU(2)$ complexify to representations of $SL(2,\mathbb{C})$ that are not unitary except for the trivial one, and the unitary dual of $SL(2,\mathbb{C})$ is continuous rather than the complexification of the discrete dual of $SU(2)$.

## Summary

The group of units is $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$, of real dimension $8$, with the unit-norm subgroup $\mathbb{B}^{\times}_1\cong SL(2,\mathbb{C})$, the maximal compact subgroups $\mathrm{U}(2)$ and $SU(2)$, and the finite-dimensional algebraic representations of $GL_2(\mathbb{C})$ parameterised by the highest weights $(\lambda_1,\lambda_2)$. The finite-dimensional representations of the Lorentz group are the outer products $(m,n)=V_m\boxtimes V_n$ of dimension $(2m+1)(2n+1)$, the polynomial ones being the symmetric powers $V_j$, which the unitary trick recovers from those of $SU(2)$ by complexifying the Lie algebra; the defining representation $V_{1/2}=\mathbb{C}^2$ is the unique simple module of the algebra $M_2(\mathbb{C})$. The defining representation and its conjugate are the two Weyl spinors $(\tfrac12,0)$ and $(0,\tfrac12)$, whose sum is the Dirac spinor and whose tensor product is the four-vector representation $(\tfrac12,\tfrac12)$; the adjoint representation of the Lorentz algebra is $(1,0)\oplus(0,1)$. Tensor products obey the Clebsch–Gordan rule, with the ballot numbers counting the composition factors of the tensor powers of the spinor. Unitarity is preserved by complexification only for the compact form $SU(2)$: the only finite-dimensional unitary representation of $SL(2,\mathbb{C})$ is the trivial one, and the infinite-dimensional unitary representations are the principal series, induced from characters of the Borel subgroup, together with the complementary series.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ | Group of units; real dimension $8$ |
| $\mathrm{U}(2)$ | Unitary biquaternions; maximal compact subgroup of $\mathbb{B}^{\times}$ |
| $(\lambda_1,\lambda_2)$ | Highest weight of an algebraic representation of $GL_2(\mathbb{C})$ |
| $\operatorname{Sym}^{\lambda_1-\lambda_2}(\mathbb{C}^2)\otimes(\det)^{\lambda_2}$ | The irreducible representation of $GL_2(\mathbb{C})$ of highest weight $(\lambda_1,\lambda_2)$ |
| $V_j$ | Irreducible representation of spin $j$, highest weight $2j$, dimension $2j+1$ |
| $(m,n)=V_m\boxtimes V_n$ | Finite-dimensional irreducible representation of the Lorentz group |
| $(\tfrac12,0)$, $(0,\tfrac12)$ | Left- and right-handed Weyl spinors |
| $(\tfrac12,\tfrac12)$ | Four-vector representation, $V_{1/2}\otimes\overline{V_{1/2}}$ |
| $V_{1/2}^{\otimes N}$ | Ballot-number decomposition of the tensor powers of the spinor |
| $\operatorname{Ind}_P^G(\chi_{m,\nu})$ | Principal series of $SL(2,\mathbb{C})$; $P=MAN$ the Borel subgroup |

## Further Reading

- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991).
- Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples* (Princeton University Press, 1986).
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed., 2015).
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636.
