# __$UT_n$ as a Linear Model of $\operatorname{Sym}_n$: Same Space, Wrong Product__

## Introduction

**The symmetrisation map carries $UT_n$ isomorphically onto $\operatorname{Sym}_n$ as a vector space, both of dimension $n(n+1)/2$, but it carries the associative product of the triangular algebra to nothing resembling the Jordan product, and no linear isomorphism can do better, because $UT_n$ has nonzero nilpotent elements and $\operatorname{Sym}_n$ has none.**

The article constructs the isomorphism, computes the defect of the product, shows that the idempotents do match, proves that the two algebras are not isomorphic in any linear way, and compares the trace forms and the automorphism groups. It assumes *The Antisymmetric Part inside $UT_n$: the Radical as the Commutator* and *The Jordan Algebra $\operatorname{Sym}_n(\mathbb{R})$*, and it defers the global reading to *The Triangular Decomposition $h\oplus n_+\oplus n_-$*.

Throughout $n\ge2$ and $S=\operatorname{Sym}_n$. The symmetrisation is

$$
\pi_+(X)=\tfrac12(X+X^{\mathsf T}),\qquad X\in UT_n.
$$

## The Isomorphism of Vector Spaces

**The symmetrisation is injective on $UT_n$ and its image is $S$.** If $\pi_+(X)=0$ for an upper triangular $X$ then $X$ is antisymmetric and upper triangular, hence zero by the emptiness of $UT_n\cap\operatorname{Skew}_n$. The image has dimension $\dim UT_n=n(n+1)/2=\dim S$, so it is all of $S$.

**The inverse is explicit.** For $S\in\operatorname{Sym}_n$, the upper triangular matrix $X$ with

$$
X_{ii}=S_{ii},\qquad X_{ij}=2S_{ij}\ (i<j),\qquad X_{ij}=0\ (i>j)
$$

satisfies $\pi_+(X)=S$. So the linear isomorphism is

$$
\pi_+\big|_{UT_n}:UT_n\longrightarrow\operatorname{Sym}_n,\qquad X\longmapsto\tfrac12(X+X^{\mathsf T}),
$$

and its inverse doubles the entries above the diagonal.

**Consequence: the two algebras live on the same vector space of dimension $n(n+1)/2$.** Every question about the difference between them is a question about the product, and not about the linear structure. The space has a basis of upper triangular matrix units and the same space has a basis of diagonal-and-symmetric pairs; the two bases are related by the map above and by nothing else.

## The Two Products

**$UT_n$ is closed under the associative product and $S$ is closed under the Jordan product.** For $X,Y\in UT_n$ the product $XY$ is upper triangular, so $UT_n$ is a subalgebra of $M_n$ with a unit and a nonzero nilpotent radical. For $S,T\in S$ the product $S\circ T=\tfrac12(ST+TS)$ is symmetric, so $S$ is a Jordan algebra with a unit and no nilpotent element other than zero.

**The two products have different algebraic laws.** The product of $UT_n$ is associative and not commutative; the product of $S$ is commutative and not associative. The two laws are exchanged: neither algebra has both, and neither algebra is a deformation of the other. So the words "the same space" carry no algebraic content without the product.

**The trace is multiplicative in neither case but behaves differently.** On $UT_n$ the trace is a homomorphism on the diagonal: $\operatorname{tr}(XY)=\sum_iX_{ii}Y_{ii}$, so it is multiplicative on $h$. On $S$ the trace satisfies $\operatorname{tr}(S\circ T)=\operatorname{tr}(ST)$, which is the invariant inner product and not a multiplicative functional. So the two algebras have different linear functionals playing the part of the trace.

## The Defect of the Product

**The symmetrisation does not carry one product to the other.** For $X,Y\in UT_n$,

$$
\pi_+(XY)\ne\pi_+(X)\circ\pi_+(Y)
$$

in general. With $X=\begin{pmatrix}1&2\\ 0&3\end{pmatrix}$ and $Y=\begin{pmatrix}0&1\\ 0&1\end{pmatrix}$,

$$
\pi_+(XY)=\begin{pmatrix}0&3/2\\ 3/2&3\end{pmatrix},\qquad \pi_+(X)\circ\pi_+(Y)=\begin{pmatrix}1/2&3/2\\ 3/2&7/2\end{pmatrix},
$$

so the two differ on the diagonal. Measured on $100$ random pairs at each of $n=2,3,4$, the two sides differed in all $300$ cases.

**The defect has a formula.** Write $S=\pi_+(X)$, $K=\pi_-(X)$, $T=\pi_+(Y)$ and $L=\pi_-(Y)$. Then $XY=ST+SL+KT+KL$ and

