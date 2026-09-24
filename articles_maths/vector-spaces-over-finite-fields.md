
# __Vector Spaces over Finite Fields__

## Introduction

Over a finite field the linear algebra of a vector space becomes finite combinatorics: a space of dimension $n$ over $\mathbb{F}_q$ has exactly $q^n$ elements, its automorphism group is finite, and its subspaces of a given dimension can be counted exactly. The counts are given by the Gaussian binomial coefficients, which are the $q$-analogues of the ordinary binomial coefficients and specialise to them as $q \to 1$. This article carries out the counting: the order of $\operatorname{GL}_n(\mathbb{F}_q)$ by counting ordered bases, the number of $k$-dimensional subspaces by a two-way count of independent tuples, the recursion and the $q \to 1$ limit of the Gaussian binomials, and the consequences for projective spaces and for the small classical groups.

Throughout, $q$ is a prime power and $\mathbb{F}_q$ is the field with $q$ elements, whose existence and uniqueness are established in the companion category of *Fields*; $V$ is a vector space of dimension $n$ over $\mathbb{F}_q$. The general linear group and its order are those of the companion article of this category on the general linear group, and the determinant and the special linear group are those of the companion article on the special linear group and the determinant; the present article computes the numerical invariants those articles leave open over a general field.

## Finite-Dimensional Spaces and Their Bases

### The Cardinality

**Proposition.** A finite-dimensional $\mathbb{F}_q$-vector space of dimension $n$ has exactly $q^n$ elements, and the number of ordered $k$-tuples of linearly independent vectors is

$$
N(n,k)=(q^n-1)(q^n-q)\cdots(q^n-q^{k-1})=\prod_{i=0}^{k-1}(q^n-q^i) .
$$

*Proof.* Choosing coordinates identifies $V$ with $\mathbb{F}_q^n$, of cardinality $q^n$. For the count, choose the first vector to be nonzero, with $q^n-1$ choices; having chosen $i$ independent vectors, their span has $q^i$ elements, so the next vector must avoid it, leaving $q^n-q^i$ choices. $\square$

**Corollary.** The number of ordered bases of $V$ is $N(n,n)=\prod_{i=0}^{n-1}(q^n-q^i)$.

### The Order of the General Linear Group

**Theorem.** The order of the general linear group is

$$
|\operatorname{GL}_n(\mathbb{F}_q)|=\prod_{i=0}^{n-1}(q^n-q^i)=q^{n(n-1)/2}\prod_{i=1}^{n}(q^i-1) .
$$

*Proof.* An invertible matrix is exactly an ordered basis of $\mathbb{F}_q^n$, read as the list of its columns: a matrix is invertible if and only if its columns are linearly independent, and every ordered basis occurs exactly once. Hence the order is the number of ordered bases, which is the previous corollary. For the second expression, write $q^n-q^i=q^i(q^{n-i}-1)$ and collect: the exponents sum to $\sum_{i=0}^{n-1}i=n(n-1)/2$, and reindexing gives $\prod_{i=1}^n(q^i-1)$. $\square$

**Corollary.** The special linear group has order

$$
|\operatorname{SL}_n(\mathbb{F}_q)|=\frac{|\operatorname{GL}_n(\mathbb{F}_q)|}{q-1}=\frac{\prod_{i=0}^{n-1}(q^n-q^i)}{q-1},
$$

since the determinant $\operatorname{GL}_n(\mathbb{F}_q) \to \mathbb{F}_q^{\times}$ is surjective with kernel $\operatorname{SL}_n(\mathbb{F}_q)$ and $|\mathbb{F}_q^{\times}|=q-1$; the fibre over any nonzero scalar is a coset and therefore has the same cardinality.

**Example.** For $n=2$: $|\operatorname{GL}_2(\mathbb{F}_q)|=(q^2-1)(q^2-q)=q(q-1)^2(q+1)$, and $|\operatorname{SL}_2(\mathbb{F}_q)|=q(q-1)(q+1)=q^3-q$. At $q=2$ this gives $|\operatorname{GL}_2(\mathbb{F}_2)|=6=|\operatorname{SL}_2(\mathbb{F}_2)|$, consistent with $\operatorname{GL}_2(\mathbb{F}_2)=\operatorname{SL}_2(\mathbb{F}_2) \cong S_3$; at $q=3$ it gives $|\operatorname{GL}_2(\mathbb{F}_3)|=48$ and $|\operatorname{SL}_2(\mathbb{F}_3)|=24$.

