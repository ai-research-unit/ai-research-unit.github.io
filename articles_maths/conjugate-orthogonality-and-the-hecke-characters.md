
# __Conjugate Orthogonality and the Hecke Characters__

## Introduction

A Hecke character of a number field $K$ is a continuous homomorphism from the idèle class group $C_K=I_K/K^\times$ to the circle group; for $K=\mathbb{Q}$ these are the Dirichlet characters, and in general they are the abelian characters of the arithmetic of $K$. The characters carrying an $L$-function, the orthogonality of the characters under the Hermitian pairing, and the way the conductor of a character enters the functional equation are the subject of this article. The orthogonality is a special case of the Peter–Weyl theory of a locally compact abelian group; the arithmetic content is the conductor-discriminant formula, and the analytic content is the Hecke $L$-function of *The Functional Equation and the Conjugate Symmetry of an L-Function*. The idèles are as in *Adeles and Ideles* and the class field theory as in *Class Field Theory*. Nothing here reads a distance as an object.

## Hecke Characters

### Definition

**Definition.** A **Hecke character** (or grossencharacter) of $K$ is a continuous homomorphism
$$
\chi:C_K=I_K/K^\times\to\mathbb{T},\qquad \mathbb{T}=\{z\in\mathbb{C}^\times:|z|=1\},
$$
equivalently a continuous homomorphism $\chi:I_K\to\mathbb{T}$ trivial on $K^\times$; a **quasi-character** is the same with values in $\mathbb{C}^\times$, and a **Dirichlet character** is the case $K=\mathbb{Q}$.

**Theorem.** The Hecke characters of $K$ form a group under pointwise multiplication, equal to the Pontryagin dual of the compact group $C_K^0$ of idèle classes of norm one times a discrete free part; each character factors as
$$
\chi=\prod_{v}\chi_v,
$$
a product of local characters $\chi_v:K_v^\times\to\mathbb{T}$ almost all of which are unramified, and a character is **unramified** at $v$ if $\chi_v$ is trivial on the units $\mathcal{O}_v^\times$.

**Proof.** The idèle class group is a product of the local multiplicative groups modulo the global units; a continuous character of a restricted product of locally compact abelian groups factors as a product of local characters with almost all factors unramified, by the theory of local compact abelian groups in *Abstract Harmonic Analysis*. The decomposition is the content of the idèle-class version of the Chinese remainder theorem.

### The local and global conductor

**Definition.** The **conductor** of a Hecke character is the ideal $\mathfrak{f}=\prod_v\mathfrak{p}_v^{a_v}$, where $a_v$ is the smallest integer such that $\chi_v$ is trivial on $1+\mathfrak{p}_v^{a_v}$, together with the archimedean part recording the order of vanishing of $\chi_v$ at the archimedean places; the character is **primitive** if it is not induced from a character of a smaller modulus.

**Theorem.** Every Hecke character is induced from a primitive character of its conductor, and the $L$-function $L(s,\chi)$ attached to a primitive character satisfies an Euler product and a functional equation with conductor $\mathfrak{f}$ and root number $W(\chi)$.

**Proof.** The induction of characters along the norm map of ideals is the standard construction; the Euler product is the multiplicativity of $\chi$, and the functional equation is the completed form of *The Functional Equation and the Conjugate Symmetry of an L-Function* with the conductor $\mathfrak{f}$ in place of $N$ and the root number in place of the sign.

## Conjugate Orthogonality

### The general theory

**Theorem (orthogonality).** Let $G$ be a compact abelian group with normalised Haar measure and dual $\widehat G$. Then
$$
\int_G\chi(g)\overline{\psi(g)}\,dg=\delta_{\chi\psi},\qquad \sum_{\chi\in\widehat G}\chi(g)\overline{\chi(h)}=\delta_{gh},
$$
where the second identity holds in the appropriate sense for the discrete dual and is the **second orthogonality** relation.

**Proof.** For $\chi\ne\psi$ the function $\chi\overline\psi$ is a nontrivial character and its integral vanishes by the invariance of the measure; for $\chi=\psi$ the integral is $1$. The second relation is the dual statement, in *Abstract Harmonic Analysis*.

**Definition.** The **conjugate orthogonality pairing** on the Hecke characters is the Hermitian form
$$
\langle\chi,\psi\rangle=\lim_{T\to\infty}\frac{1}{T}\int_{C_K^T}\chi\,\overline\psi\,d\mu ,
$$
the limit over the growing compact subgroups $C_K^T$ of the idèle class group; it is well defined on the characters of bounded conductor and it is $\delta_{\chi\psi}$.

**Theorem.** For Hecke characters of bounded conductor the conjugate orthogonality holds, and for the Dirichlet characters modulo $q$ it specialises to
$$
\frac{1}{\varphi(q)}\sum_{a\in(\mathbb{Z}/q)^\times}\chi(a)\overline{\psi(a)}=\delta_{\chi\psi}.
$$