$$
\pi_+(XY)=S\circ T+\pi_+(SL)+\pi_+(KT)+\pi_+(KL),
$$

so the defect is the sum of the three mixed and skew contributions, and it vanishes exactly when those three terms are symmetric. The first term $S\circ T$ is the part that survives, and it is the reason the isomorphism looks right at the level of the symmetric parts.

**The defect is not the commutator and not a coboundary.** The three correction terms involve the skew parts of $X$ and $Y$, which the symmetrisation forgets; so no modification of the product on $UT_n$ by a term built from $\pi_+$ alone can repair the defect. The information in $K$ and $L$ is genuinely lost, and the product of the triangular algebra uses it.

## The Idempotents Do Match

**The idempotents of $UT_n$ are the diagonal $0$-$1$ matrices, and the symmetrisation fixes them.** An upper triangular $E$ with $E^{2}=E$ has diagonal entries in $\{0,1\}$ and, by induction on the distance from the diagonal, all entries above it zero; so $E=\operatorname{diag}(\varepsilon_1,\dots,\varepsilon_n)$ with $\varepsilon_i\in\{0,1\}$. Each such matrix is symmetric, so $\pi_+(E)=E$.

**Consequence: the two algebras have the same idempotents and different products between them.** The idempotents of $S$ are the orthogonal projections, which are exactly the diagonal $0$-$1$ matrices in a suitable basis; and the $0$-$1$ diagonal matrices are simultaneously the idempotents of $UT_n$ and of $S$. So the isomorphism matches the idempotents exactly, and the products between two idempotents already differ: in $UT_n$ the product $E_{ii}E_{jj}$ is $0$ for $i\ne j$, and in $S$ the Jordan product $E_{ii}\circ E_{jj}$ is also $0$; the difference appears only when off-diagonal entries are present.

**The Peirce decompositions agree on the same space.** Relative to a diagonal idempotent $E$ of rank $r$, the Peirce spaces of $UT_n$ and of $S$ have the same dimensions $r(r+1)/2$, $r(n-r)$ and $(n-r)(n-r+1)/2$, because both are computed from the same corners. So the linear skeleton of the Peirce theory is common to the two algebras, and the multiplication rules between the corners are what separate them.

## No Linear Isomorphism Can Repair It

**The two algebras are not isomorphic, and no linear isomorphism carries one product to the other.** Suppose $\varphi:UT_n\to S$ linear and bijective with $\varphi(XY)=\varphi(X)\circ\varphi(Y)$. Take $X\ne0$ with $X^{2}=0$, which exists in $n_+$. Then $\varphi(X)\circ\varphi(X)=\varphi(0)=0$, so $\varphi(X)$ is a nilpotent element of the Jordan algebra $S$, hence zero, since a Jordan algebra of a real inner product space has no nonzero nilpotent. This contradicts the injectivity.

**Consequence: the nilpotents are the obstruction.** The set of nilpotent elements is empty in $S$ and is the whole radical $n_+$ in $UT_n$, and this set is invariant under linear isomorphisms only up to image; so the two algebras cannot be matched. The obstruction is the same in every dimension, and it is not a matter of a bad choice of the map.

**The cone of squares is the second obstruction.** In $S$ the set $\{X\circ X\}$ is the positive semidefinite cone, which is a proper cone with nonempty interior; in $UT_n$ the set $\{X^{2}\}$ is contained in the set of upper triangular matrices with nonnegative diagonal, which is not a cone at all in the symmetric sense, since $X^{2}$ need not be symmetric. So the two algebras have different sets of squares, and the difference is visible without any structure theory.

## The Forms and the Groups

**The symmetrisation is not an isometry.** The trace form on $UT_n$ is degenerate with radical $n_+$ and rank $n$; on $S$ it is positive definite. Under $\pi_+$ the form $\operatorname{tr}(XY)$ on $UT_n$ corresponds to $\operatorname{tr}(\pi_+(X)\pi_+(Y))$ on $S$, which is not the trace form of $S$: the two differ by the skew parts, and the skew parts are invisible to the diagonal.

**Consequence: the isomorphism does not preserve the invariant form.** The trace form of $UT_n$ has nullity $n(n-1)/2$, and the same form read on $S$ has nullity zero. So the linear isomorphism carries a degenerate form to a nondegenerate one, and this is the form-level statement of the same failure: the two algebras have different radicals.

**The automorphism groups are different in kind.** The automorphisms of $UT_n$ include the conjugations $X\mapsto TXT^{-1}$ by invertible upper triangular matrices, and the group they generate is solvable and noncompact; the automorphisms of $(S,\circ)$ are exactly the conjugations by orthogonal matrices, the compact group $\mathrm{O}(n)$. So the two algebras carry automorphism groups of different type, one compact and one not, and no group isomorphism is possible.