## Counting Subspaces

### The Gaussian Binomial Coefficient

**Definition.** For integers $0 \le k \le n$, the **Gaussian binomial coefficient** is

$$
\binom{n}{k}_q=\frac{(q^n-1)(q^{n-1}-1)\cdots(q^{n-k+1}-1)}{(q^k-1)(q^{k-1}-1)\cdots(q-1)}=\prod_{i=1}^{k}\frac{q^{n-k+i}-1}{q^i-1} .
$$

It is a polynomial in $q$ with integer coefficients; the value at $q=1$ is the ordinary binomial coefficient $\binom{n}{k}$.

**Theorem.** The number of $k$-dimensional subspaces of an $n$-dimensional vector space over $\mathbb{F}_q$ is $\binom{n}{k}_q$.

*Proof.* Count the pairs (ordered $k$-tuple of independent vectors, $k$-dimensional subspace containing them) in two ways. The number of independent $k$-tuples is $N(n,k)=\prod_{i=0}^{k-1}(q^n-q^i)$. Each $k$-dimensional subspace $W$ contains $N(k,k)=\prod_{i=0}^{k-1}(q^k-q^i)$ independent $k$-tuples, namely its ordered bases. Dividing,

$$
\#\{W:\dim W=k\}=\frac{\prod_{i=0}^{k-1}(q^n-q^i)}{\prod_{i=0}^{k-1}(q^k-q^i)} =\prod_{i=0}^{k-1}\frac{q^n-q^i}{q^k-q^i},
$$

and simplifying $\dfrac{q^n-q^i}{q^k-q^i}=\dfrac{q^{n-i}-1}{q^{k-i}-1}$ and reindexing gives the stated product. $\square$

**Corollary.** The number of lines (one-dimensional subspaces) equals the number of hyperplanes (codimension-one subspaces), both equal to $\dfrac{q^n-1}{q-1}=1+q+\cdots+q^{n-1}$.

*Proof.* The count of lines is $\binom{n}{1}_q=(q^n-1)/(q-1)$, and the count of hyperplanes is $\binom{n}{n-1}_q=(q^n-1)/(q-1)$; the symmetry is the duality $W \mapsto W^{\perp}$ for a nondegenerate bilinear form, or directly the identity $\binom{n}{k}_q=\binom{n}{n-k}_q$ from the formula. $\square$

**Corollary (symmetry and the $q \to 1$ limit).** $\binom{n}{k}_q=\binom{n}{n-k}_q$, and $\lim_{q \to 1}\binom{n}{k}_q=\binom{n}{k}$ for a complex $q$ approaching $1$; the Gaussian binomial therefore interpolates the ordinary binomial, the case $q=1$ being the analogue of a one-element field.

*Proof.* Symmetry is immediate from the product display for $k$ and for $n-k$. For the limit, $\frac{q^m-1}{q^r-1} \to \frac{m}{r}$ as $q \to 1$, so the product $\prod_{i=1}^k\frac{q^{n-k+i}-1}{q^i-1}$ tends to $\prod_{i=1}^k\frac{n-k+i}{i}=\binom{n}{k}$. $\square$

### The Recursion

**Proposition (Pascal recursion).** $\binom{n}{k}_q=\binom{n-1}{k-1}_q+q^k\binom{n-1}{k}_q$.

*Proof.* Put $A=\binom{n}{k}_q$, $B=\binom{n-1}{k-1}_q$ and $C=\binom{n-1}{k}_q$. From the product formula, $A=B\cdot\dfrac{q^n-1}{q^k-1}$, and $q^kC=B\cdot\dfrac{q^n-q^k}{q^k-1}$. Adding,

$$
B+q^kC=B\cdot\frac{q^k-1+q^n-q^k}{q^k-1}=B\cdot\frac{q^n-1}{q^k-1}=A . \qquad \square
$$

Geometrically, fixing a hyperplane $H$, a $k$-subspace lies in $H$, contributing $C$, or meets $H$ in a $(k-1)$-subspace $W_0$; for each of the $B$ choices of $W_0$ there are $q^{n-k}$ such subspaces, namely the lines of $V/W_0$ not lying in the hyperplane $H/W_0$, so that $\binom{n}{k}_q=C+q^{n-k}B$. This is the equivalent form of the recursion displayed, the two agreeing by the symmetry $\binom{n-1}{k}_q=\binom{n-1}{n-1-k}_q$.