**Proof.** The first statement is the orthogonality applied to the compact group $(C_K)_T$ and the passage to the limit; the specialisation is the identification of the Dirichlet characters with the characters of $(\mathbb{Z}/q)^\times$ and the orthogonality of the finite abelian group, in *Algebraic Number Theory*.

### The conductor-discriminant formula

**Theorem (conductor-discriminant formula).** For an abelian extension $L/K$ with Galois group $\operatorname{Gal}(L/K)$ and group of characters $\widehat G$,
$$
\mathfrak{d}_{L/K}=\prod_{\chi\in\widehat G}\mathfrak{f}(\chi),\qquad \operatorname{disc}(L/K)=\prod_{\chi}\operatorname{disc}(\chi),
$$
the discriminant of the extension being the product of the conductors of its characters.

**Proof.** The discriminant is the product of the local discriminants, and each local discriminant is the product of the local conductors of the characters of the local Galois group; summing over the places and using the orthogonality of the characters to distribute the factors gives the formula. This is the Führerdiskriminantenproduktformel of *Algebraic Number Theory*.

## Worked Examples

**Example (the Dirichlet characters).** For $q$ prime the group $(\mathbb{Z}/q)^\times$ is cyclic of order $q-1$ and the orthogonality is the discrete Fourier transform on a cyclic group; the Dirichlet characters are the Hecke characters of $\mathbb{Q}$ of conductor $q$.

**Example (a quadratic character).** The nontrivial character modulo $q$ of order $2$ is real, $\chi=\bar\chi$, its conductor is the discriminant of the quadratic field, and the conductor-discriminant formula gives the discriminant of $\mathbb{Q}(\sqrt{d})$ as the conductor of the character.

**Example (a grossencharacter of an imaginary quadratic field).** The Hecke characters of $\mathbb{Q}(i)$ of conductor $1$ are the powers of the character $z\mapsto z/|z|$ on the idèle class group; their $L$-functions are the Hecke $L$-functions of the Gaussian integers.

## Failure of the Degenerate Cases

The orthogonality fails in four degenerate configurations. First, for characters of unbounded conductor the limit in the pairing does not exist and the orthogonality must be read locally; the space of all Hecke characters is not compactly generated by a single orthonormal basis. Second, at the archimedean places the character is not of finite order, so the "conductor" has an archimedean component that is not an ideal; the orthogonality is then with respect to the archimedean unitary representation, not a finite sum. Third, the conjugate orthogonality for the quasi-characters with values in $\mathbb{C}^\times$ is not Hermitian and the pairing must be replaced by a sesquilinear one with a growth condition. Fourth, the nonabelian generalisation replaces the characters by the automorphic representations, and the orthogonality by the Arthur–Selberg trace formula; the abelian statement of this article is the boundary case of the general theory of *The Langlands Program*.

## Summary

A Hecke character of a number field is a continuous homomorphism from the idèle class group to the circle group, factoring as a product of local characters; for $\mathbb{Q}$ these are the Dirichlet characters. The characters satisfy the conjugate orthogonality $\langle\chi,\psi\rangle=\delta_{\chi\psi}$, which specialises for the Dirichlet characters modulo $q$ to $\frac1{\varphi(q)}\sum_a\chi(a)\overline{\psi(a)}=\delta_{\chi\psi}$, and the arithmetic content of the pairing is the conductor-discriminant formula, $\mathfrak{d}_{L/K}=\prod_\chi\mathfrak{f}(\chi)$, which expresses the discriminant of an abelian extension as the product of the conductors of its characters. The degenerate cases are the characters of unbounded conductor, the archimedean ramification, the quasi-characters and the nonabelian generalisation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C_K=I_K/K^\times$ | Idèle class group |
| $\chi:C_K\to\mathbb{T}$ | Hecke character |
| $\chi=\prod_v\chi_v$ | Local factorisation |
| $\mathfrak{f}(\chi)$ | Conductor |
| $L(s,\chi)$ | Hecke $L$-function |
| $W(\chi)$ | Root number |
| $\langle\chi,\psi\rangle=\delta_{\chi\psi}$ | Conjugate orthogonality |
| $\mathfrak{d}_{L/K}=\prod_\chi\mathfrak{f}(\chi)$ | Conductor-discriminant formula |
| $\widehat G$ | Dual group |

## Further Reading

- John Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions* (thesis, Princeton, 1950), for the Hecke characters and their $L$-functions.
- John Cassels and Albrecht Fröhlich, *Algebraic Number Theory* (Academic Press, 1967), for the conductor-discriminant formula and the class field theory.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for the Hecke characters and the idèle class group.
- Edwin Hewitt and Kenneth Ross, *Abstract Harmonic Analysis* (Springer, 1963), for the orthogonality and the duality of locally compact abelian groups.
- Jean-Pierre Serre, *Abelian $\ell$-adic Representations and Elliptic Curves* (Benjamin, 1968), for the correspondence with the Galois characters.