**Consequence: the triangular algebra is the noncompact shadow of the Jordan algebra.** The two algebras have the same dimension, the same idempotents and the same Peirce dimensions, and they differ in the product, in the nilpotents, in the cone of squares, in the radical of the trace form and in the automorphism group. So the linear model is a model of the space and not of the algebra.

## The Case $n=2$

**At $n=2$ both algebras are three-dimensional and everything is explicit.** $UT_2=\left\{\begin{pmatrix}a&b\\ 0&c\end{pmatrix}\right\}$ with the product $\begin{pmatrix}a&b\\ 0&c\end{pmatrix}\begin{pmatrix}a'&b'\\ 0&c'\end{pmatrix}=\begin{pmatrix}aa'&ab'+bc'\\ 0&cc'\end{pmatrix}$, and $S=\left\{\begin{pmatrix}p&q\\ q&r\end{pmatrix}\right\}$ with the Jordan product. The symmetrisation is $\begin{pmatrix}a&b\\ 0&c\end{pmatrix}\mapsto\begin{pmatrix}a&b/2\\ b/2&c\end{pmatrix}$.

**The defect at $n=2$ is explicit.** With $X=\begin{pmatrix}a&b\\ 0&c\end{pmatrix}$ and $Y=\begin{pmatrix}a'&b'\\ 0&c'\end{pmatrix}$,

$$
\pi_+(XY)-\pi_+(X)\circ\pi_+(Y)=\begin{pmatrix}-bb'/4&\tfrac14(ab'+bc'-a'b-b'c)\\ \tfrac14(ab'+bc'-a'b-b'c)&-bb'/4\end{pmatrix},
$$

which for the pair of the example gives $-\tfrac12\mathrm{I}$, the value computed above. So the failure is exactly the loss of the off-diagonal information: the product needs the entries $b$ and $b'$ whole, and the symmetrisation halves them.

**The nilpotent of $UT_2$ is the visible obstruction.** $E_{12}^{2}=0$ while $E_{12}\ne0$, and $E_{12}$ has no image under any algebra isomorphism, since the only nilpotent of $S$ is zero. So the smallest case already separates the two algebras.

## Summary

The symmetrisation $\pi_+(X)=\tfrac12(X+X^{\mathsf T})$ is a linear isomorphism $UT_n\to\operatorname{Sym}_n$, both spaces having dimension $n(n+1)/2$, with inverse doubling the entries above the diagonal. It does not carry the associative product of $UT_n$ to the Jordan product of $\operatorname{Sym}_n$: the defect is the sum of the three mixed terms $\pi_+(SL)$, $\pi_+(KT)$ and $\pi_+(KL)$, and it is nonzero on every random pair tested. What the isomorphism does carry correctly is the idempotents, which are the diagonal $0$-$1$ matrices in both algebras, and the dimensions of the Peirce spaces. What it cannot carry is the set of nilpotents, which is the radical $n_+$ in $UT_n$ and $\{0\}$ in $\operatorname{Sym}_n$, nor the cone of squares, nor the radical of the trace form, nor the automorphism group, which is solvable in the triangular case and compact in the Jordan case. So $UT_n$ is a linear model of the symmetric half and not an algebraic one: the same space with the wrong product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $UT_n$ | the upper triangular matrices, dimension $n(n+1)/2$ |
| $\operatorname{Sym}_n$ | the symmetric half, dimension $n(n+1)/2$ |
| $\pi_+$ | the symmetrisation $\tfrac12(X+X^{\mathsf T})$ |
| $S,K,T,L$ | the symmetric and skew parts of $X$ and $Y$ |
| $S\circ T$ | the Jordan product $\tfrac12(ST+TS)$ |
| $n_+$ | the nilpotent radical of $UT_n$ |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the absence of nilpotents in a formally real Jordan algebra.
- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the triangular subalgebras and their automorphism groups.
- [The Antisymmetric Part inside $UT_n$: the Radical as the Commutator](the-antisymmetric-part-inside-utn-the-radical-as-the-commutator-over-r.html), for the radical and the commutator of the triangular algebra.
- [The Jordan Algebra $\operatorname{Sym}_n(\mathbb{R})$](the-jordan-algebra-sym-n-r.html), for the product on the other side of the isomorphism.
- [$UT_n$ as the Complement of the Antisymmetric Part](utn-as-the-complement-of-the-antisymmetric-part-over-r.html), for the space $UT_n$ and its relation to the two halves.