## Projective Spaces and Flags

**Definition.** The **projective space** $\mathbb{P}^{n-1}(\mathbb{F}_q)$ is the set of lines through the origin of $\mathbb{F}_q^n$, that is, the set of one-dimensional subspaces; it is the quotient of $\mathbb{F}_q^n \setminus \{0\}$ by scaling by $\mathbb{F}_q^{\times}$. A **flag** is a chain $0=V_0 \subset V_1 \subset \cdots \subset V_n=V$ with $\dim V_i=i$.

**Proposition.** $|\mathbb{P}^{n-1}(\mathbb{F}_q)|=\dfrac{q^n-1}{q-1}=1+q+\cdots+q^{n-1}$. The number of complete flags is

$$
\prod_{i=1}^{n}\frac{q^{i}-1}{q-1}=\prod_{i=1}^{n}(1+q+\cdots+q^{i-1}) .
$$

*Proof.* The first is the count of lines. For the second, build the flag by choosing $V_1$ in $\binom{n}{1}_q$ ways, then $V_2/V_1$ as a line in the $(n-1)$-dimensional quotient $V/V_1$ in $\binom{n-1}{1}_q$ ways, and so on; the product is $\prod_{i=1}^n\frac{q^{i}-1}{q-1}$. $\square$

**Example.** For $n=3$ and $q=2$: the number of lines and of planes in $\mathbb{F}_2^3$ is each $\binom{3}{1}_2=\binom{3}{2}_2=7$, and the number of points of the projective plane is $7$; the number of complete flags is $(1)(1+2)(1+2+4)=1\cdot3\cdot7=21$. The Gaussian binomials are $\binom{3}{0}_2=\binom{3}{3}_2=1$, $\binom{3}{1}_2=\binom{3}{2}_2=7$, and the total number of subspaces is $1+7+7+1=16$.

**Example.** For $n=2$: $\binom{2}{1}_q=q+1$, so a finite line has $q+1$ points of the projective line; and $|\operatorname{GL}_2(\mathbb{F}_q)|=q(q-1)^2(q+1)$, whose factor $q+1$ counts the projective points and whose factors $q(q-1)^2$ count the stabiliser $\operatorname{GL}_2$ of a line.

## Irreducible Polynomials and Similarity Classes

**Definition.** Let $N_n(q)$ be the number of monic irreducible polynomials of degree $n$ in $\mathbb{F}_q[x]$.

**Proposition.** $\sum_{d \mid n}dN_d(q)=q^n$, and by Möbius inversion

$$
N_n(q)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d} .
$$

*Proof.* Count the $q^n$ monic polynomials of degree $n$ by their factorisation into monic irreducibles, grouping the factors by degree: a monic irreducible of degree $d$ contributes $d$ to the degree, and each monic polynomial of degree $n$ arises once, giving $q^n=\sum_{d\mid n}dN_d(q)$. Möbius inversion of this divisor identity gives the displayed formula. $\square$

**Example.** $N_1(q)=q$, the linear polynomials; $N_2(q)=(q^2-q)/2$; $N_3(q)=(q^3-q)/3$; $N_4(q)=(q^4-q^2)/4$. For $q=2$ these are $2,1,2,3$: the linear $x,x+1$, the quadratic $x^2+x+1$, the cubics $x^3+x+1$ and $x^3+x^2+1$, and three quartics.

**Theorem (similarity classes).** The number of similarity classes of $n \times n$ matrices over $\mathbb{F}_q$ is the coefficient of $t^n$ in

$$
\prod_{m\ge1}(1-t^m)^{-a_m}, \qquad a_m=\sum_{d\mid m}N_d(q) .
$$

*Proof.* By the structure theorem a similarity class is determined by its multiset of elementary divisors, the prime powers $f^e$ with $f$ monic irreducible. For a fixed irreducible $f$ of degree $d$, the possible exponents $e \ge 1$ contribute the factor $\prod_{e\ge1}(1-t^{de})^{-1}$ to the generating function for total degree, so the count is $\prod_d\bigl(\prod_e(1-t^{de})^{-1}\bigr)^{N_d}$. Collecting the factors with $de=m$ gives the displayed product with exponent $a_m$. $\square$

**Example.** For $n=2$ the coefficient is $a_2+\binom{a_1+1}{2}=\bigl(N_1+N_2\bigr)+\frac{q(q+1)}{2}=q^2+q$, so there are $q^2+q$ similarity classes of $2\times2$ matrices over $\mathbb{F}_q$; at $q=2$ this is $6$, namely the two scalars, the two Jordan blocks $J_2(0),J_2(1)$, the companion matrix of $x^2+x+1$, and $\operatorname{diag}(0,1)$.

## Summary

Over $\mathbb{F}_q$ a vector space of dimension $n$ has $q^n$ elements, and the number of ordered $k$-tuples of independent vectors is $\prod_{i=0}^{k-1}(q^n-q^i)$, obtained by excluding successively the spans of the vectors already chosen. The number of ordered bases, and hence the order of the general linear group, is $\prod_{i=0}^{n-1}(q^n-q^i)=q^{n(n-1)/2}\prod_{i=1}^n(q^i-1)$, since an invertible matrix is exactly an ordered basis of the coordinate space; the determinant is surjective onto $\mathbb{F}_q^{\times}$ with kernel $\operatorname{SL}_n(\mathbb{F}_q)$, so $|\operatorname{SL}_n(\mathbb{F}_q)|=|\operatorname{GL}_n(\mathbb{F}_q)|/(q-1)$. For $n=2$ these read $q(q-1)^2(q+1)$ and $q^3-q$.

The number of $k$-dimensional subspaces is the Gaussian binomial coefficient $\binom{n}{k}_q=\prod_{i=1}^k(q^{n-k+i}-1)/(q^i-1)$, obtained by counting independent $k$-tuples globally and per subspace; it is symmetric, $\binom{n}{k}_q=\binom{n}{n-k}_q$, satisfies the Pascal recursion $\binom{n}{k}_q=\binom{n-1}{k-1}_q+q^k\binom{n-1}{k}_q$, and tends to the ordinary binomial $\binom{n}{k}$ as $q \to 1$. In particular the number of lines and the number of hyperplanes are both $(q^n-1)/(q-1)$, which is also the cardinality of the projective space $\mathbb{P}^{n-1}(\mathbb{F}_q)$; the number of complete flags is $\prod_{i=1}^n(q^i-1)/(q-1)$. In $\mathbb{F}_2^3$ this gives seven lines, seven planes, $21$ complete flags and sixteen subspaces in all.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{F}_q$ | the field with $q$ elements, $q$ a prime power |
| $V$ | $n$-dimensional $\mathbb{F}_q$-vector space |
| $N(n,k)=\prod_{i=0}^{k-1}(q^n-q^i)$ | independent $k$-tuples |
| $\operatorname{GL}_n(\mathbb{F}_q)$, $\operatorname{SL}_n(\mathbb{F}_q)$ | general and special linear groups |
| $\binom{n}{k}_q$ | Gaussian binomial coefficient |
| $\mathbb{F}_q^{\times}$ | multiplicative group of the field, order $q-1$ |
| $\mathbb{P}^{n-1}(\mathbb{F}_q)$ | projective space of lines |
| $W^{\perp}$ | orthogonal complement for a bilinear form |
| $V_0 \subset \cdots \subset V_n$ | complete flag |

## Further Reading

- Michael Artin, *Algebra* (Pearson, 2nd ed. 2011), for the finite-field linear groups.
- Peter J. Cameron, *Projective and Polar Spaces* (Queen Mary, 1991), for the combinatorial geometry of finite vector spaces.
- John B. Fraleigh, *A First Course in Abstract Algebra* (Pearson, 7th ed. 2002), for the finite fields and their linear algebra.
- Daniel E. Knuth, *The Art of Computer Programming, Vol. 4A* (Addison-Wesley, 2011), for Gaussian binomial coefficients and their combinatorics.
- Rudolf Lidl and Harald Niederreiter, *Finite Fields* (Cambridge University Press, 2nd ed. 1997), for the structure of $\mathbb{F}_q$ and its uses.
- Zhe-Xian Wan, *Geometry of Classical Groups over Finite Fields* (Studentlitteratur, 2nd ed. 2002), for the deeper counting problems.
